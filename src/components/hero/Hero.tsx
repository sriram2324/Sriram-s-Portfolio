import React from 'react';
import { motion } from 'framer-motion';
import {
  ArrowRight,
  Download,
  Mail,
  Sparkles,
} from 'lucide-react';
import { GithubIcon, LinkedinIcon, LeetCodeIcon } from '../ui/Icons';
import { portfolioData } from '../../data/portfolio';
import { TechCanvas } from './TechCanvas';
import { ProfileImage } from './ProfileImage';

export const Hero: React.FC = () => {
  const { personal, socials } = portfolioData;

  const getSocialIcon = (platform: string) => {
    switch (platform) {
      case 'github':
        return <GithubIcon className="w-4 h-4" />;
      case 'linkedin':
        return <LinkedinIcon className="w-4 h-4" />;
      case 'leetcode':
        return <LeetCodeIcon className="w-4 h-4" />;
      default:
        return null;
    }
  };

  return (
    <section
      id="home"
      className="relative min-h-[92vh] flex items-center justify-center pt-28 pb-16 md:pt-36 md:pb-24 overflow-hidden bg-[#0B132B] bg-radial-ambient"
    >
      {/* Background Interactive Data Nodes Canvas */}
      <TechCanvas />

      {/* Grid Pattern Overlay */}
      <div className="absolute inset-0 bg-tech-grid opacity-60 pointer-events-none" />

      {/* Ambient Glow Gradients */}
      <div className="absolute top-1/4 left-1/10 w-96 h-96 bg-[#D4A373]/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-1/4 right-1/10 w-96 h-96 bg-[#6FFFE9]/10 rounded-full blur-3xl pointer-events-none" />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center">
          
          {/* Left Column: Hero Text & Actions */}
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, ease: 'easeOut' }}
            className="lg:col-span-7 flex flex-col items-center lg:items-start text-center lg:text-left"
          >
            {/* Status / Role Tag */}
            <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-semibold tracking-wider uppercase mb-6 border bg-[#1C2541]/90 text-[#D4A373] border-[#D4A373]/30 shadow-soft backdrop-blur-md">
              <span className="w-2 h-2 rounded-full bg-[#6FFFE9] animate-ping" />
              <span>Data Science &amp; Python Professional</span>
            </div>

            {/* Name */}
            <h1 className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-extrabold font-heading tracking-tight leading-[1.1] text-[#EAEAEA] mb-4">
              Hi, I'm{' '}
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#D4A373] via-[#FAEDCD] to-[#6FFFE9]">
                {personal.name}
              </span>
            </h1>

            {/* Subtitle / Role */}
            <p className="text-xl sm:text-2xl font-semibold text-[#EAEAEA] mb-6 font-heading flex items-center justify-center lg:justify-start gap-2">
              <Sparkles className="w-5 h-5 text-[#D4A373] inline" />
              <span>{personal.role}</span>
            </p>

            {/* Resume Summary Description */}
            <p className="text-base sm:text-lg text-[#9EABC0] max-w-2xl leading-relaxed mb-8">
              {personal.bioSummary}
            </p>

            {/* CTA Action Buttons */}
            <div className="flex flex-wrap items-center justify-center lg:justify-start gap-3.5 mb-8 w-full sm:w-auto">
              {/* View Projects */}
              <a
                href="#projects"
                className="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl font-bold text-sm tracking-wide bg-gradient-to-r from-[#D4A373] via-[#E4BD96] to-[#D4A373] hover:opacity-95 text-[#0B132B] shadow-glow-copper transition-all duration-300 hover:scale-[1.02] active:scale-[0.98] w-full sm:w-auto"
              >
                <span>View Projects</span>
                <ArrowRight className="w-4 h-4" />
              </a>

              {/* Contact Me */}
              <a
                href="#contact"
                className="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl font-semibold text-sm text-[#EAEAEA] bg-[#1C2541] hover:bg-[#232E4F] border border-[#D4A373]/30 hover:border-[#D4A373] transition-all duration-300 hover:scale-[1.02] active:scale-[0.98] shadow-soft w-full sm:w-auto"
              >
                <Mail className="w-4 h-4 text-[#D4A373]" />
                <span>Contact Me</span>
              </a>

              {/* Download Resume */}
              <a
                href={personal.resumeUrl}
                download="Sriram_R_Resume.pdf"
                className="inline-flex items-center justify-center gap-2 px-5 py-3.5 rounded-xl font-semibold text-sm text-[#EAEAEA] bg-[#1C2541]/80 hover:bg-[#232E4F] hover:text-[#6FFFE9] border border-[#6FFFE9]/30 hover:border-[#6FFFE9] transition-all duration-300 hover:scale-[1.02] active:scale-[0.98] shadow-soft w-full sm:w-auto"
                title="Download Sriram R's Resume"
              >
                <Download className="w-4 h-4 text-[#6FFFE9]" />
                <span>Download Resume</span>
              </a>
            </div>

            {/* Social Buttons Row */}
            <div className="flex items-center gap-3 pt-4 border-t border-[#1C2541] w-full justify-center lg:justify-start">
              <span className="text-xs font-mono text-[#9EABC0] uppercase tracking-wider">
                Profiles:
              </span>
              <div className="flex items-center gap-2.5">
                {socials.map((social) => (
                  <a
                    key={social.platform}
                    href={social.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-[#1C2541] border border-[#232E4F] hover:border-[#D4A373]/50 hover:bg-[#232E4F] text-[#9EABC0] hover:text-[#D4A373] text-xs font-medium transition-all duration-200 group shadow-soft"
                    aria-label={`${social.label} Profile (${social.username})`}
                  >
                    <span className="text-[#9EABC0] group-hover:text-[#D4A373] transition-colors">
                      {getSocialIcon(social.platform)}
                    </span>
                    <span>{social.label}</span>
                  </a>
                ))}
              </div>
            </div>
          </motion.div>

          {/* Right Column: Interactive Profile & Data Visual */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.9, ease: 'easeOut' }}
            className="lg:col-span-5 flex justify-center items-center mt-6 lg:mt-0"
          >
            <ProfileImage />
          </motion.div>

        </div>
      </div>
    </section>
  );
};
