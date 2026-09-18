import React from 'react';
import { Sparkles } from 'lucide-react';

interface SuggestedQuestionsProps {
  questions: string[];
  onSelectQuestion: (question: string) => void;
}

export const SuggestedQuestions: React.FC<SuggestedQuestionsProps> = ({
  questions,
  onSelectQuestion,
}) => {
  return (
    <div className="py-2">
      <div className="flex items-center gap-1 text-[11px] font-mono text-[#D4A373] mb-2 px-1 font-semibold">
        <Sparkles className="w-3 h-3" />
        <span>Suggested Questions:</span>
      </div>
      <div className="flex flex-wrap gap-1.5 max-h-36 overflow-y-auto pr-1">
        {questions.map((q, idx) => (
          <button
            key={idx}
            onClick={() => onSelectQuestion(q)}
            className="text-left text-[11px] px-2.5 py-1.5 rounded-lg bg-[#141D38] hover:bg-[#232E4F] text-[#EAEAEA] hover:text-[#6FFFE9] border border-[#232E4F] hover:border-[#6FFFE9]/40 transition-all active:scale-95 shadow-soft"
          >
            {q}
          </button>
        ))}
      </div>
    </div>
  );
};
