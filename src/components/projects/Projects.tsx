import React, { useState } from 'react';
import { SectionHeading } from '../ui/SectionHeading';
import { Container } from '../layout/Container';
import { ProjectCard } from './ProjectCard';
import { ProjectModal } from './ProjectModal';
import { portfolioData } from '../../data/portfolio';
import { ProjectItem } from '../../types';
import { Sparkles } from 'lucide-react';

export const Projects: React.FC = () => {
  const { projects } = portfolioData;
  const [selectedProject, setSelectedProject] = useState<ProjectItem | null>(null);

  return (
    <section id="projects" className="py-20 md:py-28 relative overflow-hidden bg-[#0B132B]">
      {/* Background Glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-5xl h-96 bg-[#D4A373]/10 rounded-full blur-3xl pointer-events-none" />

      <Container>
        <SectionHeading
          badgeText="Work & Showcase"
          title="Featured Projects"
          subtitle="A modular, production-ready project showcase system designed for data science pipelines, Python tools, and ML models."
        />

        {/* Project Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
          {projects.map((project, index) => (
            <ProjectCard
              key={project.id}
              project={project}
              index={index}
              onOpenModal={(p) => setSelectedProject(p)}
            />
          ))}
        </div>

        {/* Developer / Extensibility Callout Card */}
        <div className="glass-panel bg-[#1C2541]/90 rounded-2xl p-6 border border-[#D4A373]/25 max-w-3xl mx-auto text-center relative overflow-hidden shadow-2xl">
          <div className="flex items-center justify-center gap-2 text-[#D4A373] font-mono text-xs uppercase tracking-wider mb-2 font-semibold">
            <Sparkles className="w-4 h-4" />
            <span>Extensible Architecture</span>
          </div>
          <h4 className="text-base font-bold font-heading text-[#EAEAEA] mb-1">
            Easy Project Integration
          </h4>
          <p className="text-xs sm:text-sm text-[#9EABC0] leading-relaxed max-w-xl mx-auto">
            To add new projects or update existing repositories, simply update the entries in{' '}
            <code className="text-[#D4A373] font-mono bg-[#141D38] px-2 py-0.5 rounded border border-[#232E4F] shadow-soft">
              src/data/portfolio.ts
            </code>
            . The UI cards and detail modals will render automatically.
          </p>
        </div>

        {/* Modal Dialog */}
        <ProjectModal
          project={selectedProject}
          onClose={() => setSelectedProject(null)}
        />
      </Container>
    </section>
  );
};
