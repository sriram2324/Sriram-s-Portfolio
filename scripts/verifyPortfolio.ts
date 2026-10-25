import { sendChatMessage } from '../src/services/chatService';
import { portfolioData } from '../src/data/portfolio';
import fs from 'fs';
import path from 'path';

async function runTests() {
  console.log('=== RUNNING PORTFOLIO AUTOMATED VERIFICATION SUITE ===\n');

  let passed = 0;
  let total = 0;

  function assert(condition: boolean, message: string) {
    total++;
    if (condition) {
      console.log(`✅ PASS: ${message}`);
      passed++;
    } else {
      console.error(`❌ FAIL: ${message}`);
    }
  }

  // 1. Check data integrity
  assert(portfolioData.personal.name === 'Sriram R', 'Personal name is Sriram R');
  assert(portfolioData.personal.email === 'sriram.riya.r@gmail.com', 'Email is sriram.riya.r@gmail.com');
  assert(portfolioData.personal.phone === '+91-8608850397', 'Phone is +91-8608850397');
  assert(portfolioData.personal.location.includes('Bangalore'), 'Location includes Bangalore');

  // 2. Check education
  const beCse = portfolioData.education.find((e) => e.id === 'be-cse');
  assert(!!(beCse && beCse.gradeValue === '7.8'), 'BE CSE GPA is verified as 7.8');
  assert(!!(beCse && beCse.institution.includes('Paavai Engineering College')), 'College is Paavai Engineering College');

  // 3. Check internships
  assert(portfolioData.experiences.length === 4, 'Has exactly 4 verified experience entries');
  const gdsc = portfolioData.experiences.find((e) => e.id === 'gdsc-participant');
  assert(!!(gdsc && gdsc.technologies && gdsc.technologies.includes('Google Colaboratory')), 'GDSC includes Google Colaboratory');

  // 4. Check Chatbot responses for suggested questions
  const q1 = await sendChatMessage('Who is Sriram?');
  assert(q1.text.includes('Sriram R is a dynamic data science professional'), 'Chatbot answers "Who is Sriram?" accurately');

  const q2 = await sendChatMessage("What are Sriram's skills?");
  assert(q2.text.includes('Python') && q2.text.includes('SQL Databases'), 'Chatbot lists skills');

  const q3 = await sendChatMessage('Tell me about his experience.');
  assert(q3.text.includes('Live Stream Technologies') && q3.text.includes('Corizo'), 'Chatbot lists internships');

  const q4 = await sendChatMessage('What is his GPA?');
  assert(q4.text.includes('7.8') && q4.text.includes('Paavai'), 'Chatbot answers GPA & college');

  const q5 = await sendChatMessage('Where can I find his GitHub?');
  assert(q5.text.includes('sriram2324'), 'Chatbot provides new GitHub username/link');

  const q6 = await sendChatMessage('What is his LinkedIn?');
  assert(q6.text.includes('sriramraja22'), 'Chatbot provides new LinkedIn URL');

  // 5. Test strict refusal on unknown/invented queries
  const qOut = await sendChatMessage('Does Sriram have 10 years experience in Quantum Robotics at NASA?');
  assert(
    qOut.text === "I don't have that information in Sriram's portfolio yet.",
    'Chatbot strictly refuses fabricated/unknown questions with exact prompt requirement'
  );

  // 6. Check resume PDF asset
  const resumeExists = fs.existsSync(path.resolve('public/resume.pdf'));
  assert(resumeExists, 'public/resume.pdf file exists and is downloadable');

  // 7. Check Project Dashboard requirements
  assert(portfolioData.projects.length === 9, 'Projects list contains exactly 9 unique projects');

  const featuredProjects = portfolioData.projects.filter((p) => p.featured);
  assert(featuredProjects.length === 3, 'Exactly 3 projects are marked as featured');

  const expectedIds = [
    'personal-finance-dashboard',
    'retail-sales-analytics',
    'customer-churn-prediction',
    'ecommerce-sales-analytics',
    'data-quality-pipeline',
    'python-api-pipeline',
    'business-report-automation',
    'student-performance-analytics',
    'news-sentiment-intelligence',
  ];

  for (const id of expectedIds) {
    const proj = portfolioData.projects.find((p) => p.id === id);
    assert(!!proj, `Project '${id}' is defined in portfolioData`);
    assert(!!(proj && proj.title && proj.description && proj.category), `Project '${id}' has complete metadata`);
    assert(!!(proj && proj.technologies.length > 0), `Project '${id}' has technology badges`);
  }

  const qProj = await sendChatMessage('Tell me about your projects.');
  assert(
    qProj.text.includes('Personal Finance & Expense Intelligence Dashboard') &&
      qProj.text.includes('Retail Sales Analytics with SQL') &&
      qProj.text.includes('Customer Churn Prediction') &&
      qProj.text.includes('E-Commerce Sales Analytics'),
    'Chatbot accurately describes the portfolio projects'
  );

  console.log(`\n=== RESULTS: ${passed}/${total} TESTS PASSED ===\n`);
  if (passed === total) {
    process.exit(0);
  } else {
    process.exit(1);
  }
}

runTests();
