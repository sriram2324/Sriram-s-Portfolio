import React from 'react';
import { motion } from 'framer-motion';
import {
  ExternalLink,
  ArrowRight,
  TrendingUp,
  Database,
  Brain,
  Code2,
  Sparkles,
  Layers,
  BarChart3,
  Server
} from 'lucide-react';
import { GithubIcon } from '../ui/Icons';
import { ProjectItem } from '../../types';

interface ProjectCardProps {
  project: ProjectItem;
  index: number;
  onOpenModal: (project: ProjectItem) => void;
}

const getProjectIcon = (category?: string, id?: string) => {
  if (category?.includes('Financial') || id?.includes('finance')) {
    return <TrendingUp className="w-7 h-7" />;
  }
  if (category?.includes('SQL') || id?.includes('retail')) {
    return <Database className="w-7 h-7" />;
  }
  if (category?.includes('Machine') || category?.includes('NLP') || id?.includes('churn') || id?.includes('sentiment')) {
    return <Brain className="w-7 h-7" />;
  }
  if (category?.includes('Engineering') || id?.includes('pipeline')) {
    return <Server className="w-7 h-7" />;
  }
  if (category?.includes('Commercial') || category?.includes('Business') || id?.includes('ecommerce') || id?.includes('report')) {
    return <BarChart3 className="w-7 h-7" />;
  }
  return <Code2 className="w-7 h-7" />;
};

export const ProjectCard: React.FC<ProjectCardProps> = ({ project, index, onOpenModal }) => {
  const isFeatured = Boolean(project.featured);

  return (
    <motion.div
      initial={{ opacity: 0, y: 30 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-40px' }}
      transition={{ duration: 0.5, delay: (index % 6) * 0.1 }}
      className={`group glass-panel bg-[#1C2541]/90 rounded-2xl transition-all duration-300 flex flex-col justify-between overflow-hidden relative h-full ${
        isFeatured
          ? 'border-2 border-[#D4A373]/50 hover:border-[#D4A373] shadow-glow-copper/20 hover:shadow-card-hover'
          : 'border border-[#232E4F] hover:border-[#D4A373]/50 hover:shadow-card-hover'
      }`}
    >
      {/* Top Banner / Image Area */}
      <div className="relative w-full h-48 bg-[#141D38] flex items-center justify-center border-b border-[#232E4F] overflow-hidden">
        {/* Subtle background glow */}
        <div
          className={`absolute inset-0 bg-gradient-to-br pointer-events-none ${
            isFeatured
              ? 'from-[#D4A373]/15 via-transparent to-[#6FFFE9]/10'
              : 'from-[#141D38] via-transparent to-[#232E4F]/30'
          }`}
        />

        {project.image ? (
          <img
            src={project.image}
            alt={project.title}
            className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
          />
        ) : (
          <div className="text-center p-4 relative z-10">
            <div
              className={`w-14 h-14 rounded-2xl bg-[#1C2541] flex items-center justify-center mx-auto mb-2.5 transition-transform duration-300 shadow-soft group-hover:scale-110 ${
                isFeatured
                  ? 'border border-[#D4A373]/50 text-[#D4A373] group-hover:border-[#D4A373]'
                  : 'border border-[#232E4F] text-[#9EABC0] group-hover:text-[#D4A373]'
              }`}
            >
              {getProjectIcon(project.category, project.id)}
            </div>
            <span className="text-xs font-mono text-[#D4A373] font-semibold line-clamp-1">
              {project.subtitle || project.category || 'Data Science / Python'}
            </span>
          </div>
        )}

        {/* Top-Left Badges (Featured + Category) */}
        <div className="absolute top-3 left-3 flex flex-wrap items-center gap-1.5 z-20">
          {isFeatured && (
            <div className="px-2 py-0.5 rounded-md text-[10px] font-mono font-bold uppercase tracking-wider bg-gradient-to-r from-[#D4A373] to-[#E4BD96] text-[#0B132B] shadow-glow-copper flex items-center gap-1">
              <Sparkles className="w-2.5 h-2.5" />
              <span>Featured</span>
            </div>
          )}
          {project.category && (
            <div className="px-2 py-0.5 rounded-md text-[10px] font-mono font-semibold uppercase tracking-wider bg-[#0B132B]/85 text-[#D4A373] border border-[#D4A373]/30 shadow-soft backdrop-blur-md">
              {project.category}
            </div>
          )}
        </div>

        {/* Status Badge on Top-Right */}
        <div className="absolute top-3 right-3 z-20">
          {project.status === 'completed' && (
            <div className="px-2.5 py-1 rounded-full text-[10px] font-mono font-semibold uppercase tracking-wider bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 shadow-soft backdrop-blur-md flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
              <span>Completed</span>
            </div>
          )}
          {project.status === 'in-progress' && (
            <div className="px-2.5 py-1 rounded-full text-[10px] font-mono font-semibold uppercase tracking-wider bg-amber-500/15 text-amber-300 border border-amber-500/30 shadow-soft backdrop-blur-md flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse" />
              <span>In Progress</span>
            </div>
          )}
          {project.status === 'upcoming' && (
            <div className="px-2.5 py-1 rounded-full text-[10px] font-mono font-semibold uppercase tracking-wider bg-[#6FFFE9]/10 text-[#6FFFE9] border border-[#6FFFE9]/30 shadow-soft backdrop-blur-md flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-[#6FFFE9]" />
              <span>Upcoming</span>
            </div>
          )}
        </div>
      </div>

      {/* Card Body */}
      <div className="p-6 flex-1 flex flex-col justify-between">
        <div>
          <h3 className="text-lg sm:text-xl font-bold font-heading text-[#EAEAEA] group-hover:text-[#D4A373] transition-colors mb-2.5 line-clamp-2 min-h-[3.25rem]">
            {project.title}
          </h3>

          <p className="text-sm text-[#9EABC0] leading-relaxed mb-4 line-clamp-3">
            {project.description}
          </p>

          {/* Technology Badges */}
          <div className="flex flex-wrap gap-1.5 mb-6">
            {project.technologies.slice(0, 5).map((tech) => (
              <span
                key={tech}
                className="text-[11px] font-mono px-2.5 py-1 rounded-md bg-[#141D38] border border-[#232E4F] text-[#EAEAEA] group-hover:border-[#D4A373]/30 transition-colors shadow-soft"
              >
                {tech}
              </span>
            ))}
            {project.technologies.length > 5 && (
              <span className="text-[10px] font-mono px-2 py-1 rounded-md bg-[#141D38] border border-[#232E4F] text-[#9EABC0]">
                +{project.technologies.length - 5}
              </span>
            )}
          </div>
        </div>

        {/* Footer Actions */}
        <div className="pt-4 border-t border-[#232E4F] flex items-center justify-between gap-3">
          <button
            onClick={() => onOpenModal(project)}
            className="inline-flex items-center gap-1.5 text-xs font-semibold text-[#D4A373] hover:text-[#FAEDCD] group-hover:translate-x-0.5 transition-all"
          >
            <span>View Details</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>

          {/* External links or clear placeholders */}
          <div className="flex items-center gap-2">
            {project.github && project.github.trim() !== '' ? (
              <a
                href={project.github}
                target="_blank"
                rel="noopener noreferrer"
                className="p-2 rounded-lg bg-[#141D38] hover:bg-[#232E4F] text-[#9EABC0] hover:text-[#D4A373] border border-[#232E4F] shadow-soft transition-colors"
                aria-label={`GitHub repo for ${project.title}`}
                title="View Code on GitHub"
              >
                <GithubIcon className="w-3.5 h-3.5" />
              </a>
            ) : (
              <span
                className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md bg-[#141D38]/80 text-[#9EABC0]/70 text-[10px] font-mono border border-[#232E4F] select-none cursor-default"
                title="Repository pending publication"
              >
                <GithubIcon className="w-3 h-3 opacity-60" />
                <span>Repo Pending</span>
              </span>
            )}

            {project.liveDemo && project.liveDemo.trim() !== '' && (
              <a
                href={project.liveDemo}
                target="_blank"
                rel="noopener noreferrer"
                className="p-2 rounded-lg bg-[#D4A373]/15 hover:bg-[#D4A373]/25 text-[#D4A373] border border-[#D4A373]/30 shadow-soft transition-colors"
                aria-label={`Live demo for ${project.title}`}
                title="Live Demo"
              >
                <ExternalLink className="w-3.5 h-3.5" />
              </a>
            )}
          </div>
        </div>
      </div>
    </motion.div>
  );
};
