/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        midnight: {
          950: '#060B1A',
          900: '#0B132B', // Main Background
          850: '#141D38',
          800: '#1C2541', // Surface / Cards
          750: '#232E4F', // Hover / Nested surface
          700: '#2C395B',
          600: '#3A4B75',
        },
        copper: {
          50: '#FDF8F3',
          100: '#FBF0E6',
          200: '#F5DECA',
          300: '#ECCBAE',
          400: '#E4BD96',
          500: '#D4A373', // Primary Accent Copper
          600: '#C6905C',
          700: '#A97545',
          800: '#8A5D34',
          900: '#6D4726',
        },
        aquamarine: {
          300: '#A0FFF1',
          400: '#6FFFE9', // Primary Highlight Pop
          500: '#38EFD3',
          600: '#13CBB0',
        },
        paper: {
          100: '#FFFFFF',
          200: '#EAEAEA', // Text Primary
          300: '#CBD5E1',
          400: '#9EABC0', // Text Secondary
          500: '#6E7D99',
        }
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'Inter', 'system-ui', 'sans-serif'],
        heading: ['Outfit', '"Plus Jakarta Sans"', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
      animation: {
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'float': 'float 6s ease-in-out infinite',
        'float-slow': 'float 9s ease-in-out infinite',
        'glow-spin': 'glow-spin 12s linear infinite',
        'shimmer': 'shimmer 2.5s infinite',
        'gradient-x': 'gradient-x 8s ease infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-12px)' },
        },
        'glow-spin': {
          '0%': { transform: 'rotate(0deg)' },
          '100%': { transform: 'rotate(360deg)' },
        },
        shimmer: {
          '100%': { transform: 'translateX(100%)' },
        },
        'gradient-x': {
          '0%, 100%': {
            'background-size': '200% 200%',
            'background-position': 'left center'
          },
          '50%': {
            'background-size': '200% 200%',
            'background-position': 'right center'
          },
        }
      },
      boxShadow: {
        'soft': '0 2px 10px rgba(0, 0, 0, 0.25)',
        'card': '0 4px 20px -2px rgba(0, 0, 0, 0.4), 0 2px 6px -1px rgba(0, 0, 0, 0.2)',
        'card-hover': '0 12px 30px -4px rgba(212, 163, 115, 0.18), 0 4px 12px -2px rgba(0, 0, 0, 0.3)',
        'glow-copper': '0 0 25px -4px rgba(212, 163, 115, 0.35)',
        'glow-aqua': '0 0 25px -4px rgba(111, 255, 233, 0.35)',
      },
    },
  },
  plugins: [],
}
