import React, { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Bot,
  Send,
  Trash2,
  Minimize2,
} from 'lucide-react';
import { ChatMessage } from './ChatMessage';
import { SuggestedQuestions } from './SuggestedQuestions';
import { sendChatMessage } from '../../services/chatService';
import { portfolioData } from '../../data/portfolio';
import { ChatMessage as ChatMessageType } from '../../types';

interface ChatbotProps {
  isOpen: boolean;
  onToggle: () => void;
}

export const Chatbot: React.FC<ChatbotProps> = ({ isOpen, onToggle }) => {
  const [messages, setMessages] = useState<ChatMessageType[]>([
    {
      id: 'welcome',
      sender: 'bot',
      text: `Hello! I'm Sriram AI, your guide to Sriram R's portfolio.\n\nAsk me anything about his data science skills, Python experience, education, internships, or contact details!`,
      timestamp: new Date(),
    },
  ]);

  const [inputMessage, setInputMessage] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement | null>(null);
  const inputRef = useRef<HTMLInputElement | null>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    if (isOpen) {
      scrollToBottom();
      setTimeout(() => inputRef.current?.focus(), 150);
    }
  }, [isOpen, messages, isTyping]);

  const handleSendMessage = async (textToSend?: string) => {
    const text = (textToSend || inputMessage).trim();
    if (!text || isTyping) return;

    const userMsg: ChatMessageType = {
      id: `user-${Date.now()}`,
      sender: 'user',
      text,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMsg]);
    setInputMessage('');
    setIsTyping(true);

    try {
      const response = await sendChatMessage(text);
      const botMsg: ChatMessageType = {
        id: `bot-${Date.now()}`,
        sender: 'bot',
        text: response.text,
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, botMsg]);
    } catch (error) {
      const fallbackMsg: ChatMessageType = {
        id: `bot-err-${Date.now()}`,
        sender: 'bot',
        text: "I don't have that information in Sriram's portfolio yet.",
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, fallbackMsg]);
    } finally {
      setIsTyping(false);
    }
  };

  const handleClearChat = () => {
    setMessages([
      {
        id: `welcome-${Date.now()}`,
        sender: 'bot',
        text: `Chat cleared! What would you like to know about Sriram?`,
        timestamp: new Date(),
      },
    ]);
  };

  return (
    <>
      {/* Floating Chatbot Launch Button (Bottom-Right) */}
      <AnimatePresence>
        {!isOpen && (
          <motion.button
            initial={{ scale: 0, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0, opacity: 0 }}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={onToggle}
            className="fixed bottom-6 right-6 z-50 flex items-center gap-3 px-4 py-3 rounded-2xl bg-gradient-to-r from-[#D4A373] via-[#E4BD96] to-[#6FFFE9] hover:opacity-95 text-[#0B132B] font-bold text-sm shadow-glow-copper border border-[#FAEDCD]/30 group"
            aria-label="Open Sriram AI Chatbot"
          >
            {/* Pulsing beacon indicator */}
            <span className="relative flex h-3 w-3">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#0B132B] opacity-75" />
              <span className="relative inline-flex rounded-full h-3 w-3 bg-[#0B132B]" />
            </span>

            <div className="w-7 h-7 rounded-lg bg-[#0B132B]/20 flex items-center justify-center">
              <Bot className="w-5 h-5 text-[#0B132B] transition-transform group-hover:rotate-12" />
            </div>

            <div className="flex flex-col text-left">
              <span className="text-xs font-black tracking-wide leading-tight">Sriram AI</span>
              <span className="text-[10px] font-medium text-[#0B132B]/80 leading-tight">Ask me anything</span>
            </div>
          </motion.button>
        )}
      </AnimatePresence>

      {/* Expandable Chat Window */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, y: 30, scale: 0.92 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 30, scale: 0.92 }}
            transition={{ duration: 0.25, ease: 'easeOut' }}
            className="fixed bottom-4 right-4 sm:bottom-6 sm:right-6 z-50 w-[calc(100vw-2rem)] sm:w-[420px] h-[580px] max-h-[85vh] bg-[#0B132B]/98 rounded-3xl border border-[#D4A373]/35 shadow-2xl flex flex-col overflow-hidden"
          >
            {/* Top Accent Gradient Bar */}
            <div className="h-1.5 w-full bg-gradient-to-r from-[#D4A373] via-[#FAEDCD] to-[#6FFFE9]" />

            {/* Chatbot Header */}
            <div className="px-5 py-3.5 bg-[#1C2541]/90 border-b border-[#232E4F] flex items-center justify-between gap-2">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-[#D4A373] to-[#6FFFE9] flex items-center justify-center text-[#0B132B] shadow-glow-copper">
                  <Bot className="w-5 h-5" />
                </div>
                <div>
                  <div className="flex items-center gap-2">
                    <h4 className="font-heading font-bold text-sm text-[#EAEAEA]">
                      Sriram AI
                    </h4>
                    <span className="flex items-center gap-1 text-[10px] font-mono px-2 py-0.5 rounded-full bg-[#6FFFE9]/10 text-[#6FFFE9] border border-[#6FFFE9]/30">
                      <span className="w-1.5 h-1.5 rounded-full bg-[#6FFFE9] animate-pulse" />
                      Verified
                    </span>
                  </div>
                  <p className="text-[11px] text-[#9EABC0] font-mono">
                    Ask me about Sriram
                  </p>
                </div>
              </div>

              {/* Action Buttons */}
              <div className="flex items-center gap-1">
                <button
                  onClick={handleClearChat}
                  className="p-2 rounded-lg text-[#9EABC0] hover:text-rose-400 hover:bg-white/5 transition-colors"
                  title="Clear Chat"
                  aria-label="Clear Chat History"
                >
                  <Trash2 className="w-4 h-4" />
                </button>

                <button
                  onClick={onToggle}
                  className="p-2 rounded-lg text-[#9EABC0] hover:text-[#EAEAEA] hover:bg-white/5 transition-colors"
                  title="Minimize Chat"
                  aria-label="Minimize Chatbot"
                >
                  <Minimize2 className="w-4 h-4" />
                </button>
              </div>
            </div>

            {/* Chat Messages Container */}
            <div className="flex-1 overflow-y-auto p-4 space-y-2 custom-scrollbar bg-[#0B132B]">
              {messages.map((msg) => (
                <ChatMessage key={msg.id} message={msg} />
              ))}

              {/* Typing Indicator */}
              {isTyping && (
                <div className="flex items-center gap-2 text-xs text-[#9EABC0] p-2 bg-[#141D38] rounded-xl w-fit border border-[#232E4F]">
                  <div className="w-5 h-5 rounded-lg bg-[#D4A373]/20 text-[#D4A373] flex items-center justify-center">
                    <Bot className="w-3.5 h-3.5" />
                  </div>
                  <span className="font-mono text-[11px]">Sriram AI is thinking</span>
                  <div className="flex items-center gap-1">
                    <span className="w-1.5 h-1.5 rounded-full bg-[#D4A373] animate-bounce [animation-delay:-0.3s]" />
                    <span className="w-1.5 h-1.5 rounded-full bg-[#D4A373] animate-bounce [animation-delay:-0.15s]" />
                    <span className="w-1.5 h-1.5 rounded-full bg-[#D4A373] animate-bounce" />
                  </div>
                </div>
              )}

              {/* Suggested Questions Section */}
              <div className="pt-2">
                <SuggestedQuestions
                  questions={portfolioData.suggestedQuestions}
                  onSelectQuestion={(q) => handleSendMessage(q)}
                />
              </div>

              <div ref={messagesEndRef} />
            </div>

            {/* Input Bar */}
            <div className="p-3 bg-[#1C2541]/90 border-t border-[#232E4F]">
              <form
                onSubmit={(e) => {
                  e.preventDefault();
                  handleSendMessage();
                }}
                className="flex items-center gap-2"
              >
                <input
                  ref={inputRef}
                  type="text"
                  value={inputMessage}
                  onChange={(e) => setInputMessage(e.target.value)}
                  placeholder="Ask a question about Sriram..."
                  disabled={isTyping}
                  className="flex-1 px-3.5 py-2.5 rounded-xl bg-[#141D38] border border-[#232E4F] text-xs sm:text-sm text-[#EAEAEA] placeholder-[#6E7D99] focus:outline-none focus:border-[#D4A373] transition-colors shadow-soft"
                />
                <button
                  type="submit"
                  disabled={!inputMessage.trim() || isTyping}
                  className="p-2.5 rounded-xl bg-gradient-to-r from-[#D4A373] to-[#E4BD96] text-[#0B132B] font-bold transition-all disabled:opacity-40 shadow-glow-copper"
                  aria-label="Send Message"
                >
                  <Send className="w-4 h-4" />
                </button>
              </form>
              <div className="flex items-center justify-between text-[10px] text-[#9EABC0] font-mono mt-1.5 px-1">
                <span>Verified Data Only</span>
                <span className="text-[#6FFFE9] font-medium">0% Hallucination</span>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
};
