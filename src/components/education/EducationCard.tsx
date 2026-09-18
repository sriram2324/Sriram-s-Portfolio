import React from 'react';
import { motion } from 'framer-motion';
import { GraduationCap, Award, BookOpen, Calendar, MapPin, LucideIcon } from 'lucide-react';
import { EducationItem } from '../../types';

interface EducationCardProps {
  item: EducationItem;
  index: number;
}

const iconMap: Record<string, LucideIcon> = {
  GraduationCap,
  Award,
  BookOpen,
};

export const EducationCard: React.FC<EducationCardProps> = ({ item, index }) => {
  const Icon = iconMap[item.icon] || GraduationCap;

  return (
    <motion.div
      initial={{ opacity: 0, y: 25 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-40px' }}
      transition={{ duration: 0.5, delay: index * 0.12 }}
      className="glass-panel bg-[#1C2541]/90 rounded-2xl p-6 sm:p-7 border border-[#D4A373]/20 hover:border-[#D4A373]/50 transition-all duration-300 flex flex-col justify-between group hover:shadow-card-hover relative overflow-hidden"
    >
      {/* Ambient background glow */}
      <div className="absolute top-0 right-0 w-32 h-32 bg-[#D4A373]/10 rounded-full blur-2xl pointer-events-none" />

      <div>
        {/* Top Header with Icon & Grade Badge */}
        <div className="flex items-start justify-between gap-3 mb-4">
          <div className="w-12 h-12 rounded-xl bg-[#141D38] border border-[#232E4F] flex items-center justify-center text-[#D4A373] group-hover:scale-105 group-hover:border-[#D4A373]/50 transition-all shadow-soft">
            <Icon className="w-6 h-6" />
          </div>

          <div className="text-right">
            <span className="text-[10px] font-mono uppercase tracking-wider text-[#9EABC0] block font-medium">
              {item.gradeLabel}
            </span>
            <span className="inline-block px-3 py-1 rounded-full text-sm font-bold font-mono bg-[#D4A373]/15 border border-[#D4A373]/35 text-[#FAEDCD] shadow-soft mt-0.5">
              {item.gradeValue}
            </span>
          </div>
        </div>

        {/* Degree & Field */}
        <h3 className="text-xl font-bold font-heading text-[#EAEAEA] group-hover:text-[#D4A373] transition-colors">
          {item.degree}
        </h3>

        {item.field && (
          <p className="text-sm font-medium text-[#6FFFE9] font-mono mt-0.5 mb-2">
            {item.field}
          </p>
        )}

        {/* Institution Name */}
        <div className="text-sm font-semibold text-[#EAEAEA] mt-2">
          {item.institution}
        </div>
      </div>

      {/* Footer Details: Location & Date */}
      <div className="mt-6 pt-4 border-t border-[#232E4F] flex flex-wrap items-center justify-between gap-2 text-xs font-mono text-[#9EABC0]">
        <div className="flex items-center gap-1.5">
          <MapPin className="w-3.5 h-3.5 text-[#D4A373]" />
          <span>{item.location}</span>
        </div>
        <div className="flex items-center gap-1.5 bg-[#141D38] px-2.5 py-1 rounded-md border border-[#232E4F] text-[#EAEAEA] shadow-soft">
          <Calendar className="w-3.5 h-3.5 text-[#6FFFE9]" />
          <span>{item.completionDate}</span>
        </div>
      </div>
    </motion.div>
  );
};
