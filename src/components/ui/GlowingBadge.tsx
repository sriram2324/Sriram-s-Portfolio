import React from 'react';
import { cn } from '../../utils/cn';

interface GlowingBadgeProps {
  children: React.ReactNode;
  variant?: 'copper' | 'aqua' | 'slate' | 'amber';
  size?: 'sm' | 'md' | 'lg';
  className?: string;
  icon?: React.ReactNode;
}

export const GlowingBadge: React.FC<GlowingBadgeProps> = ({
  children,
  variant = 'copper',
  size = 'md',
  className = '',
  icon,
}) => {
  const variantStyles = {
    copper: 'bg-[#D4A373]/15 text-[#FAEDCD] border-[#D4A373]/30 hover:border-[#D4A373] hover:bg-[#D4A373]/25',
    aqua: 'bg-[#6FFFE9]/10 text-[#6FFFE9] border-[#6FFFE9]/30 hover:border-[#6FFFE9] hover:bg-[#6FFFE9]/20',
    slate: 'bg-[#1C2541] text-[#EAEAEA] border-[#232E4F] hover:border-[#D4A373]/40 hover:bg-[#232E4F]',
    amber: 'bg-amber-500/15 text-amber-300 border-amber-500/30 hover:border-amber-400 hover:bg-amber-500/25',
  };

  const sizeStyles = {
    sm: 'text-xs px-2.5 py-1',
    md: 'text-xs font-medium px-3 py-1.5',
    lg: 'text-sm font-medium px-4 py-2',
  };

  return (
    <span
      className={cn(
        'inline-flex items-center gap-1.5 rounded-full border transition-all duration-300 backdrop-blur-sm',
        variantStyles[variant] || variantStyles.copper,
        sizeStyles[size],
        className
      )}
    >
      {icon && <span className="flex-shrink-0">{icon}</span>}
      <span>{children}</span>
    </span>
  );
};
