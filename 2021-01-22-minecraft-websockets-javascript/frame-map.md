# Frame map — Minecraft WebSockets JavaScript, 22 Jan 2021

Authentic frames extracted from https://youtu.be/bjanNXXwQbo. Timestamps are candidates chosen from the transcript; review the actual frame before treating captions as exact. These are frames of the original tutorial, not new gameplay illustrations.

| Seek | Frame | Candidate content |
|---|---|---|
| 00:00:34 | [slides/01-single-grass-block.webp](slides/01-single-grass-block.webp) | First relative-coordinate setblock in Minecraft |
| 00:04:08 | [slides/02-first-connection.webp](slides/02-first-connection.webp) | Minecraft WebSocket connection established |
| 00:09:35 | [slides/03-chat-event.webp](slides/03-chat-event.webp) | Listening to Minecraft PlayerMessage and decoding JSON |
| 00:13:48 | [slides/04-pyramid-loop.webp](slides/04-pyramid-loop.webp) | Writing the nested pyramid-generation loops |
| 00:20:05 | [slides/05-small-pyramid.webp](slides/05-small-pyramid.webp) | Successful small glowstone pyramid |
| 00:21:30 | [slides/06-large-pyramid.webp](slides/06-large-pyramid.webp) | A bigger glowstone pyramid in the game |
| 00:22:47 | [slides/07-speed-breaks-it.webp](slides/07-speed-breaks-it.webp) | Removing console logging makes commands overwhelm Minecraft |
| 00:25:20 | [slides/08-response-queue.webp](slides/08-response-queue.webp) | Command-response/backpressure logic |
| 00:31:40 | [slides/09-flow-controlled-pyramid.webp](slides/09-flow-controlled-pyramid.webp) | A larger pyramid after queue/backpressure fix |

## Frames added while building the story page (18 Oct 2026)

Extracted from the same YouTube upload with ffmpeg at the exact seek shown, scaled to 1280×720. `07-speed-breaks-it.webp` was confirmed to be the 22:47 frame (the unfinished ring).

| Seek | Frame | Content |
|---|---|---|
| 00:21:48 | [slides/10-pyramid-ten.webp](slides/10-pyramid-ten.webp) | Complete pyramid 10, built while `console.log(cmd)` was still in `send()` |
| 00:22:00 | [slides/11-the-log-line.webp](slides/11-the-log-line.webp) | VS Code line 48 `console.log(cmd)` above `socket.send(...)`, just before deletion |
| 00:24:30 | [slides/13-command-responses.webp](slides/13-command-responses.webp) | `commandResponse` messages: statusCode 0 “Block placed” and −2147352576 “The block couldn't be placed” |
| 00:32:48 | [slides/15-corner-errors.webp](slides/15-corner-errors.webp) | “x x x x” corner sketch in the editor; failed commands are all ring corners |
| 00:33:36 | [slides/16-complete-pyramid.webp](slides/16-complete-pyramid.webp) | Complete flow-controlled pyramid 10 in mid-air |

Caption correction: `06-large-pyramid.webp` (21:30) shows the chat history (pyramid 3, 5, `1-`), not a large pyramid.
