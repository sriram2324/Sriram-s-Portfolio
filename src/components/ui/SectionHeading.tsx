import React from 'react';
import { motion } from 'framer-motion';

interface SectionHeadingProps {
  badgeText?: string;
  title: string;
  subtitle?: string;
  center?: boolean;
  className?: string;
}

export const SectionHeading: React.FC<SectionHeadingProps> = ({
  badgeText,
  title,
  subtitle,
  center = true,
  className = '',
}) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-50px' }}
      transition={{ duration: 0.6, ease: 'easeOut' }}
      className={`mb-12 md:mb-16 ${center ? 'text-center' : 'text-left'} ${className}`}
    >
      {badgeText && (
        <div className={`inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-semibold tracking-wider uppercase mb-3.5 border bg-[#1C2541]/90 border-[#D4A373]/30 text-[#D4A373] backdrop-blur-md shadow-soft ${
          center ? 'mx-auto' : ''
        }`}>
          <span className="w-1.5 h-1.5 rounded-full bg-[#6FFFE9] animate-ping" />
          {badgeText}
        </div>
      )}

      <h2 className="text-3xl md:text-4xl lg:text-5xl font-extrabold font-heading tracking-tight text-[#EAEAEA]">
        {title}
      </h2>

      {subtitle && (
        <p className="mt-4 text-base md:text-lg text-[#9EABC0] max-w-2xl font-normal leading-relaxed mx-auto">
          {subtitle}
        </p>
      )}

      <div className={`h-1 w-20 bg-gradient-to-r from-[#D4A373] via-[#E4BD96] to-[#6FFFE9] rounded-full mt-5 ${
        center ? 'mx-auto' : ''
      }`} />
    </motion.div>
  );
};
