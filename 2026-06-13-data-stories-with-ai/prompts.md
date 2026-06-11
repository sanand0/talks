# Prompts

## Initial draft, 07 Jun 2026

<!--
cd /home/sanand/code/talks/2026-06-13-data-stories-with-ai
dev.sh -p ~/code/
claude --dangerously-skip-permissions --model claude-opus --effort medium
-->


Create a `techniques.html` that will fetch and render `techniques.jsonl`.

Read `claude-chat.md` to understand the context and how `techniques.jsonl` was generated.

I want `techniques.html` to fit on a single page and show all the techniques on a scatter plot with impact on the Y axis and ease on the X axis.

Ensure that the points are spread out. The values are subjective - you can edit the impact and ease values to make them distinguishable, as long as you are convinced that the relative ordering is correct.

Label the quadrants with large light/subtle text in the background. Top-left is "Moonshots". Top-right is "Quick Wins". Bottom-left is "Time sinks". Bottom-right is "Small wins".

Color them based on the "stage". Add a legend showing which color corresponds to which stage. The legend should be styled like a workflow. Hovering on a legend should highlight the points of that stage and fade out the others. Clicking on a legend item should persist the highlight. Clicking on multiple legend items should allow selecting multiple stages. Allow clearing the selection to show all points again.

If possible, label the points with the technique name in a way that avoids label overlap. Move labels intelligently to ensure they do not overlap. It's OK not to show some labels if there are too many points, but show as many as possible without overlap. The labels should be styled nicely and be easy to read.

When hovering over a point, show a tooltip with the technique name, tagline, and stage (colored). The tooltip should be styled nicely and be easy to read.

When brushing a region, open a popup that shows the selected techniques, mentioning their name, tagline, and stage (colored). The popup should be scrollable if there are many techniques.

When clicking on a point or the technique in the popup, open a sidebar that shows the full details of the technique, including the description and example. The sidebar should be well-designed and easy to read. For links to files, point to GitHub. For example, `~/code/journalists/prompts.md` -> `https://github.com/sanand0/journalists/blob/main/prompts.md`. Where possible, link to specific sections as a permalink, for example: `https://github.com/sanand0/journalists/blob/cdfa61e0a1854b56c1aa83d283f7286512186147/prompts.md#statnostics-2-mar-2026` for the `source-sweep` technique where we mention "In the section 'Statnostics, 2 Mar 2026 -> Find stories via Codex'...".

Preserve the state of the brushing, legend selection, and sidebar selection in the URL so that it can be shared. Use #?key=value&key=value...

Ensure that the colors look good on dark AND light mode, the app can be used on mobile AND desktop, and the layout is responsive.

---

Change the title to "Data Stories with AI - Technique Atlas". Drop the subtitle.
Remove the .lcap "Find → … → Orchestrate" -- this is obvious.

On hover and brush, also show "Why it works".

Go through the content in "techniques.jsonl". Will a layman understand it, standalone? For example, "A constrained format that travels on social and survives print" isn't as clear as "A fixed format can be repeatedly used on print and social media as a recurring series". Revise the tagline, move, why, try_it, watch_for and examples.context in `techniques.jsonl` where required to make it simple and clear for a layman.

Find more examples of as many techniques as you can from ~/code/journalists/ or ~/code/datastories/ (or ~/Documents/chatgpt/ or ~/Documents/claude/ - which are dumps of some of my older chats).
Include them only if they're apt and absolutely spot-on as an exemplar for that technique - and make sure that comes through when you write the "context".

Also, create a "Tour" that guides the user through the techniques. Don't pick all the techniques. Just a sequence of the 1-2 most powerful techniques for each stage. Make sure you show progress along the tour, allow the user to use the keyboard to navigate without clashing with other keyboard usage (e.g. for scrolling), make the next / previous buttons easy to see and click, ensure that it will look and work well on mobile.

<!-- claude --resume eb5216a1-8b16-4bcd-9255-81822ca5bf7a --dangerously-skip-permissions -->
