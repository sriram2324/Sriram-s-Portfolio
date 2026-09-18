import React, { useState } from 'react';
import { Navbar } from './components/layout/Navbar';
import { Footer } from './components/layout/Footer';
import { Hero } from './components/hero/Hero';
import { About } from './components/about/About';
import { Skills } from './components/skills/Skills';
import { Experience } from './components/experience/Experience';
import { Projects } from './components/projects/Projects';
import { Education } from './components/education/Education';
import { Training } from './components/training/Training';
import { Activities } from './components/activities/Activities';
import { Interests } from './components/interests/Interests';
import { Contact } from './components/contact/Contact';
import { Chatbot } from './components/chatbot/Chatbot';

export function App() {
  const [chatOpen, setChatOpen] = useState(false);

  return (
    <div className="relative min-h-screen bg-[#0B132B] text-[#EAEAEA] flex flex-col selection:bg-[#D4A373]/30 selection:text-[#FAEDCD]">
      {/* Sticky Header Navigation */}
      <Navbar onOpenChat={() => setChatOpen(true)} />

      {/* Main Content Sections */}
      <main className="flex-1">
        <Hero />
        <About />
        <Skills />
        <Experience />
        <Projects />
        <Education />
        <Training />
        <Activities />
        <Interests />
        <Contact />
      </main>

      {/* Floating Sriram AI Chatbot */}
      <Chatbot isOpen={chatOpen} onToggle={() => setChatOpen(!chatOpen)} />

      {/* Footer */}
      <Footer />
    </div>
  );
}

export default App;
