import React, { useState } from 'react';
import { SectionHeading } from '../ui/SectionHeading';
import { Container } from '../layout/Container';
import { ContactForm } from './ContactForm';
import { portfolioData } from '../../data/portfolio';
import { Mail, Phone, MapPin, Copy, Check, Sparkles } from 'lucide-react';
import { GithubIcon, LinkedinIcon, LeetCodeIcon } from '../ui/Icons';

export const Contact: React.FC = () => {
  const { personal, socials } = portfolioData;
  const [copiedEmail, setCopiedEmail] = useState(false);
  const [copiedPhone, setCopiedPhone] = useState(false);

  const copyToClipboard = (text: string, type: 'email' | 'phone') => {
    navigator.clipboard.writeText(text);
    if (type === 'email') {
      setCopiedEmail(true);
      setTimeout(() => setCopiedEmail(false), 2000);
    } else {
      setCopiedPhone(true);
      setTimeout(() => setCopiedPhone(false), 2000);
    }
  };

  const getSocialIcon = (platform: string) => {
    switch (platform) {
      case 'github':
        return <GithubIcon className="w-4 h-4" />;
      case 'linkedin':
        return <LinkedinIcon className="w-4 h-4" />;
      case 'leetcode':
        return <LeetCodeIcon className="w-4 h-4" />;
      default:
        return null;
    }
  };

  return (
    <section id="contact" className="py-20 md:py-28 relative overflow-hidden bg-[#0B132B] bg-radial-ambient">
      {/* Ambient background glows */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-[#D4A373]/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-[#6FFFE9]/10 rounded-full blur-3xl pointer-events-none" />

      <Container>
        <SectionHeading
          badgeText="Get In Touch"
          title="Contact Me"
          subtitle="Feel free to reach out for opportunities, collaborations, or data science discussions."
        />

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
          
          {/* Left Column: Direct Contact Info & Verified Socials */}
          <div className="lg:col-span-5 space-y-6">
            <div className="glass-panel bg-[#1C2541]/90 rounded-3xl p-6 sm:p-8 border border-[#D4A373]/25 shadow-2xl relative overflow-hidden">
              <div className="flex items-center gap-2 text-[#D4A373] font-mono text-xs uppercase tracking-wider mb-2 font-semibold">
                <Sparkles className="w-4 h-4" />
                <span>Direct Contact Details</span>
              </div>

              <h3 className="text-2xl font-bold font-heading text-[#EAEAEA] mb-6">
                Let's Connect
              </h3>

              <div className="space-y-4">
                {/* Email Item */}
                <div className="p-4 rounded-2xl bg-[#141D38] border border-[#232E4F] hover:border-[#D4A373]/40 transition-colors flex items-center justify-between gap-3 group shadow-soft">
                  <div className="flex items-center gap-3.5 overflow-hidden">
                    <div className="w-11 h-11 rounded-xl bg-[#1C2541] border border-[#232E4F] flex items-center justify-center text-[#D4A373] flex-shrink-0">
                      <Mail className="w-5 h-5" />
                    </div>
                    <div className="overflow-hidden">
                      <span className="text-[11px] font-mono uppercase text-[#9EABC0] block font-medium">
                        Email Address
                      </span>
                      <a
                        href={`mailto:${personal.email}`}
                        className="text-sm font-semibold text-[#EAEAEA] hover:text-[#D4A373] truncate block transition-colors"
                      >
                        {personal.email}
                      </a>
                    </div>
                  </div>
                  <button
                    onClick={() => copyToClipboard(personal.email, 'email')}
                    className="p-2 rounded-xl bg-[#1C2541] hover:bg-[#232E4F] text-[#9EABC0] hover:text-[#D4A373] border border-[#232E4F] transition-colors shadow-soft"
                    title="Copy Email"
                    aria-label="Copy Email"
                  >
                    {copiedEmail ? <Check className="w-4 h-4 text-[#6FFFE9]" /> : <Copy className="w-4 h-4" />}
                  </button>
                </div>

                {/* Phone Item */}
                <div className="p-4 rounded-2xl bg-[#141D38] border border-[#232E4F] hover:border-[#D4A373]/40 transition-colors flex items-center justify-between gap-3 group shadow-soft">
                  <div className="flex items-center gap-3.5 overflow-hidden">
                    <div className="w-11 h-11 rounded-xl bg-[#1C2541] border border-[#232E4F] flex items-center justify-center text-[#D4A373] flex-shrink-0">
                      <Phone className="w-5 h-5" />
                    </div>
                    <div>
                      <span className="text-[11px] font-mono uppercase text-[#9EABC0] block font-medium">
                        Phone Number
                      </span>
                      <a
                        href={`tel:${personal.phone}`}
                        className="text-sm font-semibold text-[#EAEAEA] hover:text-[#D4A373] transition-colors"
                      >
                        {personal.phone}
                      </a>
                    </div>
                  </div>
                  <button
                    onClick={() => copyToClipboard(personal.phone, 'phone')}
                    className="p-2 rounded-xl bg-[#1C2541] hover:bg-[#232E4F] text-[#9EABC0] hover:text-[#D4A373] border border-[#232E4F] transition-colors shadow-soft"
                    title="Copy Phone"
                    aria-label="Copy Phone"
                  >
                    {copiedPhone ? <Check className="w-4 h-4 text-[#6FFFE9]" /> : <Copy className="w-4 h-4" />}
                  </button>
                </div>

                {/* Location Item */}
                <div className="p-4 rounded-2xl bg-[#141D38] border border-[#232E4F] flex items-center gap-3.5 shadow-soft">
                  <div className="w-11 h-11 rounded-xl bg-[#1C2541] border border-[#232E4F] flex items-center justify-center text-[#D4A373] flex-shrink-0">
                    <MapPin className="w-5 h-5" />
                  </div>
                  <div>
                    <span className="text-[11px] font-mono uppercase text-[#9EABC0] block font-medium">
                      Current Location
                    </span>
                    <span className="text-sm font-semibold text-[#EAEAEA]">
                      {personal.location}
                    </span>
                  </div>
                </div>
              </div>

              {/* Social Profiles */}
              <div className="mt-8 pt-6 border-t border-[#232E4F]">
                <span className="text-xs font-mono uppercase tracking-wider text-[#9EABC0] block mb-3 font-medium">
                  Verified Social Channels:
                </span>
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                  {socials.map((social) => (
                    <a
                      key={social.platform}
                      href={social.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center gap-2 p-2.5 rounded-xl bg-[#141D38] border border-[#232E4F] hover:border-[#D4A373]/50 text-[#EAEAEA] hover:text-[#D4A373] hover:bg-[#1C2541] transition-colors shadow-soft"
                    >
                      <span className="text-[#D4A373]">{getSocialIcon(social.platform)}</span>
                      <span className="text-xs font-medium">{social.label}</span>
                    </a>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* Right Column: Contact Form */}
          <div className="lg:col-span-7">
            <ContactForm />
          </div>

        </div>
      </Container>
    </section>
  );
};
