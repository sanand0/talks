# Primary sources, links and assets — Minecraft WebSockets JavaScript (January 2021)

## The selected recording and the actual author

- **Original tutorial video, and the ONLY embedded video:** https://youtu.be/bjanNXXwQbo (ID `bjanNXXwQbo`, 33:44). It is a **solo screen-recorded tutorial**, uploaded by Anand S on **22 January 2021**, not a conference keynote. Keep that genre and date straight.
- **Original blog post:** https://www.s-anand.net/blog/programming-minecraft-with-websockets/ — first published **20 Jan 2021**, later modified **2 Feb 2022**. Blog updated later, so don't assume every paragraph reflects exactly what was said in the 22 Jan video.
- **Original open-source tutorial:** https://github.com/sanand0/minecraft-websocket/tree/master/tutorial — genuine example source in `sources/`. In particular:
  - https://github.com/sanand0/minecraft-websocket/blob/master/tutorial/mineserver1.js — initial server and connection
  - https://github.com/sanand0/minecraft-websocket/blob/master/tutorial/mineserver2.js — subscribe/listen for PlayerMessage
  - https://github.com/sanand0/minecraft-websocket/blob/master/tutorial/mineserver3.js — block-setting pyramid
  - https://github.com/sanand0/minecraft-websocket/blob/master/tutorial/mineserver4.js — command responses and errors
  - https://github.com/sanand0/minecraft-websocket/blob/master/tutorial/mineserver5.js — bounded send queue with command acknowledgements
- **Source repository root:** https://github.com/sanand0/minecraft-websocket — undocumented Minecraft WebSocket (MCWSS) experimentation. The Python files are companion implementations, NOT the selected JavaScript recording.
- **Optional separate Python tutorial:** https://youtu.be/o-NgvtJZDcY — link as related material if valuable; do not load as alternative video or splice into the player.
- **Short later glowstone pyramid demonstration:** https://youtu.be/v3W2cjTWY-Y (published 2025) — later evidence of the enduring playful demo idea, not archival 2021 footage.

## Underlying protocol and historical environment

- **WebSocket (RFC 6455):** https://www.rfc-editor.org/rfc/rfc6455 — standard network transport; contrast it with the **undocumented** Minecraft MCWSS message shapes.
- **Node.js:** https://nodejs.org/ — 2021 tutorial uses Node 14, not necessarily the current Node module environment.
- **`ws` library:** https://github.com/websockets/ws — tutorial uses the Node package.
- **UUID:** https://www.rfc-editor.org/rfc/rfc4122 — historical reference for unique command request IDs; don't imply every unique number works (the speaker reports sequential numbers failing for some requests).
- **Minecraft Bedrock:** https://www.minecraft.net/en-us/about-minecraft — **2021 tested environment was Bedrock 1.16** per original blog; GitHub README later mentions 1.17/1.18. Not automatically transferable to Java Edition or current versions.
- **Minecraft commands docs (live, may change):** https://learn.microsoft.com/en-us/minecraft/creator/documents/commandsintroduction — use for context only, not as a claim about 2021 MCWSS support.
- **Why a fast producer overwhelms a consumer:** network flow control/backpressure explanation can be grounded in the specific source implementation; avoid presenting Minecraft's 2021 ~100 outstanding commands as an official universal documented quota.

## Assets on disk

- `2021-01-22-minecraft-websockets-javascript.opus` — 33:44 mono Opus, local only. Do not invent a GitHub release audio URL; link public release only after it exists.
- `transcript.md` — cleaned, cumulative, video-relative 2026 automated transcription. A verbatim quote requires checking original sound.
- `sources/` — preserved originals `mineserver1.js` through `mineserver5.js`, tutorial README, blog source, and manifest; quote only what actual code implements.
- `slides/*.webp` and `frame-map.md` — original screen-recording frames. Particularly the missing-pyramid bug ~22:08 and queue fix ~31:06. Don't present newly rendered world as an actual 2021 screenshot.
- `comic-page.avif` — **pending user input; not yet made**.

## Embedding and publication

Use ONLY the YouTube IFrame Player API for video; no local hosted WebM/MP4 or alternate YouTube. Show the original historical source and screenshots. 2021 API and server configuration (including disabling encrypted WebSockets) are potentially **insecure/outdated in 2026**; no invitation to run exposed/unencrypted websocket services. Any browser animation is an educational *simulation*, not connected to Minecraft.
