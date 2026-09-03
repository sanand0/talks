# Prompts

## Story, 3 Aug 2026

<!--
cd ~/code/talks/
dev.sh -- claude --dangerously-skip-permissions --model sonnet --effort medium
-->

Create a narrative story for the talk at 2026-09-03-convergence-jio-institute/

Go through the prompts.md in other recent files in this repo - you'll understand what I want. Implement along similar lines.

Here are the links I used.

1. Convergence 2026 — What's Left For Us
   survey.html
2. How I Make AI Outputs Verifiable
   verification-techniques.html
3. Contract Analysis
   https://sanand0.github.io/contractanalysis/
4. LLM Mental Math
   https://sanand0.github.io/llmevals/double-checking/
5. Who Gets the Final Call?
   autonomy-techniques.html
6. LLM Pricing
   https://sanand0.github.io/llmpricing/
7. SDLC — Past, Present, Future
   https://files.s-anand.net/pages/ai-sdlc-shift/

Feel free to use sub-agents as required, e.g. Opus for complex tasks or judgement (planning, analysis, storyline, etc.) and Haiku for simple execution.

<!-- Comic page: https://chatgpt.com/c/6a99402b-20bc-83ec-a4d6-0151de5a0f5c -->

---

Make it more prominently obvious that you need to click on the slides in survey.html (or use arrow keys to navigate). Maybe label it as a slide deck, too.
Modify the `*-techniques.html` files so that by default, they show all techniques, not just the first.
The contract analysis and double-checking embeds are too narrow. Don't make them side-by-side. Also, the iframes are not designed/formatted well. Fix that.
The "The verification tax" section is too long, undifferentiated text. How can we make this more engaging?
https://files.s-anand.net/pages/ai-sdlc-shift/ does not fit fully on the page and gets cut off at the bottom. Make sure that it does. Feel free to scale it downwards - since it's designed for a larger screen if you think that's the right approach.
Search online extensively for any additional links, references, etc. that will enhance the reading experience.
In the spirit of these revisions, if there are other revisions you feel should be made, find and fix those, too.

<!-- claude --resume 5e0f4af6-fc14-4544-ae9e-1bbc93eb8385 --dangerously-skip-permissions -->

## Survey data story, 3 Aug 2026

<!--
cd ~/code/talks/2026-09-03-convergence-jio-institute
dev.sh -- claude --dangerously-skip-permissions --model sonnet --effort medium
-->

Create a single page survey.html that visualizes data for Jio Institute, Convergence, 3 Sep 2026.

This shares insights from the categorized survey responses in survey.xlsx (which was created by chat-audience-profile.md).
Read chat-\*.md for context.

I would like the centerpiece to be a sand-dance - with each response rendered a single dot (rounded square or circle).
Depending on the context, they may smoothly move into clusters, or re-shape them into horizontal bar charts, or into grids, or into scatterplots, or any other visualization.
Depending on the context, the colors of the dots may vary.
Clicking on any dot should open a modal popup with full details of that response, visualized beautifully. Make sure the context is retained, i.e. if a dot is clicked from a chart that highlights specific colors and positions based on specific columns, those should be highlighted in the popup and be immediately visible on opening - otherwise there might be too much information to sort through.
But the crux of it is that every story element is based on the colors and position of these dots, and the smooth movement helps people understand the shifts and patterns.

I would also like the user to have some controls when viewing the sand-dance - e.g. to change the coloring or grouping - as appropriate.
What I mean is that I will be presenting live. When doing so, I might want to go off on a tangent, exploring the data with slightly different cuts.
I'd like to be able to do that without too many controls overwhelming the screen and still allowing me to return to the main story after a few detours.
URL hashes, back button, popping up an exploration chart in a modal and with close icon in popups, etc. might be possible approaches.

This is a data story. I'd like you to weave this together as a series of slides or as a scrollytelling story - your choice.
Each story element should have a title, BRIEFLY explain what the user is seeing in a way that conveys what they need to take away in SIMPLE language.
The categories and labels are too abstract and people can't relate to them. ("Adoption Posture"? What does THAT mean? "Barrier Breadth" isn't evocative - doesn't convey anything at a glance.) Rename these in a way that's intuitive, relatable, and evocative (i.e. just hearing / seeing the phrase should give them an instant feeling of what it means.)

The actual story is yours to craft. There are insights in chat-\*.md.
Prioritize story elements based on impact (what will be really useful for the majority of the audience) and surprise (what won't they likely know, what'll be memorable).
Create sand-dance visuals for each story element that are appropriate. Sometimes, just creating groups of dots is relevant.
Sometimes, creating a 2x2 (or m x n for small m,n) grid and moving dots into the appropriate cells is the best.
Sometimes, a horizontal bar chart with the dots moving into the bars is best.
The visual appearance and animation aesthetics do matter.

Use relevant skills.

Make sure I can jump from any part of the story to any other easily. I WILL be jumping around.
I will also take detours to other topics (e.g. techniques on I verify AI results, how AI can actually do creative work, etc.)
So this is more a collection of insights I will weave into my talk, rather than being the strict slides / storyline for my talk.
I will, likely begin with this and go ROUGHLY in sequence, but not entirely / necessarily.

Feel free to use Opus as a sub-agent for complex tasks, planning, analysis, storyline, etc., wherever you feel it is required.

---

A few revisions.

- My screen is 1920x1080 with the toolbar, statusbar, horizontal tab view, etc. taking up some space. Even at 200% zoom I feel the dots can be bigger and the labels can be bigger and there's too much space between the groups. Fill more space. Keep things centered. Make sure that at different zoom levels, the visual as well as the narrative on the left both look fine. Right now, at ~175% zoom is when things feel OK overall but the text and dots could certainly be larger. The labels, in particular, need to be quite prominent. In the beat 6 grid map, at that zoom, they cut off / overlap, though, so be careful.
- In One Wall, Two Walls, etc. move the labels nearer to the dots - below or above the counts.
- Beat 6 is too complex. Simplify - maybe avoid the grid?
- Start with You are the dataset.
  Then Beat 2 - So what's stopping you? and then move to Beat 3. Then Beat 1. Then Beat 5. Beat 6 (revised). Then the rest in any order - I might not use them.
- When I click "Explore a different cut" and make a selection using my keyboard, Esc doesn't close the popup.

There may be other similar issues. Find and fix.

--- <!-- steering -->

Make sure there's spacing BETWEEN the dots!

--- <!-- steering -->

Make sure associated labels are closer to the dots than the NEXT label! E.g. in bar charts.

<!-- claude --resume 0bf23b99-7bc6-4f4c-91d6-0464e620ff73 --dangerously-skip-permissions -->
