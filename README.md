# Sriram R — Personal Portfolio & AI Showcase

> **Data Science & Python Professional**  
> *Data Analysis • Python Development • SQL Databases • Machine Learning*

A modern, responsive personal portfolio website for **Sriram R**, built with React, TypeScript, Vite, Tailwind CSS, Framer Motion, and a zero-hallucination local AI Chatbot engine with pluggable LLM architecture.

---

## 🌟 Key Features

- **Futuristic Data Science Aesthetic**: Charcoal/dark-950 base, subtle glassmorphism, interactive HTML5 data nodes canvas, gradient text accents, and soft glowing borders.
- **Single Source of Truth**: All information is strictly verified against Sriram R's resume and centralized in [`src/data/portfolio.ts`](file:///c:/protofilo/src/data/portfolio.ts).
- **Interactive Sriram AI Chatbot**:
  - Floating bottom-right assistant with expand/collapse animations.
  - Suggested questions chips (*"Who is Sriram?"*, *"What are Sriram's skills?"*, *"Tell me about his experience."*, *"What is his GPA?"*, etc.).
  - 100% deterministic, zero-hallucination local engine out-of-the-box.
  - Pluggable API abstraction in [`src/services/chatService.ts`](file:///c:/protofilo/src/services/chatService.ts) for OpenAI/Gemini/Claude endpoints via environment variables.
  - Strictly refuses unknown/unverified questions with *"I don't have that information in Sriram's portfolio yet."*
- **Modular Project Showcase**:
  - Editable project cards with structured schema (Problem Statement, Solution, Key Features, Technologies, GitHub, Live Demo).
  - Built-in interactive detail modals with keyboard Escape and backdrop support.
- **Animated Vertical Timeline**:
  - Experience timeline featuring GDSC Namakkal participant highlights and Corizo, Live Stream Technologies, and AICTE Edu Skills internships.
- **Academic Qualifications**:
  - Paavai Engineering College BE CSE (GPA 7.8, May 2026), HSC (82%), and SSLC (80%).
- **Training, Activities & Interests**:
  - GDSC Training in Python & Google Colab.
  - NSS Volunteering, YI Volunteering, Placement Coordinator, Basketball Player.
  - Networking Building & Entrepreneurship.
- **Interactive Contact Hub**:
  - One-click copy for email (`sriram.riya.r@gmail.com`) and phone (`+91-8608850397`).
  - Contact form with client-side validation, quick-fill templates, and celebratory feedback.
- **Downloadable Resume**:
  - Pre-packaged clean PDF asset at [`public/resume.pdf`](file:///c:/protofilo/public/resume.pdf).
- **Profile Image System**:
  - Reads [`public/profile.jpg`](file:///c:/protofilo/public/profile.jpg) with graceful fallback to a tech monogram avatar if not yet uploaded.

---

## 🚀 Getting Started

### 1. Install Dependencies
```bash
npm install
```

### 2. Run Development Server
```bash
npx vite --host 127.0.0.1 --port 5173
```
Open [http://localhost:5173](http://localhost:5173) in your browser.

### 3. Run Automated Verification Suite
```bash
npx tsx scripts/verifyPortfolio.ts
```

### 4. Build for Production
```bash
npm run build
```

---

## 🛠️ How to Customize

### How to Update Portfolio Content
Edit [`src/data/portfolio.ts`](file:///c:/protofilo/src/data/portfolio.ts) to update personal bio, skills, education, experience, or add real project links and descriptions.

### How to Replace Profile Photo
Place your photo at:
```
public/profile.jpg
```
The website and chatbot will automatically pick up your photo.

### How to Replace Resume PDF
Place your updated resume file at:
```
public/resume.pdf
```

### How to Connect an External AI API
Create a `.env` file in the project root:
```env
VITE_AI_API_ENDPOINT=https://your-api-endpoint/v1/chat/completions
VITE_AI_API_KEY=your_secret_key_here
```
The chatbot in [`src/services/chatService.ts`](file:///c:/protofilo/src/services/chatService.ts) will automatically route queries through the API with the local knowledge base as a fallback.

---

## 📂 Project Architecture

```
c:\protofilo\
├── public/
│   ├── favicon.svg          # Portfolio glowing monogram favicon
│   ├── og-image.svg         # Open Graph social preview banner
│   ├── resume.pdf           # Downloadable PDF resume
│   └── profile.jpg          # Profile photo location (with fallback)
├── src/
│   ├── components/
│   │   ├── about/           # About section & 4 highlight cards
│   │   ├── activities/      # NSS, YI, Placement, Basketball cards
│   │   ├── chatbot/         # Sriram AI widget, message list, suggested queries
│   │   ├── contact/         # Contact info cards, copy buttons, contact form
│   │   ├── education/       # Education timeline cards (BE CSE, HSC, SSLC)
│   │   ├── experience/      # Animated vertical experience timeline
│   │   ├── hero/            # Hero headline, TechCanvas, ProfileImage, CTAs
│   │   ├── interests/       # Networking & Entrepreneurship cards
│   │   ├── layout/          # Sticky Navbar, Footer, Container
│   │   ├── projects/        # Featured projects & ProjectModal dialog
│   │   ├── skills/          # Interactive skill categories & chips
│   │   ├── training/        # GDSC Google Colaboratory training
│   │   └── ui/              # SectionHeading, GlowingBadge, Card, Icons
│   ├── data/
│   │   └── portfolio.ts     # Centralized single source of truth
│   ├── services/
│   │   └── chatService.ts   # Chatbot engine & API abstraction
│   ├── types/
│   │   └── index.ts         # TypeScript interfaces
│   ├── App.tsx              # Main layout assembler
│   ├── index.css            # Global CSS, glassmorphism, glowing utilities
│   └── main.tsx             # React DOM entry point
└── tailwind.config.js       # Dark tech tokens & animations
```

---

© 2026 Sriram R. All rights reserved.
