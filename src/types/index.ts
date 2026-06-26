export interface Paper {
  id: string
  title: string
  year: number
  arxivId: string
  category: 'foundation' | 'llm' | 'alignment' | 'multimodal'
  categoryName: string
  contentHtml: string
  filePath: string
}

export interface LearningItem {
  id: string
  text: string
  completed: boolean
}

export interface LearningStage {
  id: string
  name: string
  order: number
  items: LearningItem[]
}

export interface GlossaryTerm {
  term: string
  definition: string
}

export interface ExamQuestion {
  id: string
  question: string
  answer: string
  category: string
}

export interface AgentResource {
  id: string
  title: string
  type: 'framework' | 'pattern' | 'project'
  description: string
}

export interface Product {
  id: string
  title: string
  description: string
  tag?: string
  link?: string
}

export interface SearchItem {
  id: string
  title: string
  category: string
  type: 'paper' | 'knowledge' | 'agent' | 'product' | 'exam'
  text: string
  route: string
}
