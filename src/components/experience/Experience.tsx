import React from 'react';
import { SectionHeading } from '../ui/SectionHeading';
import { Container } from '../layout/Container';
import { TimelineItem } from './TimelineItem';
import { portfolioData } from '../../data/portfolio';

export const Experience: React.FC = () => {
  const { experiences } = portfolioData;

  return (
    <section id="experience" className="py-20 md:py-28 relative overflow-hidden bg-[#0B132B]">
      {/* Background ambient radial gradients */}
      <div className="absolute top-1/4 left-1/4 w-80 h-80 bg-[#D4A373]/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-[#6FFFE9]/10 rounded-full blur-3xl pointer-events-none" />

      <Container>
        <SectionHeading
          badgeText="Work & Engagements"
          title="Practical Experience & Internships"
          subtitle="Hands-on industry internships and student developer program participation strictly verified from resume."
        />

        <div className="max-w-4xl mx-auto pt-6">
          {experiences.map((exp, index) => (
            <TimelineItem
              key={exp.id}
              experience={exp}
              index={index}
              isLast={index === experiences.length - 1}
            />
          ))}
        </div>
      </Container>
    </section>
  );
};
