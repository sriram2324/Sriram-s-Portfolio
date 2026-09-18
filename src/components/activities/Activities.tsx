import React from 'react';
import { motion } from 'framer-motion';
import { SectionHeading } from '../ui/SectionHeading';
import { Container } from '../layout/Container';
import { portfolioData } from '../../data/portfolio';
import { HeartHandshake, Sparkles, UserCheck, Trophy, LucideIcon } from 'lucide-react';

const iconMap: Record<string, LucideIcon> = {
  HeartHandshake,
  Sparkles,
  UserCheck,
  Trophy,
};

export const Activities: React.FC = () => {
  const { activities } = portfolioData;

  return (
    <section id="activities" className="py-20 md:py-28 relative overflow-hidden bg-[#0B132B] bg-radial-ambient">
      {/* Background ambient lighting */}
      <div className="absolute top-1/2 right-1/10 w-80 h-80 bg-[#6FFFE9]/10 rounded-full blur-3xl pointer-events-none" />

      <Container>
        <SectionHeading
          badgeText="Leadership & Community"
          title="Extracurricular Activities"
          subtitle="Volunteer leadership, youth empowerment initiatives, campus placement coordination, and competitive sports."
        />

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {activities.map((activity, index) => {
            const Icon = iconMap[activity.icon] || Sparkles;

            return (
              <motion.div
                key={activity.id}
                initial={{ opacity: 0, y: 25 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: '-40px' }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="glass-panel bg-[#1C2541]/90 rounded-2xl p-6 border border-[#D4A373]/20 hover:border-[#D4A373]/50 transition-all duration-300 flex flex-col justify-between group hover:shadow-card-hover relative overflow-hidden"
              >
                {/* Accent glow on hover */}
                <div className="absolute -top-10 -right-10 w-28 h-28 bg-[#D4A373]/10 rounded-full blur-xl group-hover:bg-[#D4A373]/20 transition-all duration-300 pointer-events-none" />

                <div>
                  {/* Category Pill */}
                  <div className="flex items-center justify-between mb-4">
                    <span
                      className={`text-[10px] font-mono font-semibold uppercase tracking-wider px-2.5 py-1 rounded-full border shadow-soft ${activity.badgeColor}`}
                    >
                      {activity.category}
                    </span>
                  </div>

                  {/* Icon Box */}
                  <div className="w-12 h-12 rounded-xl bg-[#141D38] border border-[#232E4F] flex items-center justify-center text-[#D4A373] group-hover:scale-110 group-hover:border-[#D4A373]/50 transition-all mb-4 shadow-soft">
                    <Icon className="w-6 h-6" />
                  </div>

                  {/* Title */}
                  <h3 className="text-lg font-bold font-heading text-[#EAEAEA] group-hover:text-[#D4A373] transition-colors mb-2">
                    {activity.title}
                  </h3>

                  {/* Description */}
                  {activity.description && (
                    <p className="text-xs sm:text-sm text-[#9EABC0] leading-relaxed">
                      {activity.description}
                    </p>
                  )}
                </div>

                <div className="mt-5 pt-3 border-t border-[#232E4F] flex items-center gap-1 text-[11px] font-mono text-[#6FFFE9] font-semibold">
                  <span>Verified Engagement</span>
                </div>
              </motion.div>
            );
          })}
        </div>
      </Container>
    </section>
  );
};
