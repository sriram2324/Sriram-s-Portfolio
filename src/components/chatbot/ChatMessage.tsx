import React from 'react';
import { Bot, User } from 'lucide-react';
import { ChatMessage as ChatMessageType } from '../../types';

interface ChatMessageProps {
  message: ChatMessageType;
}

export const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
  const isBot = message.sender === 'bot';

  return (
    <div className={`flex items-start gap-2.5 mb-3.5 ${isBot ? 'justify-start' : 'justify-end'}`}>
      {isBot && (
        <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-[#D4A373] to-[#6FFFE9] flex items-center justify-center text-[#0B132B] flex-shrink-0 mt-0.5 shadow-soft">
          <Bot className="w-4 h-4" />
        </div>
      )}

      <div
        className={`max-w-[82%] sm:max-w-[78%] rounded-2xl px-4 py-3 text-xs sm:text-sm leading-relaxed ${
          isBot
            ? 'bg-[#1C2541] text-[#EAEAEA] border border-[#232E4F] shadow-soft'
            : 'bg-gradient-to-r from-[#D4A373] to-[#E4BD96] text-[#0B132B] font-semibold shadow-glow-copper'
        }`}
      >
        <div className="whitespace-pre-wrap">{message.text}</div>
        <div
          className={`text-[10px] font-mono mt-1 ${
            isBot ? 'text-[#9EABC0]' : 'text-[#0B132B]/75'
          }`}
        >
          {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
        </div>
      </div>

      {!isBot && (
        <div className="w-8 h-8 rounded-xl bg-[#141D38] border border-[#232E4F] flex items-center justify-center text-[#EAEAEA] flex-shrink-0 mt-0.5 shadow-soft">
          <User className="w-4 h-4" />
        </div>
      )}
    </div>
  );
};
