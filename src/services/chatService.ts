import { portfolioData } from '../data/portfolio';

export interface ChatResponse {
  text: string;
  source: 'local' | 'api';
  matchedCategory?: string;
  confidence?: number;
}

/**
 * Knowledge Engine strictly populated from Sriram R's verified resume data.
 * Zero hallucinations or invented data.
 */
class PortfolioKnowledgeBase {
  private normalize(text: string): string {
    return text.toLowerCase().trim().replace(/[^\w\s]/gi, ' ');
  }

  public getAnswer(userQuery: string): string {
    const q = ` ${this.normalize(userQuery)} `;

    // First check for known unverified / out-of-scope topics
    const outOfScopeKeywords = [
      'nasa',
      'quantum',
      'doctor',
      'phd',
      'master',
      'salary',
      'age',
      'marital',
      'religion',
      'driver',
      'pilot',
      'aws',
      'azure',
      'docker',
      'kubernetes',
      'blockchain',
      'crypto',
      'flutter',
      'swift',
      'ios',
      'android',
      'java',
      'rust',
      'golang',
    ];

    for (const word of outOfScopeKeywords) {
      if (q.includes(` ${word} `)) {
        return "I don't have that information in Sriram's portfolio yet.";
      }
    }

    // 1. Identity & Overview ("Who is Sriram?", "About", "Introduce yourself", "Who are you")
    if (
      q.includes(' who is ') ||
      q.includes(' about sriram ') ||
      q.includes(' introduce ') ||
      q.includes(' summary ') ||
      q.includes(' bio ') ||
      q.includes(' tell me about yourself ') ||
      q.includes(' overview ') ||
      q.includes(' background ') ||
      q.includes(' profile ')
    ) {
      return `Sriram R is a dynamic data science professional with hands-on experience in Python development and data analysis. He has experience with data visualization, SQL databases, Excel management, teamwork, communication and project-related activities. He is currently pursuing his B.E. in Computer Science Engineering (GPA: 7.8) at Paavai Engineering College.`;
    }

    // 2. GPA, Marks, College & Education
    if (
      q.includes(' gpa ') ||
      q.includes(' cgpa ') ||
      q.includes(' marks ') ||
      q.includes(' percentage ') ||
      q.includes(' grade ') ||
      q.includes(' study ') ||
      q.includes(' studied ') ||
      q.includes(' education ') ||
      q.includes(' college ') ||
      q.includes(' school ') ||
      q.includes(' university ') ||
      q.includes(' paavai ') ||
      q.includes(' degree ')
    ) {
      return `Sriram's educational background:\n\n• B.E. Computer Science Engineering: Paavai Engineering College (Autonomous), Namakkal (Expected May 2026) — GPA: 7.8\n• Higher Secondary Certificate (HSC): Sree Ambaal's Matric Higher Secondary School, Perambalur (May 2022) — 82%\n• SSLC (Class X): Sree Ambaal's Matric Higher Secondary School, Perambalur (May 2020) — 80%`;
    }

    // 3. Programming Languages
    if (
      q.includes(' programming language ') ||
      q.includes(' programming languages ') ||
      q.includes(' languages ') ||
      q.includes(' coding language ') ||
      q.includes(' coding languages ') ||
      q.includes(' python ') ||
      q.includes(' c ') ||
      q.includes(' c++ ') ||
      q.includes(' cpp ')
    ) {
      return `Sriram knows the following programming languages:\n• Python (Core focus & data workflows)\n• C\n• C++`;
    }

    // 4. Full Skills / Data / Database skills
    if (
      q.includes(' skill ') ||
      q.includes(' skills ') ||
      q.includes(' tech stack ') ||
      q.includes(' technologies ') ||
      q.includes(' tools ') ||
      q.includes(' sql ') ||
      q.includes(' database ') ||
      q.includes(' databases ') ||
      q.includes(' excel ') ||
      q.includes(' visualization ') ||
      q.includes(' analysis ')
    ) {
      return `Here are Sriram's verified skills:\n\n• Programming: Python, C, C++\n• Data & Databases: Data Analysis, Data Visualization, SQL Databases, MS Excel\n• Professional: Teamwork, Workplace Communication, Time Management`;
    }

    // 5. Experience & Internships
    if (
      q.includes(' experience ') ||
      q.includes(' internship ') ||
      q.includes(' internships ') ||
      q.includes(' work ') ||
      q.includes(' company ') ||
      q.includes(' companies ') ||
      q.includes(' corizo ') ||
      q.includes(' live stream ') ||
      q.includes(' aicte ') ||
      q.includes(' gdsc ')
    ) {
      return `Sriram's experience & internships include:\n\n1. Participant — GDSC Namakkal (Sep 2025 – Nov 2025): Python programming in Google Colaboratory, social impact activities, C/C++, and MS Excel data management.\n2. Data Science Intern — Corizo Edu Tech (Apr 2025 – Jun 2025)\n3. Data Science Intern — Live Stream Technologies (Jan 2025 – Feb 2025)\n4. AI & ML Intern — AICTE – Edu Skills (Apr 2024 – Jun 2024)`;
    }

    // 6. Projects
    if (
      q.includes(' project ') ||
      q.includes(' projects ') ||
      q.includes(' portfolio work ') ||
      q.includes(' apps ') ||
      q.includes(' built ')
    ) {
      return `Sriram's portfolio features 9 production-grade data science & engineering projects:\n\n` +
        `• Featured 1: Personal Finance & Expense Intelligence Dashboard (Python, Pandas, Plotly, Streamlit)\n` +
        `• Featured 2: Retail Sales Analytics with SQL (SQL, Python, Pandas, Plotly)\n` +
        `• Featured 3: Customer Churn Prediction (Python, Pandas, NumPy, Scikit-learn, Matplotlib)\n` +
        `• 4. E-Commerce Sales Analytics (Python, Pandas, SQL, Plotly, Streamlit)\n` +
        `• 5. Data Cleaning and Quality Pipeline (Python, Pandas, SQL, pytest)\n` +
        `• 6. Python API Data Pipeline (Python, REST APIs, Pandas, SQL, logging, pytest)\n` +
        `• 7. Business Performance Reporting Automation (Python, Pandas, SQL, CSV/Excel)\n` +
        `• 8. Student Academic Performance Analytics (Python, Pandas, NumPy, Matplotlib)\n` +
        `• 9. News Sentiment & Editorial Intelligence Studio (Python, Scikit-learn, Plotly, Streamlit)\n\n` +
        `All projects include working source code, synthetic datasets, and automated unit tests.`;
    }

    // 7. Training & GDSC
    if (
      q.includes(' training ') ||
      q.includes(' course ') ||
      q.includes(' workshop ') ||
      q.includes(' colab ') ||
      q.includes(' colaboratory ')
    ) {
      return `Sriram participated in the GDSC (Google Developer Student Club) training program focusing on Python programming using Google Colaboratory with a social-impact objective.`;
    }

    // 8. Extracurricular Activities
    if (
      q.includes(' extracurricular ') ||
      q.includes(' activity ') ||
      q.includes(' activities ') ||
      q.includes(' volunteering ') ||
      q.includes(' nss ') ||
      q.includes(' yi ') ||
      q.includes(' basketball ') ||
      q.includes(' sports ') ||
      q.includes(' placement ')
    ) {
      return `Sriram's extracurricular activities include:\n• NSS Volunteering (Social Leadership)\n• YI Volunteering (Youth Initiatives)\n• Placement Coordinator (Student Placement Drives)\n• Basketball Player`;
    }

    // 9. Areas of Interest
    if (
      q.includes(' interest ') ||
      q.includes(' interests ') ||
      q.includes(' passion ') ||
      q.includes(' passions ') ||
      q.includes(' entrepreneurship ') ||
      q.includes(' networking ')
    ) {
      return `Sriram's primary areas of interest are:\n• Networking Building\n• Entrepreneurship`;
    }

    // 10. Contact & Social Profiles
    if (
      q.includes(' contact ') ||
      q.includes(' email ') ||
      q.includes(' phone ') ||
      q.includes(' mobile ') ||
      q.includes(' number ') ||
      q.includes(' reach ') ||
      q.includes(' location ') ||
      q.includes(' where does he live ') ||
      q.includes(' address ') ||
      q.includes(' bangalore ') ||
      q.includes(' karnataka ')
    ) {
      return `You can contact Sriram R at:\n• Email: ${portfolioData.personal.email}\n• Phone: ${portfolioData.personal.phone}\n• Location: ${portfolioData.personal.location}`;
    }

    if (
      q.includes(' github ') ||
      q.includes(' linkedin ') ||
      q.includes(' leetcode ') ||
      q.includes(' social ') ||
      q.includes(' resume ') ||
      q.includes(' cv ')
    ) {
      return `Sriram's social & professional links:\n• GitHub: https://github.com/sriramriya (Username: sriramriya)\n• LinkedIn: https://www.linkedin.com/in/sriramraja22?utm_source=share_via&utm_content=profile&utm_medium=member_android (Username: sriramraja22)\n• LeetCode: https://leetcode.com/u/sriram_22 (Username: sriram_22)\n• Resume: Available via the "Download Resume" button on this website.`;
    }

    // Strict refusal when question is outside provided resume/portfolio
    return "I don't have that information in Sriram's portfolio yet.";
  }
}

const localKnowledgeBase = new PortfolioKnowledgeBase();

/**
 * Chat service abstraction.
 * Allows switching between offline deterministic knowledge matching and secure backend LLM API proxy.
 */
export async function sendChatMessage(message: string): Promise<ChatResponse> {
  const apiEndpoint = typeof import.meta !== 'undefined' && import.meta.env ? import.meta.env.VITE_AI_API_ENDPOINT : undefined;
  const apiKey = typeof import.meta !== 'undefined' && import.meta.env ? import.meta.env.VITE_AI_API_KEY : undefined;

  // If a secure API endpoint is provided in env, we can query it
  if (apiEndpoint && apiKey) {
    try {
      const response = await fetch(apiEndpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${apiKey}`,
        },
        body: JSON.stringify({
          messages: [
            {
              role: 'system',
              content: `You are Sriram AI, the official assistant for Sriram R's portfolio. You answer questions strictly based on Sriram's verified data: ${JSON.stringify(
                portfolioData
              )}. NEVER invent any experience, companies, projects, or certifications. If unknown, reply: "I don't have that information in Sriram's portfolio yet."`,
            },
            {
              role: 'user',
              content: message,
            },
          ],
        }),
      });

      if (response.ok) {
        const data = await response.json();
        const replyText =
          data.choices?.[0]?.message?.content ||
          data.reply ||
          data.message ||
          localKnowledgeBase.getAnswer(message);
        return {
          text: replyText,
          source: 'api',
        };
      }
    } catch (error) {
      console.warn('AI API failed, falling back to verified local knowledge base:', error);
    }
  }

  // Fallback to local verified knowledge base (always available, instant, 0 hallucinations)
  await new Promise((resolve) => setTimeout(resolve, 200));
  const answer = localKnowledgeBase.getAnswer(message);

  return {
    text: answer,
    source: 'local',
  };
}
