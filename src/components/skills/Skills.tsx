import React, { useState } from 'react';
import { SectionHeading } from '../ui/SectionHeading';
import { Container } from '../layout/Container';
import { SkillCategoryCard } from './SkillCategoryCard';
import { portfolioData } from '../../data/portfolio';
import { Layers, Terminal, Database, Briefcase } from 'lucide-react';

export const Skills: React.FC = () => {
  const { skillCategories } = portfolioData;
  const [activeFilter, setActiveFilter] = useState<string>('all');

  const filterButtons = [
    { id: 'all', label: 'All Skills', icon: Layers },
    { id: 'programming', label: 'Programming', icon: Terminal },
    { id: 'data', label: 'Data & Databases', icon: Database },
    { id: 'professional', label: 'Professional', icon: Briefcase },
  ];

  const filteredCategories =
    activeFilter === 'all'
      ? skillCategories
      : skillCategories.filter((cat) => cat.id === activeFilter);

  return (
    <section id="skills" className="py-20 md:py-28 relative overflow-hidden bg-[#0B132B] bg-radial-ambient">
      {/* Background glowing orbs */}
      <div className="absolute top-1/3 right-0 w-96 h-96 bg-[#D4A373]/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-10 left-10 w-72 h-72 bg-[#6FFFE9]/10 rounded-full blur-3xl pointer-events-none" />

      <Container>
        <SectionHeading
          badgeText="Capabilities"
          title="Technical & Professional Skills"
          subtitle="Core programming languages, analytical tools, database technologies, and workplace competencies."
        />

        {/* Category Filter Tabs */}
        <div className="flex flex-wrap justify-center gap-2 mb-12">
          {filterButtons.map((btn) => {
            const Icon = btn.icon;
            const isActive = activeFilter === btn.id;
            return (
              <button
                key={btn.id}
                onClick={() => setActiveFilter(btn.id)}
                className={`inline-flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium transition-all duration-200 shadow-soft ${
                  isActive
                    ? 'bg-gradient-to-r from-[#D4A373] via-[#E4BD96] to-[#D4A373] text-[#0B132B] font-bold shadow-glow-copper'
                    : 'bg-[#1C2541]/80 text-[#9EABC0] hover:text-[#EAEAEA] hover:bg-[#232E4F] border border-[#D4A373]/20'
                }`}
              >
                <Icon className="w-4 h-4" />
                <span>{btn.label}</span>
              </button>
            );
          })}
        </div>

        {/* Skill Category Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredCategories.map((category, index) => (
            <SkillCategoryCard key={category.id} category={category} index={index} />
          ))}
        </div>
      </Container>
    </section>
  );
};
