import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Bot, Menu, X, Sparkles, Download } from 'lucide-react';
import { portfolioData } from '../../data/portfolio';

interface NavbarProps {
  onOpenChat: () => void;
}

const navLinks = [
  { name: 'Home', href: '#home' },
  { name: 'About', href: '#about' },
  { name: 'Skills', href: '#skills' },
  { name: 'Experience', href: '#experience' },
  { name: 'Projects', href: '#projects' },
  { name: 'Education', href: '#education' },
  { name: 'Contact', href: '#contact' },
];

export const Navbar: React.FC<NavbarProps> = ({ onOpenChat }) => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [activeSection, setActiveSection] = useState('home');

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);

      // Simple active section detection
      const sections = navLinks.map((link) => link.href.substring(1));
      const scrollPosition = window.scrollY + 200;

      for (const section of sections) {
        const el = document.getElementById(section);
        if (el) {
          const top = el.offsetTop;
          const height = el.offsetHeight;
          if (scrollPosition >= top && scrollPosition < top + height) {
            setActiveSection(section);
            break;
          }
        }
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleLinkClick = (href: string) => {
    setMobileMenuOpen(false);
    const element = document.querySelector(href);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header
      className={`fixed top-0 left-0 right-0 z-40 transition-all duration-300 ${
        isScrolled
          ? 'bg-[#0B132B]/90 backdrop-blur-xl border-b border-[#1C2541] shadow-lg shadow-black/40 py-3.5'
          : 'bg-transparent py-5'
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between">
          {/* Brand / Logo */}
          <a
            href="#home"
            className="flex items-center gap-2.5 group focus:outline-none"
            aria-label="Sriram R Home"
          >
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-[#D4A373] via-[#FAEDCD] to-[#6FFFE9] p-[1.5px] transition-transform duration-300 group-hover:scale-105 shadow-glow-copper">
              <div className="w-full h-full bg-[#0B132B] rounded-[10px] flex items-center justify-center font-heading font-black text-sm text-[#D4A373]">
                SR
              </div>
            </div>
            <div className="flex flex-col">
              <span className="font-heading font-bold text-lg tracking-wider text-[#EAEAEA] group-hover:text-[#D4A373] transition-colors">
                SRIRAM R
              </span>
              <span className="text-[10px] uppercase font-mono tracking-widest text-[#9EABC0] -mt-1">
                Data Science &amp; Python
              </span>
            </div>
          </a>

          {/* Desktop Navigation Links */}
          <nav className="hidden lg:flex items-center gap-1 bg-[#1C2541]/80 p-1.5 rounded-full border border-[#D4A373]/20 backdrop-blur-md">
            {navLinks.map((link) => {
              const isActive = activeSection === link.href.substring(1);
              return (
                <a
                  key={link.name}
                  href={link.href}
                  onClick={(e) => {
                    e.preventDefault();
                    handleLinkClick(link.href);
                  }}
                  className={`relative px-4 py-1.5 rounded-full text-sm font-medium transition-all duration-200 ${
                    isActive
                      ? 'text-[#0B132B] font-bold'
                      : 'text-[#9EABC0] hover:text-[#EAEAEA] hover:bg-white/5'
                  }`}
                >
                  {isActive && (
                    <motion.div
                      layoutId="activeNavIndicator"
                      className="absolute inset-0 bg-gradient-to-r from-[#D4A373] to-[#E4BD96] rounded-full shadow-sm"
                      transition={{ type: 'spring', stiffness: 350, damping: 30 }}
                    />
                  )}
                  <span className="relative z-10">{link.name}</span>
                </a>
              );
            })}
          </nav>

          {/* Right Action Items (Desktop) */}
          <div className="hidden md:flex items-center gap-3">
            {/* Resume Quick Download */}
            <a
              href={portfolioData.personal.resumeUrl}
              download="Sriram_R_Resume.pdf"
              className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-semibold text-[#EAEAEA] bg-[#1C2541] hover:bg-[#232E4F] border border-[#D4A373]/30 hover:border-[#D4A373] transition-all duration-200 shadow-soft"
              title="Download Sriram R's Resume"
            >
              <Download className="w-3.5 h-3.5 text-[#D4A373]" />
              <span>Resume</span>
            </a>

            {/* AI Assistant Button */}
            <button
              onClick={onOpenChat}
              className="relative inline-flex items-center gap-2 px-4 py-2 rounded-xl font-bold text-xs tracking-wide bg-gradient-to-r from-[#D4A373] via-[#E4BD96] to-[#6FFFE9] hover:opacity-95 text-[#0B132B] shadow-glow-copper transition-all duration-300 hover:scale-[1.02] active:scale-[0.98] group"
              aria-label="Open Sriram AI Chatbot"
            >
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#0B132B] opacity-75" />
                <span className="relative inline-flex rounded-full h-2 w-2 bg-[#0B132B]" />
              </span>
              <Bot className="w-4 h-4 text-[#0B132B] transition-transform group-hover:rotate-12" />
              <span>AI Assistant</span>
              <Sparkles className="w-3 h-3 text-[#0B132B]/80" />
            </button>
          </div>

          {/* Mobile Actions: AI trigger & Hamburger */}
          <div className="flex items-center gap-2 md:hidden">
            <button
              onClick={onOpenChat}
              className="p-2 rounded-lg bg-[#1C2541] border border-[#D4A373]/30 text-[#D4A373]"
              aria-label="Open AI Assistant"
            >
              <Bot className="w-5 h-5" />
            </button>

            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-2 rounded-lg text-[#EAEAEA] hover:text-[#D4A373] bg-[#1C2541] border border-[#D4A373]/20"
              aria-label="Toggle Navigation Menu"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Drawer */}
      <AnimatePresence>
        {mobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.25, ease: 'easeInOut' }}
            className="md:hidden glass-panel border-b border-[#1C2541] bg-[#0B132B]/98 overflow-hidden shadow-2xl"
          >
            <div className="px-5 py-6 space-y-3">
              {navLinks.map((link) => {
                const isActive = activeSection === link.href.substring(1);
                return (
                  <a
                    key={link.name}
                    href={link.href}
                    onClick={(e) => {
                      e.preventDefault();
                      handleLinkClick(link.href);
                    }}
                    className={`block px-4 py-2.5 rounded-xl text-base font-medium transition-colors ${
                      isActive
                        ? 'bg-[#D4A373]/15 text-[#FAEDCD] border border-[#D4A373]/40 font-bold'
                        : 'text-[#9EABC0] hover:bg-[#1C2541] hover:text-[#EAEAEA]'
                    }`}
                  >
                    {link.name}
                  </a>
                );
              })}

              <div className="pt-4 border-t border-[#1C2541] flex flex-col gap-2.5">
                <button
                  onClick={() => {
                    setMobileMenuOpen(false);
                    onOpenChat();
                  }}
                  className="w-full flex items-center justify-center gap-2 py-3 rounded-xl font-bold text-sm bg-gradient-to-r from-[#D4A373] via-[#E4BD96] to-[#6FFFE9] text-[#0B132B] shadow-glow-copper"
                >
                  <Bot className="w-4 h-4" />
                  <span>Launch Sriram AI Chatbot</span>
                </button>

                <a
                  href={portfolioData.personal.resumeUrl}
                  download="Sriram_R_Resume.pdf"
                  className="w-full flex items-center justify-center gap-2 py-2.5 rounded-xl font-medium text-sm text-[#EAEAEA] bg-[#1C2541] border border-[#D4A373]/30"
                >
                  <Download className="w-4 h-4 text-[#D4A373]" />
                  <span>Download Resume (PDF)</span>
                </a>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
};
