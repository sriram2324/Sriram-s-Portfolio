import React from 'react';
import { motion } from 'framer-motion';
import { SectionHeading } from '../ui/SectionHeading';
import { Container } from '../layout/Container';
import { portfolioData } from '../../data/portfolio';
import { Network, Lightbulb, Sparkles, ArrowUpRight, LucideIcon } from 'lucide-react';

const iconMap: Record<string, LucideIcon> = {
  Network,
  Lightbulb,
};

export const Interests: React.FC = () => {
  const { interests } = portfolioData;

  return (
    <section id="interests" className="py-20 md:py-28 relative overflow-hidden bg-[#0B132B]">
      {/* Background visual effects */}
      <div className="absolute bottom-0 left-1/3 w-96 h-96 bg-[#D4A373]/10 rounded-full blur-3xl pointer-events-none" />

      <Container>
        <SectionHeading
          badgeText="Vision & Passions"
          title="Areas of Interest"
          subtitle="Key domains driving my professional curiosity, innovation focus, and long-term career pursuits."
        />

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
          {interests.map((item, index) => {
            const Icon = iconMap[item.icon] || Sparkles;

            return (
              <motion.div
                key={item.id}
                initial={{ opacity: 0, scale: 0.95 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true, margin: '-40px' }}
                transition={{ duration: 0.5, delay: index * 0.15 }}
                className="glass-panel bg-[#1C2541]/90 rounded-3xl p-8 border border-[#D4A373]/20 hover:border-[#D4A373]/50 transition-all duration-300 group hover:shadow-card-hover relative overflow-hidden flex flex-col justify-between"
              >
                {/* Accent gradient behind card */}
                <div
                  className={`absolute inset-0 bg-gradient-to-br ${item.gradient} opacity-30 group-hover:opacity-50 transition-opacity duration-300 pointer-events-none`}
                />

                <div className="relative z-10">
                  <div className="flex items-center justify-between mb-6">
                    <div className="w-14 h-14 rounded-2xl bg-[#141D38] border border-[#232E4F] flex items-center justify-center text-[#D4A373] group-hover:scale-110 group-hover:border-[#D4A373]/50 transition-all shadow-soft">
                      <Icon className="w-7 h-7" />
                    </div>
                    <div className="w-8 h-8 rounded-full bg-[#141D38] border border-[#232E4F] flex items-center justify-center text-[#9EABC0] group-hover:text-[#6FFFE9] group-hover:border-[#6FFFE9]/40 transition-colors shadow-soft">
                      <ArrowUpRight className="w-4 h-4" />
                    </div>
                  </div>

                  <h3 className="text-2xl font-bold font-heading text-[#EAEAEA] group-hover:text-[#D4A373] transition-colors mb-3">
                    {item.title}
                  </h3>

                  <p className="text-sm sm:text-base text-[#9EABC0] leading-relaxed font-normal">
                    {item.description}
                  </p>
                </div>

                <div className="relative z-10 mt-8 pt-4 border-t border-[#232E4F] flex items-center gap-2 text-xs font-mono text-[#6FFFE9] font-semibold">
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Strategic Focus</span>
                </div>
              </motion.div>
            );
          })}
        </div>
      </Container>
    </section>
  );
};
