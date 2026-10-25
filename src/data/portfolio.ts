import { PortfolioData } from '../types';

export const portfolioData: PortfolioData = {
  personal: {
    name: 'Sriram R',
    role: 'Computer Science Engineering Graduate | Python | SQL | Data Analytics',
    tagline: 'Computer Science Engineering Graduate • Python Developer • SQL & Data Analytics',
    bioSummary:
      'I’m a Computer Science Engineering graduate with internship experience in data science and AI/ML. I enjoy solving problems using Python, working with data, and building practical technology projects. I’m looking for opportunities to contribute, learn, and grow as an IT professional.',
    aboutText:
      'I am a Computer Science Engineering graduate with practical internship experience in data science and AI/ML. My technical focus centers on Python development, relational SQL databases, Excel data management, and exploratory data analytics. I enjoy building practical, reproducible technology projects and continuously growing my software capabilities as an entry-level IT professional.',
    location: 'Bangalore, Karnataka, India',
    email: 'sriram.riya.r@gmail.com',
    phone: '+91-8608850397',
    resumeUrl: '/resume.pdf',
    profileImageUrl: '/images/sriram-formal.jpg',
    gpa: '7.8 GPA (BE CSE)',
    status: 'Available for Opportunities',
  },

  socials: [
    {
      platform: 'github',
      label: 'GitHub',
      username: 'sriram2324',
      url: 'https://github.com/sriram2324',
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
      title: 'Python Development',
      description: 'Hands-on programming, automation, and algorithmic problem-solving with Python.',
      icon: 'Code2',
      gradient: 'from-[#D4A373]/20 via-[#D4A373]/5 to-transparent',
      borderColor: 'border-[#D4A373]/30 group-hover:border-[#D4A373]',
    },
    {
      id: 'sql',
      title: 'SQL Databases',
      description: 'Relational data modeling, SQLite querying, multi-table joins, and aggregations.',
      icon: 'Database',
      gradient: 'from-[#6FFFE9]/20 via-[#6FFFE9]/5 to-transparent',
      borderColor: 'border-[#6FFFE9]/30 group-hover:border-[#6FFFE9]',
    },
    {
      id: 'data',
      title: 'Analytics & Excel',
      description: 'Exploratory data analysis, statistical metrics, and spreadsheet management.',
      icon: 'BarChart3',
      gradient: 'from-[#FAEDCD]/20 via-[#FAEDCD]/5 to-transparent',
      borderColor: 'border-[#FAEDCD]/30 group-hover:border-[#FAEDCD]',
    },
    {
      id: 'projects',
      title: 'Practical Projects',
      description: 'End-to-end data pipelines, ML workflows, and interactive dashboard applications.',
      icon: 'Layers',
      gradient: 'from-[#E4BD96]/20 via-[#E4BD96]/5 to-transparent',
      borderColor: 'border-[#E4BD96]/30 group-hover:border-[#E4BD96]',
    },
  ],

  skillCategories: [
    {
      id: 'programming',
      title: 'Programming',
      subtitle: 'Core programming logic & scripting',
      icon: 'Terminal',
      color: '#D4A373',
      skills: [
        { name: 'Python', highlight: true },
        { name: 'C' },
        { name: 'C++' },
      ],
    },
    {
      id: 'databases',
      title: 'Databases',
      subtitle: 'Relational database schemas & data querying',
      icon: 'Database',
      color: '#6FFFE9',
      skills: [
        { name: 'SQL', highlight: true },
        { name: 'SQLite', highlight: true },
        { name: 'Relational Queries' },
      ],
    },
    {
      id: 'productivity-analytics',
      title: 'Productivity & Analytics',
      subtitle: 'Spreadsheet management & data insight discovery',
      icon: 'BarChart3',
      color: '#FAEDCD',
      skills: [
        { name: 'Microsoft Excel', highlight: true },
        { name: 'Data Analysis', highlight: true },
        { name: 'Data Visualization', highlight: true },
      ],
    },
    {
      id: 'additional-tools',
      title: 'Additional Tools & Libraries',
      subtitle: 'Verified libraries & frameworks applied across portfolio projects',
      icon: 'Layers',
      color: '#E4BD96',
      skills: [
        { name: 'Pandas', highlight: true },
        { name: 'NumPy' },
        { name: 'Scikit-learn', highlight: true },
        { name: 'Matplotlib & Seaborn' },
        { name: 'Plotly' },
        { name: 'Streamlit' },
        { name: 'pytest' },
        { name: 'REST APIs' },
        { name: 'Git & GitHub' },
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
      id: 'personal-finance-dashboard',
      title: 'Personal Finance & Expense Intelligence Dashboard',
      subtitle: 'Expense Analysis & Financial KPIs',
      category: 'Financial Analytics',
      featured: true,
      description:
        'An end-to-end personal finance analytics and budgeting application providing automated transaction validation, category budget tracking, spending velocity trends, core financial KPIs, and downloadable reports.',
      problemStatement:
        'Managing personal cash flows across variable expenses makes it difficult to maintain category budgets, track spending velocity, and identify spending leaks without structured analytics.',
      solution:
        'A modular Python pipeline that cleans and audits raw financial records, tracks category budget variances, computes key financial KPIs, and renders interactive spending visualizations in Streamlit.',
      technologies: ['Python', 'Pandas', 'Plotly', 'Streamlit', 'pytest'],
      keyFeatures: [
        'Automated expense analysis & category classification',
        'Monthly budget tracking with variance alerts',
        'Historical spending trends & net savings velocity',
        'Interactive financial KPIs & metrics overview',
        'Downloadable executive expense summary reports',
      ],
      status: 'completed',
      github: 'https://github.com/sriram2324/Sriram-s-Portfolio/tree/main/projects/personal-finance-dashboard',
      details:
        'Full implementation delivered in projects/personal-finance-dashboard with modular analytics engine, synthetic transaction dataset, interactive Streamlit app, and automated pytest test suite.',
    },
    {
      id: 'retail-sales-analytics',
      title: 'Retail Sales Analytics with SQL',
      subtitle: 'Commercial Sales Intelligence & SQL Aggregation',
      category: 'SQL & Business Intelligence',
      featured: true,
      description:
        'A business intelligence and relational analytics system evaluating retail sales volume, revenue growth trends, product performance hierarchies, customer purchasing patterns, and commercial business insights.',
      problemStatement:
        'Retail managers need consolidated multi-table visibility into order transactions to understand revenue fluctuations, product category velocity, and repeat customer purchasing behavior.',
      solution:
        'Relational SQL data extraction and aggregation queries coupled with Python analytics to evaluate revenue trends, basket sizes, and product performance across normalized tables.',
      technologies: ['SQL', 'Python', 'Pandas', 'Plotly', 'pytest'],
      keyFeatures: [
        'Relational SQL schema across 4 normalized database tables',
        'Complex SQL queries with window functions & date aggregations',
        'Retail revenue trends & seasonal sales performance',
        'Product catalog evaluation & category contribution ranking',
        'Customer purchasing patterns & basket size metrics',
      ],
      status: 'completed',
      github: 'https://github.com/sriram2324/Sriram-s-Portfolio/tree/main/projects/retail-sales-analytics',
      details:
        'Full implementation delivered in projects/retail-sales-analytics with SQLite relational schema, seed generator, SQL analytics engine, and automated pytest test suite.',
    },
    {
      id: 'customer-churn-prediction',
      title: 'Customer Churn Prediction',
      subtitle: 'Predictive Modeling & Churn Risk Classification',
      category: 'Machine Learning',
      featured: true,
      description:
        'A reproducible scikit-learn machine learning workflow featuring exploratory data analysis, feature preprocessing and encoding without data leakage, baseline and classification models, and ROC-AUC evaluation.',
      problemStatement:
        'Subscription businesses experience customer churn and revenue attrition when warning indicators and behavioral signals go undetected prior to account cancellation.',
      solution:
        'A scikit-learn predictive modeling pipeline with ColumnTransformer preprocessing, regularized Logistic Regression baseline, Random Forest classification, and Gini feature importance extraction.',
      technologies: ['Python', 'Pandas', 'NumPy', 'Scikit-learn', 'Matplotlib', 'pytest'],
      keyFeatures: [
        'Exploratory data analysis (EDA) of customer behavioral drivers',
        'Robust feature preprocessing & scaling with zero data leakage',
        'Supervised classification models (Logistic Regression, Random Forest)',
        'Comprehensive model evaluation (ROC-AUC, Precision, Recall, F1)',
        'Explainable feature importance ranking',
      ],
      status: 'completed',
      github: 'https://github.com/sriram2324/Sriram-s-Portfolio/tree/main/projects/customer-churn-prediction',
      details:
        'Full implementation delivered in projects/customer-churn-prediction with synthetic dataset, zero-data-leakage pipeline, model benchmarking, and automated pytest test suite.',
    },
    {
      id: 'ecommerce-sales-analytics',
      title: 'E-Commerce Sales Analytics',
      subtitle: 'Revenue Trends & Customer RFM',
      category: 'Commercial Analytics',
      featured: false,
      description:
        'Multi-channel e-commerce analytics platform evaluating gross revenue trends, seasonal order volume, category performance rankings, and Recency-Frequency-Monetary (RFM) customer segmentation.',
      problemStatement:
        'Online merchants need granular visibility into customer transaction frequencies and product category contributions to retain high-value customer cohorts and optimize seasonal inventory.',
      solution:
        'A modular Python and Streamlit analytics engine computing MoM revenue growth trajectories, category revenue share, and behavioral RFM segmentation.',
      technologies: ['Python', 'Pandas', 'SQL', 'Plotly', 'Streamlit', 'pytest'],
      keyFeatures: [
        'Sales and revenue trend analysis with MoM growth metrics',
        'Monthly and seasonal order distribution modeling',
        'Product and category performance contribution ranking',
        'RFM customer segmentation (Champions, Loyal, Recent, At-Risk)',
        'Interactive Streamlit KPI dashboard & downloadable CSV reports',
      ],
      status: 'completed',
      github: 'https://github.com/sriram2324/Sriram-s-Portfolio/tree/main/projects/ecommerce-sales-analytics',
      details:
        'Full implementation delivered in projects/ecommerce-sales-analytics with order dataset, RFM segmentation engine, Streamlit dashboard, and automated pytest test suite.',
    },
    {
      id: 'data-quality-pipeline',
      title: 'Data Cleaning and Quality Pipeline',
      subtitle: 'Schema Validation & Audit Engine',
      category: 'Data Engineering',
      featured: false,
      description:
        'An automated, reusable data cleaning and validation pipeline providing missing-value imputation, duplicate detection, schema validation, statistical outlier capping (IQR), and audit reporting.',
      problemStatement:
        'Dirty tabular data with corrupt types, duplicate entries, invalid negative attributes, and extreme outliers undermine downstream business intelligence and machine learning models.',
      solution:
        'A reusable data validation pipeline that audits schema compliance, imputes missing values using robust statistical defaults, removes duplicate keys, and caps outliers using 1.5x IQR.',
      technologies: ['Python', 'Pandas', 'SQL', 'pytest'],
      keyFeatures: [
        'Deterministic missing-value handling and imputation',
        'Duplicate record detection on natural and composite keys',
        'Data type validation and domain consistency checks',
        'Statistical outlier detection and IQR boundary capping',
        'Automated data quality scoring and markdown audit reports',
      ],
      status: 'completed',
      github: 'https://github.com/sriram2324/Sriram-s-Portfolio/tree/main/projects/data-quality-pipeline',
      details:
        'Full implementation delivered in projects/data-quality-pipeline with dirty sample dataset, modular pipeline classes, quality scoring engine, and automated pytest test suite.',
    },
    {
      id: 'python-api-pipeline',
      title: 'Python API Data Pipeline',
      subtitle: 'REST Ingestion & Fault-Tolerant Storage',
      category: 'Data Engineering',
      featured: false,
      description:
        'A fault-tolerant REST API ingestion pipeline with automated pagination, exponential backoff retries, schema normalization, and relational SQLite storage with structured logging.',
      problemStatement:
        'External REST APIs are prone to transient network timeouts, rate limit throttles (HTTP 429), and malformed payloads requiring resilient ingestion pipelines.',
      solution:
        'A resilient Python pipeline connecting to open public REST endpoints with session pooling, backoff retry cycles, schema validation, and SQLite upsert mechanics.',
      technologies: ['Python', 'REST APIs', 'Pandas', 'SQL', 'logging', 'pytest'],
      keyFeatures: [
        'Public REST API integration with real open endpoints',
        'Response schema validation and structured normalization',
        'Resilient pagination and exponential backoff retry handler',
        'Relational SQLite table persistence with upsert mechanics',
        'Comprehensive Python logging and automated pytest test suite',
      ],
      status: 'completed',
      github: 'https://github.com/sriram2324/Sriram-s-Portfolio/tree/main/projects/python-api-pipeline',
      details:
        'Full implementation delivered in projects/python-api-pipeline with open endpoint integration, SQLite persistence, unit tests with mocked responses, and structured logging.',
    },
    {
      id: 'business-report-automation',
      title: 'Business Performance Reporting Automation',
      subtitle: 'KPI Calculation & Executive Reports',
      category: 'Business Intelligence',
      featured: false,
      description:
        'An automated enterprise business intelligence pipeline computing key financial KPIs, revenue-versus-quota target attainments, operating margins, and generating repeatable executive briefs.',
      problemStatement:
        'Manual compilation of quarterly commercial performance reports from fragmented spreadsheets is slow, error-prone, and delays management decisions.',
      solution:
        'A Python reporting automation pipeline that validates multi-department records, computes revenue attainment and operating margins, and generates formatted executive markdown and CSV briefs.',
      technologies: ['Python', 'Pandas', 'SQL', 'CSV/Excel', 'Automated Reporting', 'pytest'],
      keyFeatures: [
        'Multi-department commercial dataset ingestion',
        'Key financial KPIs (Revenue, Cost, Gross Profit, Operating Margin %)',
        'Quota attainment tracking and revenue-per-employee metrics',
        'Department performance comparison hierarchies',
        'Repeatable executive summary report generation in Markdown & CSV',
      ],
      status: 'completed',
      github: 'https://github.com/sriram2324/Sriram-s-Portfolio/tree/main/projects/business-report-automation',
      details:
        'Full implementation delivered in projects/business-report-automation with quarterly performance data, KPI engine, executive report generator, and automated pytest test suite.',
    },
    {
      id: 'student-performance-analytics',
      title: 'Student Academic Performance Analytics',
      subtitle: 'Exploratory Analysis & Statistical Correlations',
      category: 'Data Analytics',
      featured: false,
      description:
        'An end-to-end data science pipeline analyzing student academic marks across subjects to discover the statistical relationship between daily study habits, attendance, and exam scores.',
      problemStatement:
        'Educational institutions need data-driven evidence to quantify how attendance and daily study hours dictate subject-level exam performance.',
      solution:
        'A modular Python analytics pipeline that audits student records, computes Pearson correlation metrics, renders high-resolution charts, and compiles findings reports.',
      technologies: ['Python', 'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'pytest'],
      keyFeatures: [
        'Non-destructive dataset cleaning and validation rules',
        'Descriptive statistics, benchmarks, and pass/fail distributions',
        'Pearson correlation between attendance, study hours, and exam marks',
        '5 high-resolution publication-grade Matplotlib charts',
        'Automated unit and pipeline tests via pytest',
      ],
      status: 'completed',
      github: 'https://github.com/sriram2324/Sriram-s-Portfolio/tree/main/project%201',
      details:
        'Full implementation delivered in project 1 folder with untouched raw dataset, cleaned dataset, 5 high-resolution charts, findings report, and automated pytest tests.',
    },
    {
      id: 'news-sentiment-intelligence',
      title: 'News Sentiment & Editorial Intelligence Studio',
      subtitle: 'NLP Sentiment Telemetry & Feature Attribution',
      category: 'NLP & Machine Learning',
      featured: false,
      description:
        'An editorial-grade NLP intelligence platform that extracts linguistic sentiment signals, directional polarity, and mathematical feature attributions from news dispatches.',
      problemStatement:
        'Financial market announcements and media headlines contain nuanced sentiment valence that requires real-time quantitative feature extraction without model hallucination.',
      solution:
        'A production-grade NLP telemetry studio using sublinear TF-IDF feature representation, regularized Logistic Regression, zero data leakage, and interactive Plotly confusion matrices.',
      technologies: ['Python', 'Scikit-learn', 'Plotly', 'Streamlit', 'Pandas'],
      keyFeatures: [
        'Real-time headline classification (Positive, Negative, Neutral)',
        'Directional polarity spectrum meter (-1.000 to +1.000)',
        'Feature attribution reel extracting influential n-grams',
        'Batch analytics with CSV ingestion and confusion matrix telemetry',
        'Curated 435-row benchmark dataset with zero data leakage',
      ],
      status: 'completed',
      github: 'https://github.com/sriram2324/Sriram-s-Portfolio/tree/main/PROJECT%202',
      details:
        'Full implementation delivered in PROJECT 2 folder with curated benchmark dataset CONS-435, held-out evaluation telemetry (77.01% accuracy), interactive Streamlit studio, and automated test sandbox.',
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
