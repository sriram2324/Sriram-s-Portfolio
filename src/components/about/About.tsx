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

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-center">
            {/* Left Column: Professional Photo */}
            <div className="lg:col-span-4 flex flex-col items-center justify-center">
              <div className="relative group w-full max-w-[280px] sm:max-w-[300px]">
                {/* Ambient glow behind portrait */}
                <div className="absolute -inset-2 bg-gradient-to-tr from-[#D4A373]/30 via-[#FAEDCD]/15 to-[#6FFFE9]/30 rounded-3xl blur-xl opacity-70 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none" />

                {/* Photo Frame with subtle rounded corners */}
                <div className="relative rounded-2xl overflow-hidden border-2 border-[#D4A373]/40 bg-[#0B132B] shadow-2xl p-1.5">
                  <div className="w-full h-80 sm:h-96 rounded-xl overflow-hidden bg-[#141D38] relative">
                    <img
                      src={personal.profileImageUrl || '/images/sriram-formal.jpg'}
                      alt="Sriram R — Computer Science Engineering graduate"
                      loading="lazy"
                      decoding="async"
                      className="w-full h-full object-cover object-[center_15%] transition-transform duration-500 group-hover:scale-105"
                    />
                    {/* Subtle gradient vignette at bottom */}
                    <div className="absolute inset-0 bg-gradient-to-t from-[#0B132B]/90 via-transparent to-transparent pointer-events-none" />

                    {/* Caption badge */}
                    <div className="absolute bottom-3 left-3 right-3 text-center">
                      <span className="inline-block px-3 py-1 rounded-full text-xs font-mono font-semibold bg-[#1C2541]/95 text-[#D4A373] border border-[#D4A373]/30 shadow-soft backdrop-blur-md">
                        Sriram R • B.E. CSE
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Right Column: Recruiter-Friendly Narrative & Facts */}
            <div className="lg:col-span-8 flex flex-col justify-between space-y-6">
              <div>
                <div className="flex items-center gap-2 text-[#D4A373] font-mono text-xs uppercase tracking-wider mb-3 font-semibold">
                  <Sparkles className="w-4 h-4" />
                  <span>Professional Overview &amp; Background</span>
                </div>
                <h3 className="text-2xl sm:text-3xl font-bold font-heading text-[#EAEAEA] mb-4">
                  Computer Science Engineering Graduate &amp; Technology Enthusiast
                </h3>
                <p className="text-base sm:text-lg text-[#EAEAEA] leading-relaxed font-normal mb-4">
                  {personal.aboutText}
                </p>
                <p className="text-sm sm:text-base text-[#9EABC0] leading-relaxed">
                  During my academic journey at Paavai Engineering College (7.8 GPA) and practical internships at Corizo Edu Tech, Live Stream Technologies, and AICTE – Edu Skills, I developed hands-on capabilities across Python programming, relational database querying with SQL, data visualization, and data quality pipelines. I enjoy solving real problems with clean code, exploring data insights, and continuously learning modern software engineering practices.
                </p>
              </div>

              {/* Quick Fact Badges */}
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-4 border-t border-[#232E4F]">
                {quickFacts.map((fact, idx) => {
                  const Icon = fact.icon;
                  return (
                    <div
                      key={idx}
                      className="flex items-center gap-3 p-3 rounded-xl bg-[#141D38] border border-[#232E4F] hover:border-[#D4A373]/40 transition-colors shadow-soft"
                    >
                      <div className="p-2 rounded-lg bg-[#1C2541] text-[#D4A373] flex-shrink-0">
                        <Icon className="w-5 h-5" />
                      </div>
                      <div>
                        <div className="text-[11px] font-mono text-[#9EABC0]">{fact.label}</div>
                        <div className="text-sm font-semibold text-[#EAEAEA]">{fact.value}</div>
                        <div className="text-[11px] text-[#9EABC0]">{fact.detail}</div>
                      </div>
                    </div>
                  );
                })}
              </div>
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
