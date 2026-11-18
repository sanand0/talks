# Source map — AIPL Session 3, 15 Nov 2026

Checked on 18 Nov. URLs are sources and potential public-facing links, not proof each page appeared in this workshop. All source/media checks refer to the actual local device/repo context.

## Actual media and files

- Local video: ~/r2/media/2026-11-15-aipl-3.webm. ffprobe confirms 7515.976 seconds = 2h 05m 16s, AV1 1920×1200, Opus, 131,619,607 bytes. No subtitle stream listed. Public https://media.s-anand.net/2026-11-15-aipl-3.webm — HTTP 200, Accept-Ranges bytes; **wrong MIME audio/webm despite actual video**. Test real browser playback and seek in page build, not just HEAD.
- Local audio: ./2026-11-15-aipl-3.opus (9,255,129 bytes, 7515.9745 seconds). Release https://github.com/sanand0/talks/releases/download/talks/2026-11-15-aipl-3.opus — HTTP 200 after redirect. Do not extract temporary signed redirect URL as canonical.
- ./transcript.md: supplied complete 487 lines, 67,511 bytes; actual first speaker at 09:19 and farewell 122:59. Untimed continuation paragraphs and a few duplicated boundary snippets; inspect local video for precise seeks/quotations. Full source ~/Dropbox/notes/transcripts/2026-11-15 AIPL Session 3.md includes the Gemini transcription configuration (5 chunks, none failed); source call audio ~/Documents/calls/2026-11-15 AIPL Session 3.opus.
- ./comic-page.avif: existing 133,893-byte AVIF; **do not regenerate or alter**.
- ./chatgpt-chat-aipl-3-food-court-game.md (220 lines): source conversation on creation/deployment, first score analysis and excerpts. Private provenance https://chatgpt.com/c/6af92045-6224-83ec-8caf-b9f275823c59 — not a public source link. It contains earlier snapshot approximations; prefer fresh replay for precise figures.
- Page (future, not built here): https://talks.s-anand.net/2026-11-15-aipl-3/ .

## Trilogy and closest examples

- https://talks.s-anand.net/2026-10-18-aipl-when-do-you-let-ai-act/ — Session 1, local ../2026-10-18-aipl-when-do-you-let-ai-act/{prompts.md,index.html,story-context.md,research-notes.md,survey-analysis.md,links.md}.
- https://talks.s-anand.net/2026-10-25-aipl-2/ — Session 2, local ../2026-10-25-aipl-2/{prompts.md,index.html,story-context.md,research-notes.md,exercise-analysis.md,survey-analysis.md,links.md}. Includes original Ten Checks exercise, calibration chart, instruction leakage, and source-specific examples.
- https://talks.s-anand.net/2026-11-16-tds-ideation/ — next day's IITM faculty discussion; actual local ../2026-11-16-tds-ideation/{prompts.md,index.html,story-context.md,research-notes.md,links.md,transcript.md}. Use as design precedent and separate later evidence, not same video. All three talk pages and the GDPval visualization below returned HTTP 200 on 18 Nov.
- Talk catalog: ~/code/talks/README.md and config.json. Leave unchanged before page build/review.

## First-party game, survey and analysis (private raw sources)

- Workshop assessment https://exam.sanand.workers.dev/aipl-2026-11-15 — HTTP 404 in the 18 Nov HEAD check; historical exercise link, not currently confirmed accessible. Implementation ~/code/exam/src/exam-aipl-2026-11-15.js and q-food-court-discount.js, a-food-court-discount.js. Do not reveal answer keys, JWTs, enrolled identities, admin endpoints or screenshots containing login info.
- Game https://tds-network-games.sanand.workers.dev/realtime/food-court/ — HTTP 200 on 18 Nov HEAD, but inspect actual live availability at page-build time; use standalone explorable or video crop if access requires auth. Source ~/code/tds-network-games/src/realtime/games/food-court/{game.ts,model.ts}; DATA-SYNC.md, REALTIME-GAMES.md. Read only. Private session directories under .private/realtime/food-court/ (session-specific JSON, CSV, room logs) and .private/realtime/food-court/analysis/README.md (prototype model). The game's actual implementation, not prototype recommendations, is authoritative.
- Live survey https://forms.s-anand.net/aipl2026-s3/ — HTTP 530 in the 18 Nov HEAD check; source ~/code/liveform-data/aipl2026-s3/{form.yaml,responses.tsv}; results presenter-gated, do not embed private results or prompt users to submit to an old class. Use anonymized counts in survey-analysis.md. Plan contains questions not administered; no pre/post, A/B or capstone results.
- Comparisons: food-court-analysis.md uses the six 10–15 Nov sessions, excluding pilot; production sync command completed 18 Nov. All 173 room score checks passed. Keep raw data in ignored .private/ only.

## Session 1/2 callbacks, independent evidence

- [GDPval research](https://openai.com/index/gdpval/) and [author visualization](https://sanand0.github.io/datastories/gdpval/) (actual chart associated with Session 1, shown again in S3); beware current page may have changed.
- [Session 1 double-checking benchmark](https://sanand0.github.io/llmevals/double-checking/); [Session 2 confidence study](https://sanand0.github.io/llmevals/confidence-calibration/); [Ten Checks exercise](https://files.s-anand.net/temp/2026-10-25-aipl-session-2-human-checks.html). Existing talk notes give methodological and public/private boundaries.
- Noy & Zhang (2023): https://doi.org/10.1126/science.adh2586 .
- Dell'Acqua et al., jagged frontier (2023): https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 .
- Vaccaro et al. (2024), human-AI synergy meta-analysis: https://doi.org/10.1038/s41562-024-02024-1 .
- Calvano et al. (2020), algorithmic pricing interactions: https://doi.org/10.1257/aer.20190623 .
- Optional tax anecdote source for verification only: https://itat.gov.in/public/files/upload/1743164374-NKBaya-1-TO.pdf . Verify original case facts before any specific legal claim; no personal tax records or advice.

**Publication boundary:** the user requested source preparation only. No index.html, new images, build, deployment or catalog change was done. Claude can choose links/embeds after testing access; ensure the article never exposes student/email/room identities or private prompts, transcripts/chats, receipts or sensitive workflow/account screenshots.
