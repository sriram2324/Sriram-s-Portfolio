import React from 'react';
import { motion } from 'framer-motion';
import { Code2, BarChart3, Database, Users2, LucideIcon } from 'lucide-react';
import { HighlightCardItem } from '../../types';

interface HighlightCardProps {
  card: HighlightCardItem;
  index: number;
}

const iconMap: Record<string, LucideIcon> = {
  Code2,
  BarChart3,
  Database,
  Users2,
};

export const HighlightCard: React.FC<HighlightCardProps> = ({ card, index }) => {
  const Icon = iconMap[card.icon] || Code2;

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-40px' }}
      transition={{ duration: 0.5, delay: index * 0.1 }}
      className={`group relative rounded-2xl p-6 glass-card bg-[#1C2541]/90 border ${card.borderColor} bg-gradient-to-br ${card.gradient} transition-all duration-300 hover:-translate-y-1 hover:shadow-card-hover`}
    >
      {/* Icon badge */}
      <div className="w-12 h-12 rounded-xl bg-[#141D38] border border-[#232E4F] flex items-center justify-center mb-4 transition-transform duration-300 group-hover:scale-105 shadow-soft">
        <Icon className="w-6 h-6 text-[#D4A373] group-hover:text-[#FAEDCD]" />
      </div>

      <h3 className="text-xl font-bold font-heading text-[#EAEAEA] mb-2 group-hover:text-[#D4A373] transition-colors">
        {card.title}
      </h3>

      <p className="text-sm text-[#9EABC0] leading-relaxed">
        {card.description}
      </p>

      {/* Ambient hover line */}
      <div className="absolute bottom-0 left-0 right-0 h-[2px] bg-gradient-to-r from-transparent via-[#D4A373]/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
    </motion.div>
  );
};
