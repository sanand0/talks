# Story context — AIPL Session 3 (15 November 2026)

Prepared 18 Nov 2026 as input for Claude Code; this is **not the page**. Working story title: **Every agent did its job. Why did the business fail?** The strongest narrative is a discovery about joint outcomes, with a human story of experiments, unintended consequences, expert disagreement and an abandoned plan.

## Event and evidence

LeadUp Universe with E&ICT Academy, IIT Kanpur, online AI Product Leadership Module 5, third and final session with working professionals on Sunday 15 Nov. Earlier sessions: 18 Oct ("when to delegate"), 25 Oct ("how to verify cheaply"). This time, the challenge was what happens when **teams of humans and agents interact**, and whether optimizing an agent is sufficient to optimize a business. The instructor repeatedly recaps earlier data; use the earlier sessions' actual notes to distinguish evidence from anecdotes. Date in original prompts skeleton erroneously said 15 October; corrected to 15 November.

Sources: complete supplied 487-line transcript, existing comic, local and public video/audio, private companion conversation on game deployment and initial results, liveform question YAML and response TSV, fresh synced game event logs, public primary research. Source hierarchy: recording for what happened; authoritative game implementation and event replay for scores; survey responses for opinions; analysis for interpretations. Don't treat planned activities as completed.

## Suggested story (not a wireframe)

**Setup: the other side has AI.** The recap shows a pragmatic teacher making and testing commitments. He followed up on Session 1's "when should I stop the agent?" question, reporting three reasons: a stalled agent, clearly wrong direction, and running out of tokens. Treat this as his self-observation (no underlying stop-event diary supplied), not a validated decision rule. He reports an agent sent emails to 40 people despite an earlier do-not-send instruction. That is his account, not an independently inspected incident report. Screen recording of the Codex practice entrance test is the vivid setup: he eats an apple while the browser agent answers questions, uploads an essay and handles coding questions. It reportedly scored full marks. This illustrates the mismatch between assessment and capabilities in a permitted practice environment; not instructions on defeating proctoring or proof that hiring is doomed.

**Complication: a food court where nobody needs to be wrong.** Participants run simulated restaurants. They can ask agents, choose 12 monthly discounts, view their rivals' plans, negotiate via chat and update saved decisions. Everyone wants profit; the score combines 60% collective and 40% individual. In real markets discounts can attract new visitors but the model has a saturating shared demand effect; they also divert customers and reduce profit per sale. A participant asks how to see others, another struggles with connection after registration closes. These are not embarrassing mistakes: the tooling is part of system performance.

The live first run yielded seven rooms, 32 entrants (8 IITM email addresses, 4 with earlier TDS round experience). AIPL's combined checkpoint-mean team score 88.06 was lower than the comparison student sessions, ~92.51–95.57. Actual first/last checkpoint averages 91.81→85.95; six of seven rooms worsened. In one five-stall room r002, 95.21→79.69, 47 of 60 final cells at 20%. This is more dramatic than a leaderboard. The lesson isn't that players are foolish: choosing a discount in response to someone else's offer can help one's own outcome while collectively destroying profit. It is possible to have a well-understood individual objective and a badly aligned joint system. The mathematical game is a social dilemma, not proof of a specific Nash equilibrium or pricing behavior of LLM agents.

**Revelation: experience can help or hurt.** Participants offer richer views than a binary poll: Swati observes she made more profit without discounting in high-footfall months; Bhavya says her rank changed from 3 to 4 and coordination felt difficult; Mandar reflects on rigidity and openness; Chumki challenges transfer of domain experience (eating in a food court vs operating one) and says a banking or medical case might differ. Aishwarya predicts AI agents would be less selfish; this is a belief, not a fact. Sourabh and Lakshmi suggest numerical AI strength and human psychological/context strength. The instructor reveals 14/23 think students would do better; 19/23 think AI would do better, yet only 7/20 reported using AI. These four survey questions produced insufficient responses for the **planned** next half. At 82:22 the teacher ends the structured plan early: "I had planned this for a degree of statistical significance" and calls it a failed experiment. A threshold of 25 does not itself make A/B comparison significant. The audience does not deserve ridicule; connectivity, participation incentives, time, small sample, and instrument design are alternate explanations.

**Implication: verify the system, not the component.** The discussion turns to human-agent combinations, counterchecking expertise, and resilience. In the last Q&A the speaker says an agent read the game's underlying mechanics, wrote simulations and discovered rotating two 10%-discount stalls with the rest at 0% was nearly optimal for **team** profit. Recomputing the actual model confirms near-100 team score for fixed rotations (see food-court-analysis.md); it does not show that unsynchronized, individually optimizing agents would adopt or sustain this convention. Design at organizational level: shared outcome objective, controlled interfaces, common ground truth, negotiation or resource allocation, independent checks, escalation and fail-safe capabilities. Give youngsters + agents a chance to cross-question experts, but frame it as a testable suggestion, not a hiring prescription. Bhavya's outage story is the necessary robustness counterweight.

## Anchors in supplied transcript (minute:second from start of source recording)

| Time | Scene / use |
|---|---|
| 09:19–09:40 | Opening and recap begins; compare previous sessions |
| 09:40–29:53 | Recap: trust framing, stop button, bank ticket T040, secret word, accidental email anecdote; screen-share recording of Codex taking practice exam; Food Court instructions. The transcript has long un-timestamped speaker continuations; find exact clip offsets on local video rather than pretending each sentence is at 09:40. |
| 29:53–33:12 | Bhavya's guesswork question, score objective at 30:40, Akshika's discount memory question, game begins |
| 40:10–47:59 | Registration/connection problem and advice to use Talk pane; 50:33 Lakshmi asks what team means; 52:33 Swati asks if Save can be revised |
| 55:26–56:52 | Wrap-up/final negotiation directions then first participant debrief; the transcription jumps between actions. Check actual wall-clock recording, don't infer that final negotiation happened at exactly 55:26. |
| 56:52–58:25 | Aishwarya warns 20% all year; Sourabh describes ChatGPT's seasonal suggestions; survey shared |
| 59:59–62:06 | Maximum discounts, seasonality; Bhavya tries human + AI + peer coordination under time pressure, rank 3→4 |
| 63:53–68:59 | Swati tests removing discount in high demand; asks whether AI would outperform; Aishwarya, Sourabh, Lakshmi explain beliefs |
| 70:37–74:01 | Chumki challenges oversimplified student-professional comparison; speaker insists on binary question; response threshold; break |
| 76:09–82:22 | QR-code confusion and peer help, then instructor abandons planned second half |
| 82:22–89:39 | First-run results and contrasts with student sessions, participant explanations (do not equate duration/experience claims with controlled covariates) |
| 89:48–93:12 | Mandar reflects on rigidity, actual checkpoint decline, Akshika on prior assumptions and enthusiasm |
| 95:36–99:05 | Chumki's "other side of the counter" objection; banking/law as alternate domain |
| 99:05–107:48 | Self-reported agent use contrasted with lecturer's impressions of IITM; GDPval chart; tax anecdote; use public evidence and scope carefully |
| 107:48–109:21 | Bhavya points out AI outages and dependence; accept as self-report |
| 109:38–117:23 | Q&A on education, automation and hiring; speaker closes trilogy: verify human-agent system |
| 117:23–122:41 | Akshika asks whether humans would win on initial attempt; teacher explains source-code investigation and simulated alternating 10% strategy |
| 122:45–122:59 | Farewell; video ends ~125:16 |

## Quotes worth verifying in video

- "We aren't necessarily irrational. We may well be responding rationally to another person's discounts. And the net result may well be destroying the collective profit." (~90:34 onward)
- "We related to the example as a user, not as ... on the other side of the counter." (Chumki ~95:36)
- "The comparison is never human versus agent. The comparison is human plus agent versus human plus agent." (~before 107:48)
- "We really should be verifying the system, which is human-agent synthesis, and see what are the weak elements of the system. And a human may well be the weak element in this." (~before 117:23)
- Bhavya's felt drop in work quality during an AI outage: important counterpoint to treating higher AI usage as unqualified success (~107:48).

## Untold planned second half (optional context, clearly labeled)

The form contains questions on conflicting KPIs, accountability, dynamically interacting prices, bottlenecks, redundant same-model agents, AI-vs-human forgiveness, promoting autonomy, rush to the same advice, repeated review selection, capstone failures and permissions. They were **not answered or run in this session**, and the post-question was not administered. If the story introduces a synthetic reader challenge about one of these, explicitly label it as proposed/hypothetical, not workshop evidence. Do not conflate the workshop's goal with the full planned syllabus.

## Useful callbacks

Session 1: 18 of 33 checked everything; 21 of 33 selected high-impact decisions; expense-claim framing A/B tiny and inconclusive; instructor's first roll-call. Session 2: T040 gold-label disagreement despite claimed 100% confidence and second AI agreement; secret-word exercise; participant's two-day conversion and rug→table example. Verify names: Session 2 transcript names Priya; Session 3 recap says Rhea, so avoid falsely attributing the same project if identity cannot be resolved. Two previous workshops already have detailed public-safe stories and evidence files.

The 16 Nov IITM meeting returns to the same game, discusses student-professional differences, and includes participant feedback about having to scroll to reach chat while operating the game. This is useful context **after** Session 3, and could reinforce a UI/system hypothesis if clearly dated. Do not conflate two meetings' speakers or evidence.

**Creative latitude:** this is a set of verified anchors and editorial possibilities. The reader should understand the mechanism, the actual evidence and the uncertainties, not be walked through every transcript line. Choose a more arresting title or structure if the video suggests one.
