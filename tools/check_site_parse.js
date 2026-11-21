// Checks the practice site can parse every TOPICS row, question file, past paper and mock.
// Usage: node tools/check_site_parse.js .   (no web server needed)
const fs = require("fs"); const root = process.argv[2] || ".";
const src = fs.readFileSync(root + '/site/app.js', 'utf8');
const grab = (start, end) => src.slice(src.indexOf(start), src.indexOf(end));
eval(grab('function parseQuestions', '// split a worked answer'));
eval(grab('function parseMock', 'let timerHandle'));
// loadIndex logic, synchronous copy of the regexes
const t = fs.readFileSync(root + '/TOPICS.md', 'utf8'); const topics = [], mocks = [], CH = {}; let ch = 0;
for (const line of t.split('\n')) {
  const c = line.match(/^##\s+(Chapters?\s+[^:]+):\s*(.*)$/i); if (c) { ch++; CH[ch] = c[1] + ' · ' + c[2].replace(/\s*\(.*\)\s*$/, ''); }
  const m = line.match(/^\|\s*(\d+)\s*\|\s*\[([^\]]+)\]\((notes\/[^)]+)\)\s*\|[^|]*\|\s*\[([^\]]+)\]\((questions\/([^)]+)\.md)\)\s*\|\s*([^|]*)\|/);
  if (m) topics.push({ n: +m[1], title: m[2], notes: m[3], file: m[5], slug: m[6], ch });
  const k = line.match(/\[([^\]]*(?:Mock|Wrap|Final)[^\]]*)\]\(((mock|papers)\/([a-z0-9-]+)\.md)\)\s*(\(([^)]*)\))?/i);
  if (k && line.startsWith('|')) mocks.push({ title: k[1], file: k[2], id: k[4], paper: k[3] === 'papers' });
}
console.log('chapters', CH); console.log('topics', topics.length, 'by ch', [1,2,3,4].map(c => topics.filter(x => x.ch === c).length));
console.log('mocks', mocks.map(m => m.id + (m.paper ? '(paper)' : '')).join(' '));
let total = 0, tut = 0; const keys = new Set(); let dup = 0;
for (const tp of topics) {
  const p = parseQuestions(fs.readFileSync(root + '/' + tp.file, 'utf8'), tp);
  const nt = p.qs.filter(q => q.part === 'tut').length; total += p.qs.length; tut += nt;
  p.qs.forEach(q => { if (keys.has(q.key)) { dup++; console.log('DUP', q.key); } keys.add(q.key); if (!q.ans) console.log('NO ANSWER', q.key); });
  const types = p.qs.map(q => q.type).join(',');
  console.log(tp.n, tp.slug.padEnd(32), 'qs', p.qs.length, 'tut', nt, 'tags', p.qs.filter(q=>q.part==='tut').map(q => q.qid).join(' '));
}
console.log('TOTAL', total, 'tutorial+past', tut, 'dups', dup);
for (const m of mocks) {
  const r = parseMock(fs.readFileSync(root + '/' + m.file, 'utf8'));
  console.log('mock', m.id, 'qs', r.qs.map(q => q.id + ':' + q.marks + (q.ans ? '' : ' NOANS')).join(' '));
}
