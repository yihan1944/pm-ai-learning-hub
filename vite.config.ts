import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  base: process.env.CUSTOM_DOMAIN ? '/' : '/pm-ai-learning-hub/',
})
