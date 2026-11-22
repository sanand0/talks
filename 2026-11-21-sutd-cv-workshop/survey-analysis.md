# SUTD CV workshop: survey analysis

Source: `~/code/liveform-data/sutd-cv-2026-11/{form.yaml,responses.tsv}`, inspected 22 Nov 2026. This is an anonymized aggregate, not the underlying restricted data.

## Method and denominators

168 answer events, 132 distinct respondent-question pairs, 17 distinct responding email identities across all questions. Keep the most recent event by timestamp for each (email, question) pair, matching editable survey semantics. The 7 core multiple-choice questions each have 15 final answers; the same 15 should not be assumed without comparing identities. Later questions have different denominators. No attendance denominator is available. The survey was sequential and not a repeated pre/post survey; changing the question cannot demonstrate a learning effect. Counts at closing can differ from the in-talk snapshots.

## Final counts

| Question | Final answers | Distribution |
|---|---:|---|
| After graduation | 15 | Work 9; Startup 4; Study 2; Break 0 |
| Primary hiring criterion | 15 | Portfolio 9; Actual outcomes 2; Inter-personal skills 2; Grades 0; Other 2 |
| Can a text-only LLM recognize encoded images? | 15 | No 10; Yes 5 |
| Can LLM-based models recognize what happens in video? | 15 | Yes 11; No 4 |
| Can LLM-based models count better than specialized models? | 15 | No 9; Yes 6 |
| Who should identify and optimize models? | 15 | Humans themselves, in most cases 11; Coding agents could do most 4 |
| What should you learn? | 15 | Verification 6; Finding problems 6; Execution 1; Doing data science 0; Other 2 |
| Workshop ideas (editable) | 6 | Gesture instrument 1; accessible game 1; second-hand product pricing 1; emotion identifier 1; music composer with hand tracking 1; a wild game 1 |
| Final submitted links | 10 | Ten unique HTTP(S) project URLs, one each; all ten opened on 22 Nov |
| Learning (free text) | 11 | See anonymous excerpts below |

Hiring "Other": all of the above; how one uses agents to do/speed up the job. Learning priorities "Other": keeping up; conveying human needs and emotions logically. The six recorded ideas are incomplete and editable, not a count of everyone who attempted an idea.

## The more useful comparisons

- **7 of 9 submitters who answered model selection/optimization thought people needed to identify/optimize models themselves.** The other 2 favored agents; one of the 10 submitters did not answer the question. This makes the hands-on exercise a compelling counterpoint, although we do not know whether each person's deployment actually involved model optimization or how their opinion changed after it.
- 7 of the 10 people who answered No to encoded images answered Yes to recognizing video. Both questions have 15 paired respondents: No→Yes 7, No→No 3, Yes→Yes 4, Yes→No 1. The inputs/questions differ (encoded text vs video images), so these are not contradictory opinions or a pre/post result.
- 5 of 9 submitters with a learning-priority answer chose finding problems, 2 verification, 1 execution, 1 keeping up (other). Not evidence that choosing an option caused a deployment.
- 9/15 preferred a portfolio and nobody chose grades or doing data science as their own primary learning priority. These were single-choice questions; zero selections is not a judgment that grades or all data science education are worthless.
- First submitted URL event was 15:41 SGT; last final link update 16:30 SGT. The transcript says the build break lasted approximately an hour and that many people were first-time gesture users. Ten submissions are not necessarily all the demos or proof that all features were fully working within an hour. Avoid reporting a submission rate against the unknown attendance.

## Anonymous learning excerpts

Use real wording, with ellipses explicitly marking omissions. These are student observations, not independently verified claims.

> I realised CV already has solutions for almost any kind of standard problems. The problem lies in finding an actual use case thats truly beneficial.

> I didn't know computer vision can be so easily vibe coded as well

> I didn't know it was possible to make a website in such a short time. I found out that user design is still a limitation with AI. Human won't always be logical, so I need to make a better design to communicate with human.

> Even free AI models accessible to public are able to integrate Computer Vision mostly effectively into a html/app file

> Now I see how AI has been getting more and more powerful being able to complete projects fully with almost no serious bugs. As I saw the project files, I realized that human verification is unfeasible, so we need to focus on governance of the creation process. […]

> Agents are a limitation to developing truly comerically viable software products

The last response is a useful counterweight: feasibility of a demo and commercial viability are not the same. Other respondents noted faster creation, available libraries/tools, model input limitations, LLM generation mechanics and prompting. No post-workshop quality or skill assessment was run.

## Reproduce

Read TSV as CSV with tab delimiter (not line splitting, as one answer includes a newline). Sort timestamp, keep last row per email/question, group by question and answer. For paired findings, join on email within the two question IDs. Never export email or response metadata.
