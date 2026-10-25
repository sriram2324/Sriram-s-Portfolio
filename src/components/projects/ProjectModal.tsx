import React, { useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  X,
  ExternalLink,
  Sparkles,
  CheckCircle2,
  Code2,
  Layers,
  AlertCircle,
  TrendingUp,
  Database,
  Brain,
  Info,
} from 'lucide-react';
import { GithubIcon } from '../ui/Icons';
import { ProjectItem } from '../../types';

interface ProjectModalProps {
  project: ProjectItem | null;
  onClose: () => void;
}

const getProjectModalIcon = (category?: string, id?: string) => {
  if (category?.includes('Financial') || id?.includes('finance')) {
    return <TrendingUp className="w-8 h-8" />;
  }
  if (category?.includes('SQL') || id?.includes('retail')) {
    return <Database className="w-8 h-8" />;
  }
  if (category?.includes('Machine') || id?.includes('churn')) {
    return <Brain className="w-8 h-8" />;
  }
  return <Code2 className="w-8 h-8" />;
};

export const ProjectModal: React.FC<ProjectModalProps> = ({ project, onClose }) => {
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    if (project) {
      document.body.style.overflow = 'hidden';
      window.addEventListener('keydown', handleKeyDown);
    }
    return () => {
      document.body.style.overflow = 'unset';
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [project, onClose]);

  if (!project) return null;

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 overflow-y-auto">
        {/* Backdrop */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={onClose}
          className="fixed inset-0 bg-[#060B1A]/80 backdrop-blur-md"
        />

        {/* Modal Window */}
        <motion.div
          initial={{ opacity: 0, scale: 0.95, y: 20 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.95, y: 20 }}
          transition={{ duration: 0.3, ease: 'easeOut' }}
          className="relative w-full max-w-3xl bg-[#0B132B] rounded-3xl border border-[#D4A373]/30 p-6 sm:p-8 shadow-2xl z-10 my-8 overflow-hidden max-h-[90vh] flex flex-col"
        >
          {/* Top highlight bar */}
          <div className="absolute top-0 left-0 right-0 h-1.5 bg-gradient-to-r from-[#D4A373] via-[#FAEDCD] to-[#6FFFE9]" />

          {/* Modal Header */}
          <div className="flex items-start justify-between gap-4 pb-4 border-b border-[#1C2541]">
            <div>
              <div className="flex flex-wrap items-center gap-2 mb-2">
                {project.category && (
                  <span className="text-xs font-mono uppercase tracking-wider px-2.5 py-1 rounded-md bg-[#D4A373]/15 text-[#FAEDCD] border border-[#D4A373]/30 font-semibold">
                    {project.category}
                  </span>
                )}
                {project.status === 'in-progress' && (
                  <span className="text-xs font-mono px-2.5 py-1 rounded-md bg-amber-500/15 text-amber-300 border border-amber-500/30 flex items-center gap-1.5 font-semibold">
                    <span className="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse" />
                    In Progress
                  </span>
                )}
                {project.status === 'upcoming' && (
                  <span className="text-xs font-mono px-2.5 py-1 rounded-md bg-[#6FFFE9]/10 text-[#6FFFE9] border border-[#6FFFE9]/30 flex items-center gap-1.5 font-semibold">
                    <span className="w-1.5 h-1.5 rounded-full bg-[#6FFFE9]" />
                    Upcoming / Planned
                  </span>
                )}
                {project.status === 'completed' && (
                  <span className="text-xs font-mono px-2.5 py-1 rounded-md bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 flex items-center gap-1.5 font-semibold">
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                    Completed
                  </span>
                )}
              </div>
              <h3 className="text-2xl sm:text-3xl font-extrabold font-heading text-[#EAEAEA]">
                {project.title}
              </h3>
              {project.subtitle && (
                <p className="text-sm text-[#D4A373] font-mono mt-0.5 font-medium">
                  {project.subtitle}
                </p>
              )}
            </div>

            <button
              onClick={onClose}
              className="p-2 rounded-xl text-[#9EABC0] hover:text-[#EAEAEA] bg-[#1C2541] hover:bg-[#232E4F] border border-[#232E4F] transition-colors shadow-soft"
              aria-label="Close Project Modal"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* Modal Scrollable Content */}
          <div className="overflow-y-auto pr-1 py-6 space-y-6 flex-1 custom-scrollbar">
            {/* Visual Hero / Banner Area */}
            <div className="w-full h-44 sm:h-52 rounded-2xl bg-[#141D38] border border-[#232E4F] overflow-hidden relative flex items-center justify-center p-6 text-center">
              <div className="absolute inset-0 bg-gradient-to-br from-[#D4A373]/10 via-transparent to-[#6FFFE9]/5 pointer-events-none" />
              {project.image ? (
                <img
                  src={project.image}
                  alt={project.title}
                  className="w-full h-full object-cover"
                />
              ) : (
                <div className="relative z-10 select-none max-w-md">
                  <div className="w-16 h-16 rounded-2xl bg-[#1C2541] border border-[#D4A373]/30 flex items-center justify-center mx-auto mb-3 shadow-glow-copper text-[#D4A373]">
                    {getProjectModalIcon(project.category, project.id)}
                  </div>
                  <h4 className="font-heading font-bold text-[#EAEAEA] text-lg">
                    {project.title}
                  </h4>
                  <p className="text-xs text-[#9EABC0] mt-1 font-mono">
                    {project.category || 'Featured Data Science Project'}
                  </p>
                </div>
              )}
            </div>

            {/* Description */}
            <div>
              <h4 className="text-sm font-mono uppercase tracking-wider text-[#9EABC0] mb-2 flex items-center gap-2 font-semibold">
                <Sparkles className="w-4 h-4 text-[#D4A373]" />
                <span>Project Overview</span>
              </h4>
              <p className="text-base text-[#EAEAEA] leading-relaxed">
                {project.description}
              </p>
            </div>

            {/* Problem Statement */}
            {project.problemStatement && (
              <div className="p-4 rounded-xl bg-[#141D38] border border-[#232E4F]">
                <h4 className="text-xs font-mono uppercase tracking-wider text-[#9EABC0] mb-1.5 flex items-center gap-2 font-semibold">
                  <AlertCircle className="w-3.5 h-3.5 text-amber-400" />
                  <span>Problem Statement &amp; Objective</span>
                </h4>
                <p className="text-sm text-[#EAEAEA] leading-relaxed">
                  {project.problemStatement}
                </p>
              </div>
            )}

            {/* Solution */}
            {project.solution && (
              <div className="p-4 rounded-xl bg-[#141D38] border border-[#232E4F]">
                <h4 className="text-xs font-mono uppercase tracking-wider text-[#9EABC0] mb-1.5 flex items-center gap-2 font-semibold">
                  <Layers className="w-3.5 h-3.5 text-[#6FFFE9]" />
                  <span>Technical Solution &amp; Approach</span>
                </h4>
                <p className="text-sm text-[#EAEAEA] leading-relaxed">
                  {project.solution}
                </p>
              </div>
            )}

            {/* Key Features */}
            {project.keyFeatures && project.keyFeatures.length > 0 && (
              <div>
                <h4 className="text-sm font-mono uppercase tracking-wider text-[#9EABC0] mb-3 font-semibold">
                  Key Planned &amp; Delivered Features:
                </h4>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                  {project.keyFeatures.map((feat, idx) => (
                    <div
                      key={idx}
                      className="flex items-center gap-2 p-3 rounded-xl bg-[#141D38] border border-[#232E4F] text-sm text-[#EAEAEA]"
                    >
                      <CheckCircle2 className="w-4 h-4 text-[#6FFFE9] flex-shrink-0" />
                      <span>{feat}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Technologies */}
            <div>
              <h4 className="text-sm font-mono uppercase tracking-wider text-[#9EABC0] mb-2.5 font-semibold">
                Technologies &amp; Tools:
              </h4>
              <div className="flex flex-wrap gap-2">
                {project.technologies.map((tech) => (
                  <span
                    key={tech}
                    className="px-3 py-1.5 rounded-lg text-xs font-mono font-medium bg-[#D4A373]/15 text-[#FAEDCD] border border-[#D4A373]/30"
                  >
                    {tech}
                  </span>
                ))}
              </div>
            </div>

            {/* Implementation & Repository Status Note */}
            {project.details && (
              <div className="p-3.5 rounded-xl bg-[#1C2541] border border-dashed border-[#232E4F] text-xs text-[#9EABC0] flex items-start gap-2.5 font-mono">
                <Info className="w-4 h-4 text-[#D4A373] flex-shrink-0 mt-0.5" />
                <div>
                  <span className="text-[#D4A373] font-semibold">Implementation Status: </span>
                  {project.details}
                </div>
              </div>
            )}
          </div>

          {/* Modal Footer with Action Links & Clear Placeholders */}
          <div className="pt-4 border-t border-[#1C2541] flex flex-wrap items-center justify-between gap-3">
            <div className="flex flex-wrap items-center gap-2.5">
              {project.github && project.github.trim() !== '' ? (
                <a
                  href={project.github}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold bg-[#1C2541] hover:bg-[#232E4F] text-[#EAEAEA] border border-[#232E4F] transition-colors shadow-soft"
                >
                  <GithubIcon className="w-4 h-4" />
                  <span>GitHub Repo</span>
                </a>
              ) : (
                <div
                  className="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-mono bg-[#141D38] border border-[#232E4F] text-[#9EABC0]/80 shadow-soft"
                  title="Repository pending publication"
                >
                  <GithubIcon className="w-4 h-4 text-[#9EABC0]/50" />
                  <span>GitHub: Repository Pending Publication</span>
                </div>
              )}

              {project.liveDemo && project.liveDemo.trim() !== '' ? (
                <a
                  href={project.liveDemo}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold bg-gradient-to-r from-[#D4A373] via-[#E4BD96] to-[#D4A373] hover:opacity-95 text-[#0B132B] font-bold transition-colors shadow-glow-copper"
                >
                  <ExternalLink className="w-4 h-4" />
                  <span>Live Demo</span>
                </a>
              ) : (
                <div
                  className="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-mono bg-[#141D38] border border-[#232E4F] text-[#9EABC0]/80 shadow-soft"
                  title="Live deployment in preparation"
                >
                  <ExternalLink className="w-4 h-4 text-[#9EABC0]/50" />
                  <span>Live Demo: In Preparation</span>
                </div>
              )}
            </div>

            <button
              onClick={onClose}
              className="px-5 py-2 rounded-xl text-xs font-medium text-[#EAEAEA] bg-[#1C2541] hover:bg-[#232E4F] border border-[#232E4F] transition-colors ml-auto shadow-soft"
            >
              Close
            </button>
          </div>
        </motion.div>
      </div>
    </AnimatePresence>
  );
};
