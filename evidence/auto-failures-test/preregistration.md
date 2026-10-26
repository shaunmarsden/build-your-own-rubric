# Pre-registration: can a rule stop the skill inventing automatic failures?

Written on 26th October 2026, before any reply existed. The time of the first commit on this branch is the proof.

## The question

In the [template test](../template-link-test/results.md), all 18 rubric replies, in every version, listed at least one automatic failure that had no basis in the stated bad example (for example "says the contract is safe to sign"). The repository's checklist says automatic failures should come from a real bad example. The skill only says that drawing from the bad example "helps". Does a sentence that makes it a rule change what the replies do?

## The two versions

Both are the skill with the template inside it, as in the pull request that puts the template in. They are in `variants/`.

- **Baseline.** Step 3 ends: "Drawing from the bad example gathered above helps here: what specifically made it unacceptable, not merely mediocre?"
- **With rule.** That sentence is replaced by: "Take each automatic failure from the bad example, or from a failure that follows directly from it, such as the same mistake in a nearby field. Do not add a failure that nobody has described. If you think another outcome might deserve to be an automatic failure, put it in a scored area, or ask the person whether it has ever happened."

Nothing else differs.

## The prompts

The skill, a line, "(The names and figures below are made up.)", "Here are my answers to your questions." and one set of answers (`scenarios/`). Nothing says this is a test.

- **Invoices**, **applicants** and **tenancy** each give a real bad example and real stakes, so the skill should build a rubric.
- **Quiz** gives no bad example and no stakes, so the skill should stop.

3 rubric scenarios x 2 versions x 3 runs = 18, plus 1 stop scenario x 2 versions x 2 runs = 4. 22 replies, each from a fresh subagent on the same model as me (Sonnet 5.5) with Claude Code's own context, stored under random names. I score blind, then unblind.

## Scoring (fixed now)

For each of the 18 rubric replies, I list every automatic failure and mark each one:

- **Grounded**: it is the same mistake as the bad example, or a close variant (the same action, the same field, or the same consequence), or the person described it.
- **Ungrounded**: it is a general safety rule or a different kind of mistake that nothing in the answers describes.

Main measure: **ungrounded automatic failures per reply**, by version.

Other measures:

- **F** The rubric would fail the bad example. At least one listed failure is one that the bad example triggers. It must be 1 in every reply, or the rule has cost something real.
- **N** The number of automatic failures listed.
- **Shape** The five checks from the template test: S1 a five-point scale with meanings, S2 the scoring sheet as a table with area, what to check and score columns, S3 a separate automatic-failures section, S4 a "what to record" section with all four items, S5 ten areas or fewer. The rule must not break these.
- **Questions** Whether the reply asks the person whether a possible failure has ever happened. Noted, not scored.
- **T** For the four quiz replies: the reply stops and builds no rubric.

## What I expect

1. With rule has fewer ungrounded failures per reply than Baseline, by at least half.
2. F stays at 1 in every reply, and shape stays at 5 of 5.
3. Both versions stop on the quiz.

If the rule does not cut ungrounded failures, I will not add it to the skill. If it cuts them but F or shape drops, I will not add it either.

## What I will not do

- Add runs to change the result.
- Change a version or scenario after seeing a reply and count it in this test.
- Put the rule into `SKILL.md` in the same pull request as the result. If it works, that is a separate pull request.

## Limits I already know about

- Eighteen rubric replies on three scenarios I wrote is small. I judge "grounded" myself, and "close variant" involves judgement.
- A rubric with fewer automatic failures is not necessarily a better one. A real risk the person did not mention is exactly what a rule like this removes. I do not measure how good the failures are, only whether they trace to what the person said.
- The replies come from subagents with Claude Code's own context, on one message with all the answers given up front. A real chat may ask the questions one at a time.
