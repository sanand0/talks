# Evidence shelf: SUTD computer vision workshop

21 Nov 2026, in-person at SUTD. The audio is 55:26.59; the hour of student work between 48:23 and 48:37 was omitted from the recording. The discussion after the break describes the aggregate experience, not a named project-by-project review. The applications, rather than the talk transcript alone, are the most useful material for the story.

## Ten projects: one webcam, many interfaces

Inspected on 22 Nov in a fresh desktop Chromium browser (1360×850; screenshots scaled to 1280px). All ten final URLs returned HTTP 200 and displayed their intended application, including FacePlay, which had been password-protected earlier. These are contemporary screenshots, not historical screen captures of the workshop. No webcam/microphone permission was granted. Camera-free paths were tested where possible; tracking accuracy, privacy claims, latency on real hardware, cross-browser behavior, and accessibility for actual target populations are **not** verified. Use `links.md` for URLs.

| Project | What the visitor can try / what is distinctive | What we actually observed |
|---|---|---|
| **Spellglass** | Open palm, pinch or swipe to cast distinct spells; combine two within three seconds; use two hands to move, rotate, charge and fling a 3D orb. Even the camera-free preview is fun. It turns perception into an expressive vocabulary, not just a classifier. | Clicked Preview charge and Preview toward; rendered a bright golden orb animation. `active-spellglass.webp` is a better lead image than `shot-spellglass.webp`. Live gesture recognition not tested. |
| **Air Chemistry Lab** | Lunar outpost with virtual reagents, pH indicators, gas formation and an unknown sample. Pinch to pick up a reagent and select a vessel; mouse/touch/keyboard are alternatives. Gestures are the means, the chemistry mission is the goal. | Entered the workbench: vinegar, water and baking soda, three labeled cups, mission log. `active-chemistry.webp` shows the actual workbench. `shot-chemistry.webp` shows the briefing. |
| **Dustline — Gesture Ride** | Both hands visible to ride, tilt head to steer, raise either thumb to turn 90°. A motorbike controlled by the body. | Open desert 3D scene and controls rendered, waiting for camera. `shot-dustline.webp`. Did not ride. |
| **Pulse Slash** | Rhythm game: slash pink/blue blocks with left/right arms in time to music. Includes difficulty, a camera arm-swing test and adjustable camera-delay compensation; latest form update says custom YouTube songs are supported. | Title/menu rendered. The keyboard play button was disabled while video was loading, so gameplay and custom song playback not verified. `shot-pulse.webp`. Latency is a design problem the app explicitly exposes. |
| **Airwave Studio** | Play piano by pinching inside note lanes, guitar by chord/strum, flute by breath (microphone); piano has click/tap/keyboard controls. A great example of mapping continuous motion or sound to intentional discrete events. | Pressed A: UI updated LAST PLAYED to C4. `active-airwave.webp` shows this state; audio output muted during test. No camera or microphone test. |
| **HandSymphony** | Rather than playing individual keys, conduct a soundscape: hand height changes brightness, swaying changes energy, finger taps play notes, and openness shapes density. Pointer fallback, several genres and explanatory glossary. | Started pointer mode and moved pointer; gesture Sway, chord Dm, tempo 63 bpm, energy 32% shown. `active-symphony.webp`. Real music playback not assessed. Contrast with Airwave: discrete key events vs control of musical expression. |
| **FacePlay Arcade** | Gentle games designed for people who might not use conventional controls: turn head to select, open mouth to confirm/collect stars, blink to jump. No timer in Star Garden; adjustment of sensitivity and neutral calibration. | Three choices and controls rendered without login. Camera attempted to start and correctly reported no device in this browser. `shot-netlify.webp`. Do not claim independently validated accessibility or fitness for a particular disability. |
| **Mochi's Mood-Ring Arcade** | Virtual cat reacts to facial movements; offers a keyboard alternative. A more personal/fun application of face tracking. | Landing with pet and camera/keyboard choices rendered. Keyboard launch was not exercised successfully in this test. `shot-mochi.webp`. Don't imply face movements establish internal feelings. |
| **GestureLens** | Collect 24 common hand gestures; tracks 21 landmarks/hand and uses heuristic recognition. A feedback loop for learning what the camera can recognize. | Appeared with recognition UI, gallery and caveats. `shot-gesturelens.webp`. It explicitly says it is not a sign-language interpreter; meanings vary across cultures. |
| **Emotion Tracker** | Neutral-face calibration, teach individual classes, adjustable smoothing/sensitivity, expression timeline and action-unit option. The page includes unusually rich design notes about an earlier model's failures and candidate remedies. | UI and design notes rendered; models still downloading at capture, camera off. `shot-emotion.webp`. Particularly valuable as an example of iteration: according to its own notes, initial version missed subtle expressions and the newer version combines a different model, landmarks, calibration and decision rules. Treat this as developer-reported, not independently proven performance. Facial expressions aren't reliable labels of inner emotions. |

The strongest opening visuals are Spellglass's orb, the virtual chemistry workbench, Dustline's desert and FacePlay's colorful games. Then show the musical pair and the two recognition-focused apps as contrasts. Build a compact gallery of **all ten**, with bigger excerpts for 3–4 that strengthen the story. A camera-free preview is not evidence of camera accuracy.

Useful second-order design lessons:

- The CV pipeline can be similar across projects, but the interface is not: a pinch might cast a spell, pick up a chemical or trigger a piano note. The mapping from a recognized gesture to the action matters more than the detector alone.
- Continuous controls (sway/position → music) need smoothing and calibration; discrete controls (blink → jump, pinch → spell) need debounce, thresholds and undo/recovery. These are explanatory design considerations, not verified implementation details.
- In a rhythm game, end-to-end delay is part of correctness. For an accessible game, ease of interaction is the point; evaluate with the intended users, not just the person who built it.
- Camera-free controls are useful for testing, noisy lighting, limited hardware and helping people understand the experience without granting camera access. Do not ask an audience to grant camera or mic access automatically.

## What else was found

The browser history shows that I tried my Lightwell Camera Studio in a browser call and tested the extension during the break. The repo was already started on 20 Nov; 21 Nov commits at 15:44, 15:54, 16:12 and 16:15 add layer effects, refresh call code and add hand inputs/status. `shot-lightwell.webp` is the existing documentation screenshot with the built-in sample (not a recording from the workshop). It is an optional instructor-side example of camera as both input and composited output. This is experimental, not evidence all video call services work.

Two earlier form entries were not extra distinct projects: the private workspace artifact was later replaced by Spellglass's public link; the local Windows HTML file was replaced by Dustline's public URL. No separate evidence of any additional unnamed student demos appeared in the 21 Nov browser-history window. Do not imply these ten were the full set of things built. If further student links/photos are provided, add them with distinct provenance.

## Teaching evidence / fact-checks

**Tiny images.** The current base64-image-probe page shows seven 8×8 black-and-white images, four shapes and three random noise patterns; five text/encoded formats; four models, one tested at two effort settings. No tools/no vision; output pixel grids, not just guessing a category. Every pixel has to match, or all colors inverted (counted as decoded). GPT-6 Sol reconstructed 7/7 PNG grids under that rule, including four with colors swapped; Sonnet 5.5 5/7; GPT-6 Luna high effort 2/7; Gemini Flash low effort 0/7. With reasoning off Luna decoded none of the encoded files in a four-image subset. Don't frame as ordinary photographs, general-purpose binary decoding, or cheap/practical image recognition. See `shot-base64.webp`. The raw prompts and results are linked in links.md.

**Video.** The NFL page is explicitly marked internal — do not publish its link, clip, numerical results or screenshot. The rocket-launch probe sampled James Webb launch frames every 5 seconds over 5½ minutes; 19 questions per frame, 1,251 scored answers. Its own conclusion: good at information printed on screen, not yet reliable for physical events. If making broader claims, read the caveats. `shot-rocket.webp`. Content DNA Analyzer is a separate sample workflow: analyzing videos against content/retention parameters. Use `shot-dna.webp`, or capture a specific public example after selecting it; do not suggest the analysis guarantees marketing impact.

**Counting.** The live results page on 22 Nov has 54 LLM answers + 30 specialist predictions on six images, nine LLMs and five specialists. CountGD 3.7% mean count deviation, best vision LLM (Gemini Flash) 4.5%. Of 12 LLM answers with stated confidence >=90%, 8 were wrong. Three images are FSC-147 training split, three validation/test; FamNet receives exemplar inputs. This is a tiny mixed-split comparison, not a causal ranking of LLMs versus specialists. The transcript's informal ranking/model names don't match the current page. Prefer observed source and separate oral recollection. `shot-count.webp` is the overview; for story visuals use the actual deviations/calibration chart from the source.

**Push-ups.** Current dashboard: ensemble found 230 rep instances over four sessions, scores 71 → 78 → 87 → 67 (7, 8, 11, 15 Nov). Initially 95% of reps had sag; last session 98% had pike. Depth 100/100 across all; body line 39/100 weakest. Scores come from a specified composite rubric and model-derived angles, not authoritative coaching diagnoses. The fourth session prevents the oversimplification "AI coaching steadily improved performance." Inspect the actual prompts and model comparisons. `shot-pushup.webp` shows the 11 Nov deep link and current scores.

**Pottery and Proton Party.** Pottery supports shaping a vessel with both hands: open hands select height, fists moving apart/together modify radius. Mouse alternative is available. Proton Party uses a collaborative squeeze/release to throw protons; current screenshot has zero players, not a replay of the class. Do not embed a stale room QR as a way to join. `shot-pottery.webp`, `shot-protons.webp`.

## Useful exact quotes and recording offsets

Use the transcript as the source; do not turn the following short cues into a verbatim quote unless the words match. The two-part audio is continuous edited recording time, not the wall clock. 

- ~01:23 opening: "you're going to be doing the work, not me."
- ~01:23–before 19:32: "before you try and learn something, write down what you think you know, and then go ahead, test it out." (Locate exact audio offset before making a timestamp link.)
- 36:30: "I didn't really need to know what library to use or what technique to use. It can figure that out."
- 43:03: "A big part of what enables it is, are you giving the agent the right kind of tools?"
- 48:23 (then break): "I'm also going to build something. Why should you have all the fun?"
- 49:16: "In what, less than an hour, at least well more than half a dozen of you, you've created something that works" (excerpt; the rest continues in transcript).
- 49:41: "That is not your differentiation."
- 50:15: "delegate everything to agents. Let them do what they can do well. What they can't do well is the space we play in."
- 52:57: "What seems to be emerging is governance. How do I set up stuff so that agents can do the verification?"
- 54:20: ask what surprised you, what is no longer useful, or what limitation is worth building around. Make the reader answer this question too.

The claim that execution matters most is the instructor's judgement, not a measured ranking of hiring effectiveness. End the story with action, not a sweeping prediction about all future AI.
