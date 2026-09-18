import React from 'react';
import { motion } from 'framer-motion';
import { SectionHeading } from '../ui/SectionHeading';
import { Container } from '../layout/Container';
import { portfolioData } from '../../data/portfolio';
import { Award, Sparkles, CheckCircle2 } from 'lucide-react';

export const Training: React.FC = () => {
  const { training } = portfolioData;

  return (
    <section id="training" className="py-20 md:py-28 relative overflow-hidden bg-[#0B132B]">
      {/* Background gradient */}
      <div className="absolute top-1/3 right-1/4 w-96 h-96 bg-[#D4A373]/10 rounded-full blur-3xl pointer-events-none" />

      <Container>
        <SectionHeading
          badgeText="Workshops & Programs"
          title="Training & Certifications"
          subtitle="Specialized technical training programs focused on Python programming, interactive notebooks, and social impact."
        />

        <div className="max-w-4xl mx-auto space-y-6">
          {training.map((item, index) => (
            <motion.div
              key={item.id}
              initial={{ opacity: 0, y: 25 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '-40px' }}
              transition={{ duration: 0.5, delay: index * 0.15 }}
              className="glass-panel bg-[#1C2541]/90 rounded-2xl p-6 sm:p-8 border border-[#D4A373]/20 hover:border-[#D4A373]/50 transition-all duration-300 relative overflow-hidden group shadow-2xl hover:shadow-card-hover"
            >
              {/* Glowing Top Accent Line */}
              <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-[#D4A373] via-[#FAEDCD] to-[#6FFFE9]" />

              <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
                <div className="flex items-center gap-3.5">
                  <div className="w-12 h-12 rounded-xl bg-[#141D38] border border-[#232E4F] flex items-center justify-center text-[#D4A373] group-hover:scale-105 group-hover:border-[#D4A373]/50 transition-transform shadow-soft">
                    <Award className="w-6 h-6" />
                  </div>
                  <div>
                    <h3 className="text-xl sm:text-2xl font-bold font-heading text-[#EAEAEA] group-hover:text-[#D4A373] transition-colors">
                      {item.title}
                    </h3>
                    <p className="text-xs font-mono text-[#D4A373] mt-0.5 font-medium">
                      {item.organization}
                    </p>
                  </div>
                </div>

                <div className="px-3 py-1 rounded-full text-xs font-mono font-semibold bg-[#6FFFE9]/10 text-[#6FFFE9] border border-[#6FFFE9]/30 w-fit shadow-soft">
                  Verified Program
                </div>
              </div>

              <p className="text-base text-[#9EABC0] leading-relaxed mb-6">
                {item.description}
              </p>

              {/* Key Program Highlights */}
              <div className="mb-6">
                <h4 className="text-xs font-mono uppercase tracking-wider text-[#9EABC0] mb-3 flex items-center gap-2 font-semibold">
                  <Sparkles className="w-3.5 h-3.5 text-[#D4A373]" />
                  <span>Program Key Takeaways</span>
                </h4>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                  {item.keyPoints.map((point, idx) => (
                    <div
                      key={idx}
                      className="flex items-start gap-2.5 p-3 rounded-xl bg-[#141D38] border border-[#232E4F] text-xs sm:text-sm text-[#EAEAEA] shadow-soft"
                    >
                      <CheckCircle2 className="w-4 h-4 text-[#6FFFE9] flex-shrink-0 mt-0.5" />
                      <span>{point}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Technologies Applied */}
              <div className="pt-4 border-t border-[#232E4F] flex flex-wrap items-center gap-2">
                <span className="text-xs font-mono text-[#9EABC0] mr-2">Core Tools:</span>
                {item.technologies.map((tech) => (
                  <span
                    key={tech}
                    className="text-xs font-mono px-3 py-1 rounded-lg bg-[#141D38] border border-[#232E4F] text-[#EAEAEA] shadow-soft"
                  >
                    {tech}
                  </span>
                ))}
              </div>
            </motion.div>
          ))}
        </div>
      </Container>
    </section>
  );
};
