import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Send, CheckCircle2, AlertCircle, RefreshCw } from 'lucide-react';
import confetti from 'canvas-confetti';

export const ContactForm: React.FC = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
  });

  const [errors, setErrors] = useState<Record<string, string>>({});
  const [submitted, setSubmitted] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const validate = () => {
    const errs: Record<string, string> = {};
    if (!formData.name.trim()) {
      errs.name = 'Please enter your name';
    }
    if (!formData.email.trim()) {
      errs.email = 'Please enter your email address';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      errs.email = 'Please enter a valid email address';
    }
    if (!formData.subject.trim()) {
      errs.subject = 'Please enter a subject';
    }
    if (!formData.message.trim()) {
      errs.message = 'Please enter your message';
    } else if (formData.message.trim().length < 10) {
      errs.message = 'Message must be at least 10 characters long';
    }
    return errs;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const errs = validate();
    if (Object.keys(errs).length > 0) {
      setErrors(errs);
      return;
    }

    setErrors({});
    setIsSubmitting(true);

    // Simulate client-side transmission
    setTimeout(() => {
      setIsSubmitting(false);
      setSubmitted(true);

      // Trigger celebratory confetti effect
      try {
        confetti({
          particleCount: 75,
          spread: 70,
          origin: { y: 0.7 },
          colors: ['#D4A373', '#E4BD96', '#6FFFE9'],
        });
      } catch (err) {
        // Safe fallback
      }
    }, 500);
  };

  const handleReset = () => {
    setFormData({ name: '', email: '', subject: '', message: '' });
    setSubmitted(false);
    setErrors({});
  };

  const quickTemplates = [
    { label: '👋 General Inquiry', subject: 'Opportunity Discussion', text: "Hello Sriram, I came across your portfolio and would like to connect regarding an opportunity." },
    { label: '💼 Data Science Role', subject: 'Data Science Opportunity', text: "Hi Sriram, we have an open Data Science / Python role and your profile looks like a great fit." },
  ];

  const applyTemplate = (t: typeof quickTemplates[0]) => {
    setFormData({
      ...formData,
      subject: t.subject,
      message: t.text,
    });
  };

  return (
    <div className="glass-panel bg-[#1C2541]/90 rounded-3xl p-6 sm:p-8 md:p-10 border border-[#D4A373]/25 shadow-2xl relative overflow-hidden">
      {/* Top accent gradient */}
      <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-[#D4A373] via-[#FAEDCD] to-[#6FFFE9]" />

      <div className="mb-6">
        <h3 className="text-2xl font-bold font-heading text-[#EAEAEA] mb-1">
          Send a Direct Message
        </h3>
        <p className="text-xs sm:text-sm text-[#9EABC0]">
          Have a question or opportunity? Leave a message below.
        </p>
      </div>

      {submitted ? (
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          className="text-center py-10 px-4"
        >
          <div className="w-16 h-16 rounded-2xl bg-[#6FFFE9]/15 border border-[#6FFFE9]/30 text-[#6FFFE9] flex items-center justify-center mx-auto mb-4 shadow-glow-aqua">
            <CheckCircle2 className="w-8 h-8" />
          </div>
          <h4 className="text-xl font-bold font-heading text-[#EAEAEA] mb-2">
            Message Prepared!
          </h4>
          <p className="text-sm text-[#9EABC0] max-w-md mx-auto mb-6 leading-relaxed">
            Thank you for reaching out, <span className="text-[#EAEAEA] font-semibold">{formData.name}</span>. You can also reach Sriram directly at{' '}
            <a
              href={`mailto:sriram.riya.r@gmail.com?subject=${encodeURIComponent(
                formData.subject
              )}&body=${encodeURIComponent(formData.message)}`}
              className="text-[#D4A373] hover:underline font-mono text-xs block mt-1.5 font-medium"
            >
              sriram.riya.r@gmail.com
            </a>
          </p>

          <button
            onClick={handleReset}
            className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl text-xs font-semibold bg-[#141D38] hover:bg-[#232E4F] text-[#EAEAEA] border border-[#232E4F] transition-colors shadow-soft"
          >
            <RefreshCw className="w-3.5 h-3.5 text-[#D4A373]" />
            <span>Send Another Message</span>
          </button>
        </motion.div>
      ) : (
        <form onSubmit={handleSubmit} noValidate className="space-y-4">
          {/* Quick template buttons */}
          <div className="flex flex-wrap items-center gap-2 mb-2">
            <span className="text-xs font-mono text-[#9EABC0] font-medium">Quick fill:</span>
            {quickTemplates.map((t, idx) => (
              <button
                type="button"
                key={idx}
                onClick={() => applyTemplate(t)}
                className="text-xs px-2.5 py-1 rounded-lg bg-[#141D38] hover:bg-[#232E4F] text-[#EAEAEA] hover:text-[#D4A373] border border-[#232E4F] hover:border-[#D4A373]/40 transition-colors shadow-soft"
              >
                {t.label}
              </button>
            ))}
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {/* Name */}
            <div>
              <label htmlFor="name" className="block text-xs font-mono uppercase tracking-wider text-[#EAEAEA] mb-1.5 font-semibold">
                Your Name <span className="text-[#D4A373]">*</span>
              </label>
              <input
                type="text"
                id="name"
                value={formData.name}
                onChange={(e) => {
                  setFormData({ ...formData, name: e.target.value });
                  if (errors.name) setErrors({ ...errors, name: '' });
                }}
                placeholder="e.g. John Doe"
                className={`w-full px-4 py-3 rounded-xl bg-[#141D38] border text-sm text-[#EAEAEA] placeholder-[#6E7D99] focus:outline-none focus:border-[#D4A373] transition-colors shadow-soft ${
                  errors.name ? 'border-rose-400 focus:border-rose-500' : 'border-[#232E4F]'
                }`}
              />
              {errors.name && (
                <p className="mt-1 text-xs text-rose-400 flex items-center gap-1">
                  <AlertCircle className="w-3 h-3" />
                  <span>{errors.name}</span>
                </p>
              )}
            </div>

            {/* Email */}
            <div>
              <label htmlFor="email" className="block text-xs font-mono uppercase tracking-wider text-[#EAEAEA] mb-1.5 font-semibold">
                Your Email <span className="text-[#D4A373]">*</span>
              </label>
              <input
                type="email"
                id="email"
                value={formData.email}
                onChange={(e) => {
                  setFormData({ ...formData, email: e.target.value });
                  if (errors.email) setErrors({ ...errors, email: '' });
                }}
                placeholder="e.g. john@example.com"
                className={`w-full px-4 py-3 rounded-xl bg-[#141D38] border text-sm text-[#EAEAEA] placeholder-[#6E7D99] focus:outline-none focus:border-[#D4A373] transition-colors shadow-soft ${
                  errors.email ? 'border-rose-400 focus:border-rose-500' : 'border-[#232E4F]'
                }`}
              />
              {errors.email && (
                <p className="mt-1 text-xs text-rose-400 flex items-center gap-1">
                  <AlertCircle className="w-3 h-3" />
                  <span>{errors.email}</span>
                </p>
              )}
            </div>
          </div>

          {/* Subject */}
          <div>
            <label htmlFor="subject" className="block text-xs font-mono uppercase tracking-wider text-[#EAEAEA] mb-1.5 font-semibold">
              Subject <span className="text-[#D4A373]">*</span>
            </label>
            <input
              type="text"
              id="subject"
              value={formData.subject}
              onChange={(e) => {
                setFormData({ ...formData, subject: e.target.value });
                if (errors.subject) setErrors({ ...errors, subject: '' });
              }}
              placeholder="e.g. Job Opportunity / Collaboration"
              className={`w-full px-4 py-3 rounded-xl bg-[#141D38] border text-sm text-[#EAEAEA] placeholder-[#6E7D99] focus:outline-none focus:border-[#D4A373] transition-colors shadow-soft ${
                errors.subject ? 'border-rose-400 focus:border-rose-500' : 'border-[#232E4F]'
              }`}
            />
            {errors.subject && (
              <p className="mt-1 text-xs text-rose-400 flex items-center gap-1">
                <AlertCircle className="w-3 h-3" />
                <span>{errors.subject}</span>
              </p>
            )}
          </div>

          {/* Message */}
          <div>
            <label htmlFor="message" className="block text-xs font-mono uppercase tracking-wider text-[#EAEAEA] mb-1.5 font-semibold">
              Message <span className="text-[#D4A373]">*</span>
            </label>
            <textarea
              id="message"
              rows={4}
              value={formData.message}
              onChange={(e) => {
                setFormData({ ...formData, message: e.target.value });
                if (errors.message) setErrors({ ...errors, message: '' });
              }}
              placeholder="Write your message here..."
              className={`w-full px-4 py-3 rounded-xl bg-[#141D38] border text-sm text-[#EAEAEA] placeholder-[#6E7D99] focus:outline-none focus:border-[#D4A373] transition-colors resize-none shadow-soft ${
                errors.message ? 'border-rose-400 focus:border-rose-500' : 'border-[#232E4F]'
              }`}
            />
            {errors.message && (
              <p className="mt-1 text-xs text-rose-400 flex items-center gap-1">
                <AlertCircle className="w-3 h-3" />
                <span>{errors.message}</span>
              </p>
            )}
          </div>

          {/* Submit Button */}
          <button
            type="submit"
            disabled={isSubmitting}
            className="w-full inline-flex items-center justify-center gap-2 py-3.5 px-6 rounded-xl font-bold text-sm tracking-wide bg-gradient-to-r from-[#D4A373] via-[#E4BD96] to-[#D4A373] hover:opacity-95 text-[#0B132B] shadow-glow-copper transition-all duration-300 hover:scale-[1.01] active:scale-[0.99] disabled:opacity-50"
          >
            {isSubmitting ? (
              <RefreshCw className="w-4 h-4 animate-spin text-[#0B132B]" />
            ) : (
              <Send className="w-4 h-4 text-[#0B132B]" />
            )}
            <span>{isSubmitting ? 'Sending...' : 'Send Message'}</span>
          </button>
        </form>
      )}
    </div>
  );
};
