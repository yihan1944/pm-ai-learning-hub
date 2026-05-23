"""
Bilibili 字幕提取工具
用法: python bilibili_subtitle.py <B站视频URL> [选项]
输出: 纯文本字幕 .txt 文件

选项:
  -o, --output DIR      输出目录 (默认: 当前目录)
  -w, --whisper         没有字幕时使用 Whisper 语音识别
  -m, --model MODEL     Whisper 模型大小: tiny, base, small, medium, large (默认: base)
  --keep-audio          保留下载的音频文件
"""

import re
import sys
import json
import os
import argparse
import subprocess
import tempfile

try:
    import requests
except ImportError:
    print("错误: 需要安装 requests 库")
    print("请运行: pip install requests")
    sys.exit(1)


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.bilibili.com",
}

TIMEOUT = 30  # 请求超时时间（秒）


def check_whisper():
    """检查 Whisper 是否可用"""
    try:
        import whisper
        return True
    except ImportError:
        return False


def check_ffmpeg():
    """检查 ffmpeg 是否可用"""
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except FileNotFoundError:
        return False


def extract_bvid(url: str) -> str:
    """从B站链接中提取BV号"""
    match = re.search(r"(BV[\w]+)", url)
    if not match:
        raise ValueError(f"无法从URL中提取BV号: {url}")
    return match.group(1)


def get_video_info(bvid: str) -> tuple[int, str]:
    """获取视频的cid和标题"""
    try:
        resp = requests.get(
            "https://api.bilibili.com/x/web-interface/view",
            params={"bvid": bvid},
            headers=HEADERS,
            timeout=TIMEOUT,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"网络请求失败: {e}")
    except json.JSONDecodeError:
        raise RuntimeError("响应数据解析失败")

    if data["code"] != 0:
        if data["code"] == -400:
            raise RuntimeError("请求错误，请检查BV号是否正确")
        elif data["code"] == -404:
            raise RuntimeError("视频不存在或已被删除")
        elif data["code"] == 62002:
            raise RuntimeError("视频不可访问，可能需要登录或视频已下架")
        else:
            raise RuntimeError(f"获取视频信息失败: {data.get('message', '未知错误')}")

    return data["data"]["cid"], data["data"]["title"]


def get_subtitle_list(bvid: str, cid: int) -> list[dict]:
    """获取字幕列表"""
    try:
        resp = requests.get(
            "https://api.bilibili.com/x/player/wbi/v2",
            params={"bvid": bvid, "cid": cid},
            headers=HEADERS,
            timeout=TIMEOUT,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"网络请求失败: {e}")
    except json.JSONDecodeError:
        raise RuntimeError("响应数据解析失败")

    if data["code"] != 0:
        raise RuntimeError(f"获取播放器信息失败: {data.get('message', '未知错误')}")

    subtitle_info = data.get("data", {}).get("subtitle", {})
    subtitles = subtitle_info.get("subtitles", [])

    if not subtitles:
        # 可能需要登录才能获取字幕
        if not data.get("data", {}).get("login_mid", 0):
            print("提示: 未登录状态，某些视频的字幕可能需要登录才能获取")

    return subtitles


def fetch_subtitle_text(subtitle_url: str) -> str:
    """下载字幕JSON并提取纯文本"""
    # 处理相对协议URL
    if subtitle_url.startswith("//"):
        subtitle_url = "https:" + subtitle_url
    elif not subtitle_url.startswith("http"):
        subtitle_url = "https://" + subtitle_url

    try:
        resp = requests.get(subtitle_url, headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        sub_data = resp.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"下载字幕失败: {e}")
    except json.JSONDecodeError:
        raise RuntimeError("字幕数据解析失败")

    body = sub_data.get("body", [])
    if not body:
        return ""

    lines = [item["content"] for item in body if item.get("content")]
    return "\n".join(lines)


def get_audio_url(bvid: str, cid: int) -> str:
    """获取视频音频流地址"""
    try:
        resp = requests.get(
            "https://api.bilibili.com/x/player/wbi/v2",
            params={"bvid": bvid, "cid": cid},
            headers=HEADERS,
            timeout=TIMEOUT,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"网络请求失败: {e}")
    except json.JSONDecodeError:
        raise RuntimeError("响应数据解析失败")

    if data["code"] != 0:
        raise RuntimeError(f"获取播放器信息失败: {data.get('message', '未知错误')}")

    dash = data.get("data", {}).get("dash", {})
    audio_list = dash.get("audio", [])

    if not audio_list:
        raise RuntimeError("未找到音频流，可能需要登录或视频已下架")

    # 选择最高质量的音频
    audio_list.sort(key=lambda x: x.get("bandwidth", 0), reverse=True)
    return audio_list[0]["baseUrl"]


def download_audio(audio_url: str, output_path: str) -> str:
    """下载音频文件"""
    headers = HEADERS.copy()
    headers["Range"] = "bytes=0-"

    try:
        resp = requests.get(audio_url, headers=headers, timeout=120, stream=True)
        resp.raise_for_status()

        with open(output_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)

        return output_path
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"下载音频失败: {e}")


def convert_to_wav(input_path: str, output_path: str) -> str:
    """使用 ffmpeg 转换音频格式为 WAV"""
    try:
        subprocess.run(
            [
                "ffmpeg", "-i", input_path,
                "-vn",  # 不包含视频
                "-acodec", "pcm_s16le",  # 16位PCM
                "-ar", "16000",  # 16kHz采样率
                "-ac", "1",  # 单声道
                "-y",  # 覆盖输出文件
                output_path,
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        return output_path
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"音频转换失败: {e}")
    except FileNotFoundError:
        raise RuntimeError("未找到 ffmpeg，请先安装 ffmpeg")


def transcribe_with_whisper(audio_path: str, model_name: str = "base") -> str:
    """使用 Whisper 进行语音识别"""
    try:
        import whisper
    except ImportError:
        raise RuntimeError("未安装 whisper，请运行: pip install openai-whisper")

    print(f"正在加载 Whisper 模型: {model_name}")
    try:
        model = whisper.load_model(model_name)
    except Exception as e:
        raise RuntimeError(f"加载 Whisper 模型失败: {e}")

    print("正在识别音频...")
    try:
        result = model.transcribe(audio_path, language="zh")
    except Exception as e:
        raise RuntimeError(f"语音识别失败: {e}")

    # 提取文本
    segments = result.get("segments", [])
    lines = [seg["text"].strip() for seg in segments if seg.get("text")]

    return "\n".join(lines)


def sanitize_filename(name: str) -> str:
    """清理文件名中的非法字符"""
    return re.sub(r'[\\/:*?"<>|]', "_", name).strip()


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description="Bilibili 字幕提取工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s https://www.bilibili.com/video/BV1xx411c7mD
  %(prog)s https://www.bilibili.com/video/BV1xx411c7mD -o ./output
  %(prog)s https://www.bilibili.com/video/BV1xx411c7mD -w -m small
        """,
    )
    parser.add_argument("url", help="B站视频URL")
    parser.add_argument("-o", "--output", default=".", help="输出目录 (默认: 当前目录)")
    parser.add_argument(
        "-w", "--whisper",
        action="store_true",
        help="没有字幕时使用 Whisper 语音识别",
    )
    parser.add_argument(
        "-m", "--model",
        default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper 模型大小 (默认: base)",
    )
    parser.add_argument(
        "--keep-audio",
        action="store_true",
        help="保留下载的音频文件",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # 创建输出目录
    if args.output != "." and not os.path.exists(args.output):
        os.makedirs(args.output, exist_ok=True)

    print(f"正在解析视频: {args.url}")

    try:
        bvid = extract_bvid(args.url)
        print(f"BV号: {bvid}")

        cid, title = get_video_info(bvid)
        print(f"视频标题: {title}")
        print(f"CID: {cid}")

        subtitles = get_subtitle_list(bvid, cid)

        result = ""

        if subtitles:
            print(f"找到 {len(subtitles)} 条字幕，开始下载...")

            all_text_parts = []
            for i, sub in enumerate(subtitles):
                lang = sub.get("lan_doc", sub.get("lan", f"字幕{i+1}"))
                print(f"  下载字幕: {lang}")

                if "subtitle_url" not in sub:
                    print(f"    跳过: 未找到字幕URL")
                    continue

                text = fetch_subtitle_text(sub["subtitle_url"])
                if text:
                    all_text_parts.append(f"=== {lang} ===\n{text}")
                else:
                    print(f"    跳过: 字幕内容为空")

            if all_text_parts:
                result = "\n\n".join(all_text_parts)

        if not result:
            if not subtitles:
                print("该视频没有字幕。")
            else:
                print("所有字幕内容为空。")

            if args.whisper:
                # 检查依赖
                if not check_whisper():
                    print("错误: 未安装 whisper，请运行: pip install openai-whisper")
                    sys.exit(1)

                if not check_ffmpeg():
                    print("错误: 未找到 ffmpeg，请先安装 ffmpeg")
                    print("Windows: winget install ffmpeg")
                    print("macOS: brew install ffmpeg")
                    print("Linux: sudo apt install ffmpeg")
                    sys.exit(1)

                print("正在使用 Whisper 语音识别...")

                # 创建临时目录
                with tempfile.TemporaryDirectory() as tmpdir:
                    # 获取音频URL
                    audio_url = get_audio_url(bvid, cid)
                    print(f"正在下载音频...")

                    # 下载音频
                    audio_path = os.path.join(tmpdir, "audio.m4a")
                    download_audio(audio_url, audio_path)

                    # 转换为WAV
                    wav_path = os.path.join(tmpdir, "audio.wav")
                    print(f"正在转换音频格式...")
                    convert_to_wav(audio_path, wav_path)

                    # 语音识别
                    result = transcribe_with_whisper(wav_path, args.model)

                    # 保留音频文件
                    if args.keep_audio:
                        audio_filename = sanitize_filename(title) + ".m4a"
                        audio_output = os.path.join(args.output, audio_filename)
                        import shutil
                        shutil.copy2(audio_path, audio_output)
                        print(f"音频已保存到: {audio_output}")
            else:
                print("提示: 使用 -w 参数启用 Whisper 语音识别")
                sys.exit(0)

        if result:
            filename = sanitize_filename(title) + ".txt"
            filepath = os.path.join(args.output, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(result)

            print(f"文本已保存到: {filepath}")
        else:
            print("未能获取任何文本内容")
            sys.exit(1)

    except ValueError as e:
        print(f"参数错误: {e}")
        sys.exit(1)
    except RuntimeError as e:
        print(f"运行错误: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n用户取消操作")
        sys.exit(0)
    except Exception as e:
        print(f"未知错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
