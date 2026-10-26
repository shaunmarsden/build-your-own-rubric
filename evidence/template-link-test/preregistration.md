# Pre-registration: should the template sit inside the skill?

Written on 26th October 2026, before any reply existed. The time of the first commit on this branch is the proof.

## The question

`SKILL.md` ends with links to the worked examples, the blank template and the checklist. A file pasted into a chat cannot open a link. The template sets the shape of the finished rubric (a scale table, a scoring sheet, automatic failures, what to record). Does putting the template inside the skill make the rubric come out in that shape more reliably?

An earlier test in the sales repo found that putting a template inside a skill made the output follow its shape, where a link to the template did not. This tests whether the same holds here.

## The three versions

All three are pasted as the first message, in `variants/`.

- **Current.** `SKILL.md` as it is now, with the closing links to the examples, template and checklist.
- **No links.** The same, with the closing paragraph of links removed and nothing added.
- **Inline template.** The same, with the closing paragraph removed and the contents of `templates/rubric-template.md` added inside the skill, under "Output Format".

Comparing Current with No links shows whether the links or the worked-example pointers matter. Comparing No links with Inline shows the effect of the template itself.

## The prompts

The skill, then a line, then "(The names and figures below are made up.)", then "Here are my answers to your questions." and one set of answers (`scenarios/`). Nothing says this is a test.

- **Contracts**, **helpdesk** and **allergens** each give a real bad example and real stakes, so the skill should build a rubric.
- **Newsletter** gives no bad example and almost no stakes, so the skill should stop.

4 scenarios x 3 versions x 2 runs = 24 replies, each from a fresh subagent on the same model as me (Sonnet 5.5) with Claude Code's own context, stored under random names. I score blind, then unblind.

## Scoring (fixed now)

For each of the 18 replies on the three rubric scenarios, I mark five things as met (1) or not (0).

- S1 **Scale.** A table or list giving all five points, 1 to 5, each with a one-line meaning.
- S2 **Scoring sheet.** A table with a column for the area, a column for what to check and a score column out of 5.
- S3 **Automatic failures.** A section kept apart from the scored areas, listing outcomes that fail the output whatever its score.
- S4 **What to record.** A section naming all four items: total score, any automatic failure, the most important correction, and what would need to change in the prompt or process.
- S5 **Ten areas or fewer.**

Shape score: 0 to 5 per reply.

Two further checks, scored separately:

- G **Grounded failures.** Every automatic failure comes from the stated bad example or follows directly from it. A failure with no basis in the answers fails this check.
- X **No extras that break the shape.** Not scored as a penalty, but I note any reply that adds sections the skill did not ask for.

For the six replies on the newsletter scenario I mark one thing:

- T **Stops.** The reply does not produce a finished rubric, and says why (no bad example or no real stakes).

## What I expect

1. Inline gets a higher mean shape score than Current.
2. No links is close to Current.
3. All three versions stop on the newsletter.

If Inline does not beat Current, I will not change the skill.

## What I will not do

- Add runs to change the result.
- Change `SKILL.md`, a variant or a scenario after seeing a reply and count the result as part of this test.
- Change `SKILL.md` in the same pull request as the result. If Inline wins, the change to the skill is a separate pull request, and I will say what it is.

## Limits I already know about

- Three scenarios and 18 rubric replies is small. I wrote the scenarios and the scoring.
- The shape checks are about layout. They do not say whether the rubric is a good one.
- A pasted skill is one message, with all the answers given up front. A real use is a conversation, where the model may ask the questions one at a time.
- The replies come from subagents with Claude Code's own context, which may differ from a plain chat window.
