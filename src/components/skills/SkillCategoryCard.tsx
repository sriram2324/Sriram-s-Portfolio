import React from 'react';
import { motion } from 'framer-motion';
import { Terminal, Database, Briefcase, Check, Sparkles, LucideIcon } from 'lucide-react';
import { SkillCategory } from '../../types';

interface SkillCategoryCardProps {
  category: SkillCategory;
  index: number;
}

const iconMap: Record<string, LucideIcon> = {
  Terminal,
  Database,
  Briefcase,
};

export const SkillCategoryCard: React.FC<SkillCategoryCardProps> = ({ category, index }) => {
  const Icon = iconMap[category.icon] || Terminal;

  return (
    <motion.div
      initial={{ opacity: 0, y: 25 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-50px' }}
      transition={{ duration: 0.5, delay: index * 0.15 }}
      className="glass-panel bg-[#1C2541]/90 rounded-2xl p-6 sm:p-7 border border-[#D4A373]/20 hover:border-[#D4A373]/50 transition-all duration-300 group hover:shadow-card-hover flex flex-col justify-between relative overflow-hidden"
    >
      {/* Ambient background glow */}
      <div
        className="absolute -top-12 -right-12 w-32 h-32 rounded-full blur-2xl opacity-15 pointer-events-none transition-opacity duration-300 group-hover:opacity-30"
        style={{ backgroundColor: category.color }}
      />

      <div>
        {/* Header */}
        <div className="flex items-center gap-3.5 mb-4">
          <div
            className="w-12 h-12 rounded-xl bg-[#141D38] border border-[#232E4F] flex items-center justify-center transition-transform duration-300 group-hover:scale-105 shadow-soft"
            style={{ color: category.color }}
          >
            <Icon className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-xl font-bold font-heading text-[#EAEAEA] group-hover:text-[#D4A373] transition-colors">
              {category.title}
            </h3>
            <p className="text-xs text-[#9EABC0] mt-0.5">
              {category.subtitle}
            </p>
          </div>
        </div>

        <div className="h-[1px] w-full bg-[#232E4F] my-4" />

        {/* Skills Chips */}
        <div className="flex flex-wrap gap-2.5">
          {category.skills.map((skill) => (
            <div
              key={skill.name}
              className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-sm font-medium transition-all duration-200 cursor-default shadow-soft ${
                skill.highlight
                  ? 'bg-[#D4A373]/15 border border-[#D4A373]/40 text-[#FAEDCD] hover:border-[#D4A373] hover:bg-[#D4A373]/25'
                  : 'bg-[#141D38] border border-[#232E4F] text-[#EAEAEA] hover:border-[#D4A373]/30 hover:bg-[#1C2541]'
              }`}
            >
              {skill.highlight ? (
                <Sparkles className="w-3.5 h-3.5 text-[#D4A373]" />
              ) : (
                <Check className="w-3.5 h-3.5 text-[#9EABC0]" />
              )}
              <span>{skill.name}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Category Footer Indicator */}
      <div className="mt-6 pt-4 border-t border-[#232E4F] flex items-center justify-between text-xs text-[#9EABC0] font-mono">
        <span>{category.skills.length} Core Areas</span>
        <span className="text-[#6FFFE9] font-semibold transition-colors">Verified</span>
      </div>
    </motion.div>
  );
};
