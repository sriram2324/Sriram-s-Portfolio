import React from 'react';
import { ArrowUp } from 'lucide-react';
import { GithubIcon, LinkedinIcon, LeetCodeIcon } from '../ui/Icons';
import { portfolioData } from '../../data/portfolio';

export const Footer: React.FC = () => {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

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
    <footer className="relative border-t border-[#1C2541] bg-[#060B1A] text-[#9EABC0] py-12 overflow-hidden">
      {/* Top subtle copper accent line */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-3/4 h-[1px] bg-gradient-to-r from-transparent via-[#D4A373]/50 to-transparent" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-center justify-between gap-6">
          {/* Brand Info */}
          <div className="flex flex-col items-center md:items-start text-center md:text-left">
            <a href="#home" className="flex items-center gap-2.5 group">
              <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-[#D4A373] via-[#FAEDCD] to-[#6FFFE9] p-[1px]">
                <div className="w-full h-full bg-[#0B132B] rounded-[7px] flex items-center justify-center font-heading font-black text-xs text-[#D4A373]">
                  SR
                </div>
              </div>
              <span className="font-heading font-bold text-lg text-[#EAEAEA] tracking-wider">
                {portfolioData.personal.name}
              </span>
            </a>
            <p className="text-xs text-[#9EABC0] mt-2 font-mono">
              Data Science • Python • Analytics Professional
            </p>
          </div>

          {/* Social Icons */}
          <div className="flex items-center gap-3">
            {portfolioData.socials.map((social) => (
              <a
                key={social.platform}
                href={social.url}
                target="_blank"
                rel="noopener noreferrer"
                className="w-9 h-9 rounded-xl bg-[#1C2541] flex items-center justify-center text-[#9EABC0] hover:text-[#D4A373] border border-[#232E4F] hover:border-[#D4A373]/50 hover:bg-[#232E4F] shadow-soft transition-all duration-200"
                aria-label={`${social.label} Profile (${social.username})`}
              >
                {getSocialIcon(social.platform)}
              </a>
            ))}
          </div>

          {/* Back to Top & Copyright */}
          <div className="flex flex-col md:flex-row items-center gap-4 text-xs text-[#9EABC0]">
            <span>© 2026 {portfolioData.personal.name}. All rights reserved.</span>
            <button
              onClick={scrollToTop}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#1C2541] hover:bg-[#232E4F] text-[#EAEAEA] hover:text-[#D4A373] border border-[#232E4F] hover:border-[#D4A373]/40 shadow-soft transition-colors"
              aria-label="Back to top"
            >
              <span>Back to Top</span>
              <ArrowUp className="w-3.5 h-3.5 text-[#D4A373]" />
            </button>
          </div>
        </div>
      </div>
    </footer>
  );
};
