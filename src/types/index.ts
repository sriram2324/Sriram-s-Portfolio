export interface PersonalInfo {
  name: string;
  role: string;
  tagline: string;
  bioSummary: string;
  aboutText: string;
  location: string;
  email: string;
  phone: string;
  resumeUrl: string;
  profileImageUrl: string;
  gpa: string;
  status: string;
}

export interface SocialLink {
  platform: 'github' | 'linkedin' | 'leetcode' | 'email';
  label: string;
  username: string;
  url: string;
  iconName: string;
}

export interface HighlightCardItem {
  id: string;
  title: string;
  description: string;
  icon: string;
  gradient: string;
  borderColor: string;
}

export interface SkillItem {
  name: string;
  icon?: string;
  highlight?: boolean;
}

export interface SkillCategory {
  id: string;
  title: string;
  subtitle: string;
  icon: string;
  skills: SkillItem[];
  color: string;
}

export interface ExperienceItem {
  id: string;
  role: string;
  organization: string;
  location?: string;
  period: string;
  startDate: string;
  endDate: string;
  type: 'internship' | 'participant' | 'extracurricular';
  highlights?: string[];
  technologies?: string[];
  isCurrent?: boolean;
}

export interface ProjectItem {
  id: string;
  title: string;
  subtitle?: string;
  category?: string;
  description: string;
  problemStatement?: string;
  solution?: string;
  technologies: string[];
  keyFeatures?: string[];
  image?: string;
  github?: string;
  liveDemo?: string;
  details?: string;
  screenshots?: string[];
  status?: 'upcoming' | 'completed' | 'in-progress';
  featured?: boolean;
}

export interface EducationItem {
  id: string;
  degree: string;
  field?: string;
  institution: string;
  location: string;
  period: string;
  completionDate: string;
  gradeLabel: string;
  gradeValue: string;
  icon: string;
}

export interface TrainingItem {
  id: string;
  title: string;
  organization: string;
  description: string;
  keyPoints: string[];
  technologies: string[];
}

export interface ActivityItem {
  id: string;
  title: string;
  category: string;
  description?: string;
  icon: string;
  badgeColor: string;
}

export interface InterestItem {
  id: string;
  title: string;
  description: string;
  icon: string;
  gradient: string;
}

export interface PortfolioData {
  personal: PersonalInfo;
  socials: SocialLink[];
  aboutHighlights: HighlightCardItem[];
  skillCategories: SkillCategory[];
  experiences: ExperienceItem[];
  projects: ProjectItem[];
  education: EducationItem[];
  training: TrainingItem[];
  activities: ActivityItem[];
  interests: InterestItem[];
  suggestedQuestions: string[];
}

export interface ChatMessage {
  id: string;
  sender: 'user' | 'bot';
  text: string;
  timestamp: Date;
  suggestedActions?: { label: string; action: string }[];
}
