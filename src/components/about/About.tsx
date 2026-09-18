import React from 'react';
import { motion } from 'framer-motion';
import { SectionHeading } from '../ui/SectionHeading';
import { Container } from '../layout/Container';
import { HighlightCard } from './HighlightCard';
import { portfolioData } from '../../data/portfolio';
import { Sparkles, MapPin, GraduationCap, Award } from 'lucide-react';

export const About: React.FC = () => {
  const { personal, aboutHighlights } = portfolioData;

  const quickFacts = [
    {
      icon: GraduationCap,
      label: 'Academics',
      value: 'B.E. CSE (GPA 7.8)',
      detail: 'Paavai Engineering College',
    },
    {
      icon: MapPin,
      label: 'Location',
      value: 'Tamil Nadu, India',
      detail: 'Perambalur / Namakkal',
    },
    {
      icon: Award,
      label: 'Internships',
      value: '3 Practical Internships',
      detail: 'Data Science & AI/ML',
    },
  ];

  return (
    <section id="about" className="py-20 md:py-28 relative overflow-hidden bg-[#0B132B]">
      {/* Background ambient lighting */}
      <div className="absolute top-1/2 left-0 w-80 h-80 bg-[#D4A373]/10 rounded-full blur-3xl pointer-events-none" />

      <Container>
        <SectionHeading
          badgeText="Background & Focus"
          title="About Me"
          subtitle="A summary of my background in data science, programming, database management, and collaborative problem-solving."
        />

        {/* Main Narrative Card */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-40px' }}
          transition={{ duration: 0.6 }}
          className="glass-panel bg-[#1C2541]/90 rounded-2xl p-6 sm:p-8 md:p-10 mb-12 border border-[#D4A373]/25 relative overflow-hidden shadow-2xl"
        >
          {/* Top highlight gradient line */}
          <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-[#D4A373] via-[#FAEDCD] to-[#6FFFE9]" />

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            <div className="lg:col-span-8">
              <div className="flex items-center gap-2 text-[#D4A373] font-mono text-xs uppercase tracking-wider mb-3 font-semibold">
                <Sparkles className="w-4 h-4" />
                <span>Professional Overview</span>
              </div>
              <p className="text-lg sm:text-xl text-[#EAEAEA] leading-relaxed font-normal">
                {personal.aboutText}
              </p>
            </div>

            {/* Quick Fact Badges */}
            <div className="lg:col-span-4 flex flex-col gap-3">
              {quickFacts.map((fact, idx) => {
                const Icon = fact.icon;
                return (
                  <div
                    key={idx}
                    className="flex items-center gap-3.5 p-3 rounded-xl bg-[#141D38] border border-[#232E4F] hover:border-[#D4A373]/40 transition-colors shadow-soft"
                  >
                    <div className="p-2 rounded-lg bg-[#1C2541] text-[#D4A373]">
                      <Icon className="w-5 h-5" />
                    </div>
                    <div>
                      <div className="text-xs font-mono text-[#9EABC0]">{fact.label}</div>
                      <div className="text-sm font-semibold text-[#EAEAEA]">{fact.value}</div>
                      <div className="text-[11px] text-[#9EABC0]">{fact.detail}</div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </motion.div>

        {/* 4 Highlight Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {aboutHighlights.map((card, index) => (
            <HighlightCard key={card.id} card={card} index={index} />
          ))}
        </div>
      </Container>
    </section>
  );
};
