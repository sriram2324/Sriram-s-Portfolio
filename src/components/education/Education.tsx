import React from 'react';
import { SectionHeading } from '../ui/SectionHeading';
import { Container } from '../layout/Container';
import { EducationCard } from './EducationCard';
import { portfolioData } from '../../data/portfolio';

export const Education: React.FC = () => {
  const { education } = portfolioData;

  return (
    <section id="education" className="py-20 md:py-28 relative overflow-hidden bg-[#0B132B] bg-radial-ambient">
      {/* Background ambient lighting */}
      <div className="absolute top-1/2 left-0 w-80 h-80 bg-[#D4A373]/10 rounded-full blur-3xl pointer-events-none" />

      <Container>
        <SectionHeading
          badgeText="Academic Background"
          title="Education"
          subtitle="Formal engineering and secondary academic qualifications with verified grades and institutions."
        />

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {education.map((item, index) => (
            <EducationCard key={item.id} item={item} index={index} />
          ))}
        </div>
      </Container>
    </section>
  );
};
