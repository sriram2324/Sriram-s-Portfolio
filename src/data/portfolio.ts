import { PortfolioData } from '../types';

export const portfolioData: PortfolioData = {
  personal: {
    name: 'Sriram R',
    role: 'Data Science & Python Professional',
    tagline: 'Dynamic Data Science Professional • Python Developer • Analytics Specialist',
    bioSummary:
      'Dynamic data science professional with hands-on experience in Python development and data analysis, with skills in data visualization, SQL databases, Excel management, teamwork and communication.',
    aboutText:
      'Sriram R is a dynamic data science professional with hands-on experience in Python development and data analysis. He has experience with data visualization, SQL databases, Excel management, teamwork, communication and project-related activities.',
    location: 'Bangalore, Karnataka, India',
    email: 'sriram.riya.r@gmail.com',
    phone: '+91-8608850397',
    resumeUrl: '/resume.pdf',
    profileImageUrl: '/profile.jpg',
    gpa: '7.8 GPA (BE CSE)',
    status: 'Available for Opportunities',
  },

  socials: [
    {
      platform: 'github',
      label: 'GitHub',
      username: 'sriramriya',
      url: 'https://github.com/sriramriya',
      iconName: 'Github',
    },
    {
      platform: 'linkedin',
      label: 'LinkedIn',
      username: 'sriramraja22',
      url: 'https://www.linkedin.com/in/sriramraja22?utm_source=share_via&utm_content=profile&utm_medium=member_android',
      iconName: 'Linkedin',
    },
    {
      platform: 'leetcode',
      label: 'LeetCode',
      username: 'sriram_22',
      url: 'https://leetcode.com/u/sriram_22',
      iconName: 'Code2',
    },
  ],

  aboutHighlights: [
    {
      id: 'python',
      title: 'Python',
      description: 'Python development and programming experience.',
      icon: 'Code2',
      gradient: 'from-[#D4A373]/20 via-[#D4A373]/5 to-transparent',
      borderColor: 'border-[#D4A373]/30 group-hover:border-[#D4A373]',
    },
    {
      id: 'data',
      title: 'Data',
      description: 'Data analysis and visualization.',
      icon: 'BarChart3',
      gradient: 'from-[#6FFFE9]/20 via-[#6FFFE9]/5 to-transparent',
      borderColor: 'border-[#6FFFE9]/30 group-hover:border-[#6FFFE9]',
    },
    {
      id: 'sql',
      title: 'SQL',
      description: 'SQL database knowledge.',
      icon: 'Database',
      gradient: 'from-[#E4BD96]/20 via-[#E4BD96]/5 to-transparent',
      borderColor: 'border-[#E4BD96]/30 group-hover:border-[#E4BD96]',
    },
    {
      id: 'collaboration',
      title: 'Collaboration',
      description: 'Teamwork and workplace communication.',
      icon: 'Users2',
      gradient: 'from-[#38EFD3]/20 via-[#38EFD3]/5 to-transparent',
      borderColor: 'border-[#38EFD3]/30 group-hover:border-[#38EFD3]',
    },
  ],

  skillCategories: [
    {
      id: 'programming',
      title: 'Programming',
      subtitle: 'Core programming languages & development logic',
      icon: 'Terminal',
      color: '#D4A373',
      skills: [
        { name: 'Python', highlight: true },
        { name: 'C' },
        { name: 'C++' },
      ],
    },
    {
      id: 'data',
      title: 'Data & Databases',
      subtitle: 'Analytics, data visualization & database querying',
      icon: 'Database',
      color: '#6FFFE9',
      skills: [
        { name: 'Data Analysis', highlight: true },
        { name: 'Data Visualization', highlight: true },
        { name: 'SQL Databases', highlight: true },
        { name: 'MS Excel' },
      ],
    },
    {
      id: 'professional',
      title: 'Professional',
      subtitle: 'Workplace collaboration & project management skills',
      icon: 'Briefcase',
      color: '#E4BD96',
      skills: [
        { name: 'Teamwork', highlight: true },
        { name: 'Workplace Communication', highlight: true },
        { name: 'Time Management' },
      ],
    },
  ],

  experiences: [
    {
      id: 'gdsc-participant',
      role: 'Participant',
      organization: 'GDSC – Google Developer Student Club, Namakkal',
      location: 'Namakkal, Tamil Nadu',
      period: 'September 2025 – November 2025',
      startDate: 'Sep 2025',
      endDate: 'Nov 2025',
      type: 'participant',
      highlights: [
        'Participated in Python programming activities.',
        'Used Google Colaboratory for interactive workflows.',
        'Worked on activities focused on social impact.',
        'Used C and C++ for coding tasks.',
        'Managed and organized information using MS Excel.',
      ],
      technologies: ['Python', 'Google Colaboratory', 'C', 'C++', 'MS Excel'],
      isCurrent: false,
    },
    {
      id: 'corizo-intern',
      role: 'Data Science Intern',
      organization: 'Corizo – Edu Tech',
      period: 'April 2025 – June 2025',
      startDate: 'Apr 2025',
      endDate: 'Jun 2025',
      type: 'internship',
      technologies: ['Data Science', 'Python', 'Analytics'],
      isCurrent: false,
    },
    {
      id: 'live-stream-intern',
      role: 'Data Science Intern',
      organization: 'Live Stream Technologies',
      period: 'January 2025 – February 2025',
      startDate: 'Jan 2025',
      endDate: 'Feb 2025',
      type: 'internship',
      technologies: ['Data Science', 'Python', 'Data Analysis'],
      isCurrent: false,
    },
    {
      id: 'aicte-intern',
      role: 'Artificial Intelligence & Machine Learning Intern',
      organization: 'AICTE – Edu Skills',
      period: 'April 2024 – June 2024',
      startDate: 'Apr 2024',
      endDate: 'Jun 2024',
      type: 'internship',
      technologies: ['Artificial Intelligence', 'Machine Learning', 'Python'],
      isCurrent: false,
    },
  ],

  projects: [
    {
      id: 'data-science-project',
      title: 'Data Science Project',
      subtitle: 'Data Analytics & Insights',
      description: 'Project details will be added soon.',
      problemStatement:
        'Detailed problem statement and business objective will be documented once the project repository is published.',
      solution:
        'Comprehensive analytical solution incorporating data pipelines, statistical evaluation, and interactive visual insights.',
      technologies: ['Python', 'Data Analysis', 'SQL', 'Data Visualization'],
      keyFeatures: [
        'End-to-end data processing workflow',
        'Visual summary charts & reports',
        'Database integration & querying',
      ],
      status: 'upcoming',
      details:
        'This project slot is ready for integration. To update, add your title, repository link, live demo, and architecture notes in src/data/portfolio.ts.',
    },
    {
      id: 'python-project',
      title: 'Python Project',
      subtitle: 'Core Python Application',
      description: 'Project details will be added soon.',
      problemStatement:
        'Detailed problem statement and application requirements will be documented soon.',
      solution:
        'Robust Python implementation built with modular programming, error handling, and clean code patterns.',
      technologies: ['Python', 'C++', 'Data Structures', 'Automation'],
      keyFeatures: [
        'Modular architecture',
        'Efficient algorithm implementation',
        'Data extraction & file handling',
      ],
      status: 'upcoming',
      details:
        'This project slot is ready for integration. Update the GitHub and demo links in src/data/portfolio.ts.',
    },
    {
      id: 'ml-project',
      title: 'Machine Learning Project',
      subtitle: 'Predictive Modeling & Intelligence',
      description: 'Project details will be added soon.',
      problemStatement:
        'Machine learning problem formulation, dataset characteristics, and baseline metrics will be added soon.',
      solution:
        'Predictive model pipeline utilizing feature engineering, model training, validation, and performance metric tracking.',
      technologies: ['Machine Learning', 'Python', 'Data Visualization', 'Colab'],
      keyFeatures: [
        'Feature engineering & data preprocessing',
        'Predictive model evaluation',
        'Exploratory data analysis reporting',
      ],
      status: 'upcoming',
      details:
        'This project slot is ready for integration. Simply edit this project item in src/data/portfolio.ts to populate your project details.',
    },
  ],

  education: [
    {
      id: 'be-cse',
      degree: 'Bachelor of Engineering (B.E.)',
      field: 'Computer Science Engineering',
      institution: 'Paavai Engineering College (Autonomous)',
      location: 'Namakkal, Tamil Nadu',
      period: '2022 – 2026',
      completionDate: 'May 2026',
      gradeLabel: 'GPA',
      gradeValue: '7.8',
      icon: 'GraduationCap',
    },
    {
      id: 'hsc',
      degree: 'Higher Secondary Certificate (HSC)',
      field: 'Class XII',
      institution: "Sree Ambaal's Matric Higher Secondary School",
      location: 'Perambalur, Tamil Nadu',
      period: '2020 – 2022',
      completionDate: 'May 2022',
      gradeLabel: 'Percentage',
      gradeValue: '82%',
      icon: 'Award',
    },
    {
      id: 'sslc',
      degree: 'Secondary School Leaving Certificate (SSLC)',
      field: 'Class X',
      institution: "Sree Ambaal's Matric Higher Secondary School",
      location: 'Perambalur, Tamil Nadu',
      period: '2019 – 2020',
      completionDate: 'May 2020',
      gradeLabel: 'Percentage',
      gradeValue: '80%',
      icon: 'BookOpen',
    },
  ],

  training: [
    {
      id: 'gdsc-training',
      title: 'GDSC — Google Developer Student Club',
      organization: 'Google Developer Student Clubs',
      description:
        'Participated in the GDSC program involving Python programming using Google Colaboratory with a social-impact focus.',
      keyPoints: [
        'Python programming & practical coding challenges',
        'Hands-on interactive notebooks in Google Colaboratory',
        'Solutions centered on social impact & community development',
        'Data organization and management practices with MS Excel',
      ],
      technologies: ['Python', 'Google Colaboratory', 'Data Analysis', 'C / C++'],
    },
  ],

  activities: [
    {
      id: 'nss',
      title: 'NSS Volunteering',
      category: 'Social Leadership',
      description: 'Active community engagement and social development activities with the National Service Scheme.',
      icon: 'HeartHandshake',
      badgeColor: 'text-[#6FFFE9] bg-[#6FFFE9]/10 border-[#6FFFE9]/30',
    },
    {
      id: 'yi',
      title: 'YI Volunteering',
      category: 'Youth Empowerment',
      description: 'Participation in Young Indians (YI) initiatives fostering leadership and student development.',
      icon: 'Sparkles',
      badgeColor: 'text-[#D4A373] bg-[#D4A373]/10 border-[#D4A373]/30',
    },
    {
      id: 'placement-coord',
      title: 'Placement Coordinator',
      category: 'Student Leadership',
      description: 'Coordinating campus recruitment drives, student communications, and organizational logistics.',
      icon: 'UserCheck',
      badgeColor: 'text-[#E4BD96] bg-[#E4BD96]/10 border-[#E4BD96]/30',
    },
    {
      id: 'basketball',
      title: 'Basketball Player',
      category: 'Sports & Athletics',
      description: 'Competitive basketball player demonstrating agility, strategic thinking, and team coordination.',
      icon: 'Trophy',
      badgeColor: 'text-[#FAEDCD] bg-[#D4A373]/15 border-[#D4A373]/35',
    },
  ],

  interests: [
    {
      id: 'networking',
      title: 'Networking Building',
      description: 'Connecting with industry professionals, tech communities, and collaborative developer networks.',
      icon: 'Network',
      gradient: 'from-[#D4A373]/20 via-[#1C2541] to-transparent',
    },
    {
      id: 'entrepreneurship',
      title: 'Entrepreneurship',
      description: 'Exploring tech innovation, problem-solving business models, and scalable digital solutions.',
      icon: 'Lightbulb',
      gradient: 'from-[#6FFFE9]/20 via-[#1C2541] to-transparent',
    },
  ],

  suggestedQuestions: [
    'Who is Sriram?',
    "What are Sriram's skills?",
    'Tell me about his experience.',
    'What programming languages does he know?',
    'Where did he study?',
    'What is his GPA?',
    'What are his areas of interest?',
    'Where can I find his GitHub?',
  ],
};
