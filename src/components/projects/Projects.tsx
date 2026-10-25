import React, { useState, useMemo } from 'react';
import { SectionHeading } from '../ui/SectionHeading';
import { Container } from '../layout/Container';
import { ProjectCard } from './ProjectCard';
import { ProjectModal } from './ProjectModal';
import { portfolioData } from '../../data/portfolio';
import { ProjectItem } from '../../types';
import { Sparkles, Search, X, Filter, Star } from 'lucide-react';

export const Projects: React.FC = () => {
  const { projects } = portfolioData;
  const [selectedProject, setSelectedProject] = useState<ProjectItem | null>(null);
  const [selectedFilter, setSelectedFilter] = useState<string>('All');
  const [searchQuery, setSearchQuery] = useState<string>('');

  // Extract unique categories
  const categories = useMemo(() => {
    const rawCats = projects
      .map((p) => p.category)
      .filter((cat): cat is string => Boolean(cat && cat.trim() !== ''));
    return Array.from(new Set(rawCats));
  }, [projects]);

  // Compute counts
  const filterCounts = useMemo(() => {
    const counts: Record<string, number> = {
      All: projects.length,
      Featured: projects.filter((p) => p.featured).length,
    };
    for (const project of projects) {
      if (project.category) {
        counts[project.category] = (counts[project.category] || 0) + 1;
      }
    }
    return counts;
  }, [projects]);

  // Filter logic
  const filteredProjects = useMemo(() => {
    return projects.filter((project) => {
      let matchesFilter = true;
      if (selectedFilter === 'Featured') {
        matchesFilter = Boolean(project.featured);
      } else if (selectedFilter !== 'All') {
        matchesFilter = project.category === selectedFilter;
      }

      const q = searchQuery.toLowerCase().trim();
      if (!q) return matchesFilter;

      const matchesSearch =
        project.title.toLowerCase().includes(q) ||
        project.description.toLowerCase().includes(q) ||
        (project.subtitle && project.subtitle.toLowerCase().includes(q)) ||
        (project.category && project.category.toLowerCase().includes(q)) ||
        project.technologies.some((tech) => tech.toLowerCase().includes(q));

      return matchesFilter && matchesSearch;
    });
  }, [projects, selectedFilter, searchQuery]);

  const handleResetFilters = () => {
    setSelectedFilter('All');
    setSearchQuery('');
  };

  return (
    <section id="projects" className="py-20 md:py-28 relative overflow-hidden bg-[#0B132B]">
      {/* Background Glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-5xl h-96 bg-[#D4A373]/10 rounded-full blur-3xl pointer-events-none" />

      <Container>
        <SectionHeading
          badgeText="Work & Showcase"
          title="Featured & Analytics Projects"
          subtitle="Explore 9 production-ready data science projects, ETL pipelines, business intelligence dashboards, and predictive machine learning models."
        />

        {/* Filter & Search Bar */}
        <div className="mb-10 max-w-5xl mx-auto flex flex-col gap-4">
          {/* Top Filter Bar: Category & Featured Pills */}
          <div className="flex flex-wrap items-center justify-center gap-2">
            {/* All Pill */}
            <button
              onClick={() => setSelectedFilter('All')}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-mono font-medium transition-all duration-200 flex items-center gap-1.5 shadow-soft ${
                selectedFilter === 'All'
                  ? 'bg-gradient-to-r from-[#D4A373] via-[#E4BD96] to-[#D4A373] text-[#0B132B] font-bold shadow-glow-copper scale-[1.02]'
                  : 'bg-[#1C2541] hover:bg-[#232E4F] text-[#9EABC0] hover:text-[#EAEAEA] border border-[#232E4F]'
              }`}
            >
              <span>All Projects</span>
              <span
                className={`text-[10px] px-1.5 py-0.2 rounded-full ${
                  selectedFilter === 'All'
                    ? 'bg-[#0B132B]/30 text-[#0B132B] font-bold'
                    : 'bg-[#141D38] text-[#9EABC0]'
                }`}
              >
                {filterCounts['All']}
              </span>
            </button>

            {/* Featured Filter Pill */}
            <button
              onClick={() => setSelectedFilter('Featured')}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-mono font-medium transition-all duration-200 flex items-center gap-1.5 shadow-soft ${
                selectedFilter === 'Featured'
                  ? 'bg-gradient-to-r from-[#D4A373] via-[#E4BD96] to-[#D4A373] text-[#0B132B] font-bold shadow-glow-copper scale-[1.02]'
                  : 'bg-[#1C2541] hover:bg-[#232E4F] text-[#D4A373] border border-[#D4A373]/30'
              }`}
            >
              <Star className="w-3.5 h-3.5 fill-current" />
              <span>Featured</span>
              <span
                className={`text-[10px] px-1.5 py-0.2 rounded-full ${
                  selectedFilter === 'Featured'
                    ? 'bg-[#0B132B]/30 text-[#0B132B] font-bold'
                    : 'bg-[#141D38] text-[#D4A373]'
                }`}
              >
                {filterCounts['Featured']}
              </span>
            </button>

            {/* Category Pills */}
            {categories.map((cat) => {
              const isActive = selectedFilter === cat;
              const count = filterCounts[cat] ?? 0;
              return (
                <button
                  key={cat}
                  onClick={() => setSelectedFilter(cat)}
                  className={`px-3 py-1.5 rounded-xl text-xs font-mono font-medium transition-all duration-200 flex items-center gap-1.5 shadow-soft ${
                    isActive
                      ? 'bg-gradient-to-r from-[#D4A373] via-[#E4BD96] to-[#D4A373] text-[#0B132B] font-bold shadow-glow-copper scale-[1.02]'
                      : 'bg-[#1C2541] hover:bg-[#232E4F] text-[#9EABC0] hover:text-[#EAEAEA] border border-[#232E4F]'
                  }`}
                >
                  <span>{cat}</span>
                  <span
                    className={`text-[10px] px-1.5 py-0.2 rounded-full ${
                      isActive
                        ? 'bg-[#0B132B]/30 text-[#0B132B] font-bold'
                        : 'bg-[#141D38] text-[#9EABC0]'
                    }`}
                  >
                    {count}
                  </span>
                </button>
              );
            })}
          </div>

          {/* Search Input Bar */}
          <div className="relative max-w-md mx-auto w-full">
            <Search className="w-4 h-4 text-[#9EABC0] absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search across all 9 projects by title, tech, or topic..."
              className="w-full bg-[#141D38] text-[#EAEAEA] placeholder-[#9EABC0]/60 text-xs font-mono pl-9 pr-8 py-2.5 rounded-xl border border-[#232E4F] focus:border-[#D4A373] focus:outline-none transition-colors shadow-soft"
            />
            {searchQuery && (
              <button
                onClick={() => setSearchQuery('')}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-[#9EABC0] hover:text-[#EAEAEA] p-0.5"
                aria-label="Clear search"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            )}
          </div>
        </div>

        {/* Project Cards Grid */}
        {filteredProjects.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12 items-stretch">
            {filteredProjects.map((project, index) => (
              <ProjectCard
                key={project.id}
                project={project}
                index={index}
                onOpenModal={(p) => setSelectedProject(p)}
              />
            ))}
          </div>
        ) : (
          <div className="glass-panel bg-[#1C2541]/80 rounded-2xl p-10 text-center max-w-md mx-auto mb-12 border border-[#232E4F]">
            <Filter className="w-8 h-8 text-[#D4A373] mx-auto mb-3 opacity-80" />
            <h4 className="text-base font-bold font-heading text-[#EAEAEA] mb-1">
              No matching projects found
            </h4>
            <p className="text-xs text-[#9EABC0] mb-4">
              No projects match "{searchQuery}" in filter "{selectedFilter}".
            </p>
            <button
              onClick={handleResetFilters}
              className="px-4 py-2 rounded-xl text-xs font-mono font-semibold bg-[#D4A373]/20 hover:bg-[#D4A373]/30 text-[#FAEDCD] border border-[#D4A373]/40 transition-colors"
            >
              Reset Filters
            </button>
          </div>
        )}

        {/* Developer / Extensibility Callout Card */}
        <div className="glass-panel bg-[#1C2541]/90 rounded-2xl p-6 border border-[#D4A373]/25 max-w-3xl mx-auto text-center relative overflow-hidden shadow-2xl">
          <div className="flex items-center justify-center gap-2 text-[#D4A373] font-mono text-xs uppercase tracking-wider mb-2 font-semibold">
            <Sparkles className="w-4 h-4" />
            <span>Extensible Architecture</span>
          </div>
          <h4 className="text-base font-bold font-heading text-[#EAEAEA] mb-1">
            Centralized Project Configuration
          </h4>
          <p className="text-xs sm:text-sm text-[#9EABC0] leading-relaxed max-w-xl mx-auto">
            All 9 projects are driven from a single centralized data source in{' '}
            <code className="text-[#D4A373] font-mono bg-[#141D38] px-2 py-0.5 rounded border border-[#232E4F] shadow-soft">
              src/data/portfolio.ts
            </code>
            , complete with unit tests and local source repositories under{' '}
            <code className="text-[#6FFFE9] font-mono bg-[#141D38] px-2 py-0.5 rounded border border-[#232E4F] shadow-soft">
              projects/
            </code>
            .
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
