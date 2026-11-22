import fs from 'node:fs';
import path from 'node:path';
let count=0;const failures=[];
const base='/'+(process.env.SITE_BASE_PATH||'').split('/').filter(Boolean).join('/')+((process.env.SITE_BASE_PATH||'').split('/').filter(Boolean).length?'/':'');
for(const file of ['dist/index.html','dist/club/index.html']){const html=fs.readFileSync(file,'utf8');for(const match of html.matchAll(/(?:src|href|data-video|data-poster)="(\/[^"#]*)"/g)){const url=match[1];if(!url.startsWith(base)){failures.push(`${file}: incorrect base ${url}`);continue}let target=path.join('dist',url.slice(base.length));if(url.endsWith('/'))target=path.join(target,'index.html');count++;if(!fs.existsSync(target))failures.push(`${file}: ${url}`)}if((html.match(/<h1\b/g)||[]).length!==1)failures.push(`${file}: expected one h1`);if(!html.includes('https://t.me/D3SKII'))failures.push(`${file}: missing Telegram`);if(/<video[^>]*autoplay/.test(html))failures.push(`${file}: unexpected autoplay`)}
if(failures.length){console.error(failures.join('\n'));process.exit(1)}console.log(`Passed: ${count} local references, page headings, Telegram links, no video autoplay.`);
