import React from 'react';
import { motion } from 'framer-motion';
import { ExternalLink, ArrowRight, Code2 } from 'lucide-react';
import { GithubIcon } from '../ui/Icons';
import { ProjectItem } from '../../types';

interface ProjectCardProps {
  project: ProjectItem;
  index: number;
  onOpenModal: (project: ProjectItem) => void;
}

export const ProjectCard: React.FC<ProjectCardProps> = ({ project, index, onOpenModal }) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 30 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-40px' }}
      transition={{ duration: 0.5, delay: index * 0.15 }}
      className="group glass-panel bg-[#1C2541]/90 rounded-2xl border border-[#D4A373]/20 hover:border-[#D4A373]/60 transition-all duration-300 flex flex-col justify-between overflow-hidden hover:shadow-card-hover relative"
    >
      {/* Top Banner / Image Area */}
      <div className="relative w-full h-48 bg-[#141D38] flex items-center justify-center border-b border-[#232E4F] overflow-hidden">
        {project.image ? (
          <img
            src={project.image}
            alt={project.title}
            className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
          />
        ) : (
          <div className="text-center p-4">
            <div className="w-14 h-14 rounded-2xl bg-[#1C2541] border border-[#D4A373]/30 flex items-center justify-center mx-auto mb-2.5 text-[#D4A373] group-hover:scale-110 group-hover:border-[#D4A373] transition-transform duration-300 shadow-soft">
              <Code2 className="w-7 h-7" />
            </div>
            <span className="text-xs font-mono text-[#D4A373] font-semibold">
              {project.subtitle || 'Data Science / Python'}
            </span>
          </div>
        )}

        {/* Status Badge */}
        {project.status === 'upcoming' && (
          <div className="absolute top-3 right-3 px-2.5 py-1 rounded-full text-[10px] font-mono font-semibold uppercase tracking-wider bg-[#6FFFE9]/10 text-[#6FFFE9] border border-[#6FFFE9]/30 shadow-soft backdrop-blur-md">
            Slot Ready
          </div>
        )}
      </div>

      {/* Card Body */}
      <div className="p-6 flex-1 flex flex-col justify-between">
        <div>
          <h3 className="text-xl font-bold font-heading text-[#EAEAEA] group-hover:text-[#D4A373] transition-colors mb-2">
            {project.title}
          </h3>

          <p className="text-sm text-[#9EABC0] leading-relaxed mb-4">
            {project.description}
          </p>

          {/* Technology Badges */}
          <div className="flex flex-wrap gap-1.5 mb-6">
            {project.technologies.map((tech) => (
              <span
                key={tech}
                className="text-[11px] font-mono px-2.5 py-1 rounded-md bg-[#141D38] border border-[#232E4F] text-[#EAEAEA] group-hover:border-[#D4A373]/30 transition-colors shadow-soft"
              >
                {tech}
              </span>
            ))}
          </div>
        </div>

        {/* Footer Actions */}
        <div className="pt-4 border-t border-[#232E4F] flex items-center justify-between gap-3">
          <button
            onClick={() => onOpenModal(project)}
            className="inline-flex items-center gap-1.5 text-xs font-semibold text-[#D4A373] hover:text-[#FAEDCD] group-hover:translate-x-0.5 transition-all"
          >
            <span>View Details &amp; Schema</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>

          {/* External links (only shown if configured) */}
          <div className="flex items-center gap-2">
            {project.github && project.github.trim() !== '' && (
              <a
                href={project.github}
                target="_blank"
                rel="noopener noreferrer"
                className="p-2 rounded-lg bg-[#141D38] hover:bg-[#232E4F] text-[#9EABC0] hover:text-[#D4A373] border border-[#232E4F] shadow-soft"
                aria-label={`GitHub repo for ${project.title}`}
              >
                <GithubIcon className="w-3.5 h-3.5" />
              </a>
            )}
            {project.liveDemo && project.liveDemo.trim() !== '' && (
              <a
                href={project.liveDemo}
                target="_blank"
                rel="noopener noreferrer"
                className="p-2 rounded-lg bg-[#D4A373]/15 hover:bg-[#D4A373]/25 text-[#D4A373] border border-[#D4A373]/30 shadow-soft"
                aria-label={`Live demo for ${project.title}`}
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
