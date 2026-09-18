import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Sparkles, Terminal, Database, Code, CheckCircle2 } from 'lucide-react';

interface ProfileImageProps {
  src?: string;
  alt?: string;
  className?: string;
}

export const ProfileImage: React.FC<ProfileImageProps> = ({
  src = '/profile.jpg',
  alt = 'Sriram R - Data Science & Python Professional',
  className = '',
}) => {
  const [imageError, setImageError] = useState(false);
  const [imageLoaded, setImageLoaded] = useState(false);

  return (
    <div className={`relative flex items-center justify-center ${className}`}>
      {/* Outer Glow Halo */}
      <div className="absolute -inset-4 bg-gradient-to-tr from-[#D4A373]/20 via-[#E4BD96]/10 to-[#6FFFE9]/20 rounded-full blur-2xl animate-pulse-slow pointer-events-none" />

      {/* Rotating Tech Orbit Ring */}
      <div className="absolute -inset-3 rounded-full border border-dashed border-[#D4A373]/30 animate-glow-spin pointer-events-none" />
      <div className="absolute -inset-6 rounded-full border border-dotted border-[#6FFFE9]/20 animate-glow-spin pointer-events-none [animation-direction:reverse] [animation-duration:20s]" />

      {/* Floating Mini Tech Badges */}
      {/* Top Left: Python */}
      <motion.div
        animate={{ y: [0, -6, 0] }}
        transition={{ duration: 4, repeat: Infinity, ease: 'easeInOut' }}
        className="absolute -top-3 -left-3 z-20 flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#1C2541]/95 text-[#EAEAEA] border border-[#D4A373]/40 text-xs font-mono font-medium shadow-glow-copper"
      >
        <Code className="w-3.5 h-3.5 text-[#D4A373]" />
        <span>Python</span>
      </motion.div>

      {/* Top Right: Data Science */}
      <motion.div
        animate={{ y: [0, 6, 0] }}
        transition={{ duration: 4.5, repeat: Infinity, ease: 'easeInOut', delay: 0.5 }}
        className="absolute -top-2 -right-4 z-20 flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#1C2541]/95 text-[#EAEAEA] border border-[#6FFFE9]/40 text-xs font-mono font-medium shadow-glow-aqua"
      >
        <Database className="w-3.5 h-3.5 text-[#6FFFE9]" />
        <span>Data Science</span>
      </motion.div>

      {/* Bottom Right: SQL */}
      <motion.div
        animate={{ y: [0, -5, 0] }}
        transition={{ duration: 3.8, repeat: Infinity, ease: 'easeInOut', delay: 1 }}
        className="absolute -bottom-2 -right-2 z-20 flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#1C2541]/95 text-[#EAEAEA] border border-[#E4BD96]/40 text-xs font-mono font-medium shadow-soft"
      >
        <Terminal className="w-3.5 h-3.5 text-[#E4BD96]" />
        <span>SQL / Analytics</span>
      </motion.div>

      {/* Main Avatar Container */}
      <motion.div
        animate={{ y: [0, -8, 0] }}
        transition={{ duration: 6, repeat: Infinity, ease: 'easeInOut' }}
        className="relative w-64 h-64 sm:w-72 sm:h-72 md:w-80 md:h-80 lg:w-88 lg:h-88 rounded-full p-1.5 bg-gradient-to-tr from-[#D4A373] via-[#FAEDCD] to-[#6FFFE9] shadow-glow-copper"
      >
        <div className="w-full h-full rounded-full bg-[#0B132B] overflow-hidden relative flex items-center justify-center border-2 border-[#1C2541]">
          {!imageError ? (
            <img
              src={src}
              alt={alt}
              onError={() => setImageError(true)}
              onLoad={() => setImageLoaded(true)}
              className={`w-full h-full object-cover object-[center_15%] rounded-full transition-opacity duration-500 ${
                imageLoaded ? 'opacity-100' : 'opacity-0'
              }`}
            />
          ) : null}

          {/* Fallback Professional Tech Avatar (shown if /profile.jpg is absent or errored) */}
          {(imageError || !imageLoaded) && (
            <div className="absolute inset-0 flex flex-col items-center justify-center bg-gradient-to-b from-[#141D38] via-[#0B132B] to-[#141D38] p-6 text-center select-none">
              {/* Monogram graphic */}
              <div className="relative mb-3">
                <div className="w-24 h-24 sm:w-28 sm:h-28 rounded-2xl bg-[#1C2541] border border-[#D4A373]/40 flex items-center justify-center shadow-glow-copper">
                  <span className="font-heading font-black text-4xl sm:text-5xl text-transparent bg-clip-text bg-gradient-to-r from-[#D4A373] to-[#6FFFE9]">
                    SR
                  </span>
                </div>
                <div className="absolute -bottom-2 -right-2 bg-[#D4A373] text-[#0B132B] p-1.5 rounded-full shadow-md">
                  <Sparkles className="w-3.5 h-3.5" />
                </div>
              </div>

              <span className="font-heading font-bold text-[#EAEAEA] text-base sm:text-lg">
                Sriram R
              </span>
              <span className="text-[11px] font-mono text-[#6FFFE9] mt-0.5 font-medium">
                Data Science &amp; Python
              </span>

              {/* Developer notice hint */}
              <div className="mt-3 px-2.5 py-1 rounded-md bg-[#1C2541] border border-[#232E4F] text-[10px] text-[#9EABC0] flex items-center gap-1 shadow-soft">
                <span>Replace:</span>
                <code className="text-[#D4A373] font-mono">/public/profile.jpg</code>
              </div>
            </div>
          )}

          {/* Glass overlay shine */}
          <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/5 to-transparent pointer-events-none rounded-full" />
        </div>
      </motion.div>

      {/* Status Pill Badge at bottom */}
      <div className="absolute -bottom-5 left-1/2 -translate-x-1/2 z-20 whitespace-nowrap">
        <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[#1C2541]/95 border border-[#D4A373]/30 text-[#EAEAEA] text-xs font-medium backdrop-blur-md shadow-lg">
          <CheckCircle2 className="w-3.5 h-3.5 text-[#6FFFE9]" />
          <span>Available for Opportunities</span>
        </div>
      </div>
    </div>
  );
};
