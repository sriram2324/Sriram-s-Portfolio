import React from 'react';
import { motion, HTMLMotionProps } from 'framer-motion';
import { cn } from '../../utils/cn';

interface CardProps extends HTMLMotionProps<'div'> {
  children: React.ReactNode;
  className?: string;
  glow?: 'copper' | 'aqua' | 'slate' | 'none';
  hoverEffect?: boolean;
}

export const Card: React.FC<CardProps> = ({
  children,
  className = '',
  glow = 'none',
  hoverEffect = true,
  ...props
}) => {
  const glowStyles = {
    none: '',
    copper: 'hover:border-[#D4A373] hover:shadow-glow-copper',
    aqua: 'hover:border-[#6FFFE9] hover:shadow-glow-aqua',
    slate: 'hover:border-[#3A4B75] hover:shadow-card-hover',
  };

  return (
    <motion.div
      whileHover={hoverEffect ? { y: -3 } : undefined}
      transition={{ duration: 0.25, ease: 'easeOut' }}
      className={cn(
        'glass-panel rounded-2xl p-6 relative overflow-hidden transition-all duration-300 bg-[#1C2541]/90 border border-[#D4A373]/20',
        glowStyles[glow],
        className
      )}
      {...props}
    >
      {children}
    </motion.div>
  );
};
