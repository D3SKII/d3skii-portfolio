# Project guidance

## Purpose
Build a personal portfolio with DJ work as the first release and independently shareable pages for future professional directions.

## Confirmed requirements
- Artist: D3SKII, Moscow. Homepage: event and commercial DJ work. Separate /club page: club DJ work.
- Selected style: large typography, expressive photography, restrained animation. Real source media is available in media/originals.
- Support portrait and landscape video, plus photography.
- User rejected generated portraits: do not generate or add AI portraits unless explicitly requested again.
- Future directions: sound engineering, event production, music production, sport.
- Give each published direction a stable URL and relevant contact action.

## Working rules
- Do not invent the artist name, experience, clients, reviews, venues, achievements or contact information.
- Keep unconfirmed ideas in PROJECT-BRIEF.md explicitly marked as proposals.
- Preserve original media. Store derivative exports separately.
- Keep rejected generated portraits out of the working tree and Git history.
- Never autoplay audible media. Respect reduced motion, keyboard navigation and mobile layouts.
- Load video on demand or near the viewport; provide poster images and preserve intended aspect ratios.
- Do not publish empty future sections.
- Keep copy, media metadata and direction-specific content separate from shared UI.

## Agent coordination
- The primary agent owns the brief, shared visual system, integration and release.
- Delegate bounded tasks with inputs, expected output and acceptance criteria.
- Assign one owner per edited file; independent review should report findings before changing another agent's files.
- Start parallel work only for independent tasks with sufficient inputs.
- Use currently available models; record actual selections rather than claiming unverified model capabilities or costs.

## Acceptance
Verify direct page URLs, mobile layouts, media controls, contact links, keyboard use and production build where applicable. Record checks and remaining limitations. Do not claim a check passed unless it ran.

## Implementation status
Buildless static HTML/CSS/JS in dist; page source generator scripts/build-pages.mjs. Run node scripts/build-pages.mjs after changing page content, node scripts/check.mjs to validate local references, node scripts/serve.mjs for localhost:4180. Primary publication: GitHub Pages via .github/workflows/pages.yml on remote main. SITE_BASE_PATH=/d3skii-portfolio/ in CI, empty for local root preview. Original videos use Git LFS; deploy only dist/. Keep old local Sites metadata separate.




