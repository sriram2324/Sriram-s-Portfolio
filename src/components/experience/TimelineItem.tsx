import React from 'react';
import { motion } from 'framer-motion';
import { Briefcase, Calendar, MapPin, CheckCircle2, Award } from 'lucide-react';
import { ExperienceItem } from '../../types';

interface TimelineItemProps {
  experience: ExperienceItem;
  index: number;
  isLast: boolean;
}

export const TimelineItem: React.FC<TimelineItemProps> = ({ experience, index, isLast }) => {
  return (
    <div className="relative flex items-start gap-6 md:gap-8 pb-12 group">
      {/* Vertical Timeline Line */}
      {!isLast && (
        <div className="absolute top-12 left-5 md:left-6 bottom-0 w-[2px] bg-gradient-to-b from-[#D4A373]/60 via-[#E4BD96]/40 to-[#6FFFE9]/20" />
      )}

      {/* Timeline Node Icon */}
      <motion.div
        initial={{ scale: 0 }}
        whileInView={{ scale: 1 }}
        viewport={{ once: true }}
        transition={{ duration: 0.4, delay: index * 0.1 }}
        className="relative z-10 w-10 h-10 md:w-12 md:h-12 rounded-2xl bg-[#1C2541] border-2 border-[#D4A373] flex items-center justify-center text-[#D4A373] group-hover:border-[#6FFFE9] group-hover:text-[#6FFFE9] shadow-glow-copper transition-all duration-300 flex-shrink-0"
      >
        {experience.type === 'participant' ? (
          <Award className="w-5 h-5" />
        ) : (
          <Briefcase className="w-5 h-5" />
        )}
      </motion.div>

      {/* Experience Content Card */}
      <motion.div
        initial={{ opacity: 0, x: 20 }}
        whileInView={{ opacity: 1, x: 0 }}
        viewport={{ once: true, margin: '-40px' }}
        transition={{ duration: 0.5, delay: index * 0.1 }}
        className="flex-1 glass-panel bg-[#1C2541]/90 rounded-2xl p-6 sm:p-7 border border-[#D4A373]/20 group-hover:border-[#D4A373]/50 transition-all duration-300 relative overflow-hidden shadow-2xl hover:shadow-card-hover"
      >
        {/* Top ambient highlight */}
        <div className="absolute top-0 right-0 w-32 h-32 bg-[#D4A373]/10 rounded-full blur-2xl pointer-events-none" />

        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-3">
          <div>
            <span className="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-mono font-semibold uppercase tracking-wider bg-[#D4A373]/15 text-[#FAEDCD] border border-[#D4A373]/30 mb-1.5 shadow-soft">
              {experience.type === 'participant' ? 'Club Participant' : 'Internship'}
            </span>
            <h3 className="text-xl font-bold font-heading text-[#EAEAEA] group-hover:text-[#D4A373] transition-colors">
              {experience.role}
            </h3>
          </div>

          {/* Period Badge */}
          <div className="flex items-center gap-1.5 text-xs font-mono text-[#9EABC0] bg-[#141D38] px-3 py-1.5 rounded-lg border border-[#232E4F] shadow-soft w-fit">
            <Calendar className="w-3.5 h-3.5 text-[#D4A373]" />
            <span>{experience.period}</span>
          </div>
        </div>

        {/* Organization Name */}
        <div className="text-base font-semibold text-[#EAEAEA] mb-4 flex items-center gap-2">
          <span>{experience.organization}</span>
          {experience.location && (
            <span className="text-xs text-[#9EABC0] font-normal flex items-center gap-1">
              • <MapPin className="w-3 h-3 text-[#9EABC0] inline" /> {experience.location}
            </span>
          )}
        </div>

        {/* Highlights (if provided like GDSC) */}
        {experience.highlights && experience.highlights.length > 0 && (
          <div className="mb-4 space-y-2">
            <div className="text-xs font-mono uppercase tracking-wider text-[#9EABC0] font-semibold">
              Key Activities &amp; Highlights:
            </div>
            <ul className="space-y-1.5 text-sm text-[#EAEAEA]">
              {experience.highlights.map((item, idx) => (
                <li key={idx} className="flex items-start gap-2">
                  <CheckCircle2 className="w-4 h-4 text-[#6FFFE9] flex-shrink-0 mt-0.5" />
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Technology tags */}
        {experience.technologies && experience.technologies.length > 0 && (
          <div className="flex flex-wrap gap-2 pt-3 border-t border-[#232E4F]">
            {experience.technologies.map((tech) => (
              <span
                key={tech}
                className="text-xs font-mono px-2.5 py-1 rounded-md bg-[#141D38] border border-[#232E4F] text-[#EAEAEA] shadow-soft"
              >
                {tech}
              </span>
            ))}
          </div>
        )}
      </motion.div>
    </div>
  );
};
