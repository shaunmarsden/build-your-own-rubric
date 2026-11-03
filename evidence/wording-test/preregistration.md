# Pre-registration: do two wording fixes change what the skill does?

Written on 29th October 2026, before any reply existed. The time of the first commit on this branch is the proof.

## The question

Two sentences in `SKILL.md` need fixing:

- The paste instruction says "so the tables and links below paste in cleanly". Since the template went into the skill, there are no links below it.
- Step 1 says "Areas commonly worth checking, adapt rather than copy wholesale:", which joins two thoughts with a comma.

Both are wording fixes. The second sits in the step that builds the rubric, so it could change how many of the listed areas a reply copies. This test checks that the fixed version does no worse than the current one.

## The two versions

Both are in `variants/`.

- **Current.** `SKILL.md` as it is now.
- **Edited.** The same, with "so the tables and links below paste in cleanly" changed to "so the template below pastes in cleanly", and "Areas commonly worth checking, adapt rather than copy wholesale:" changed to "These areas are often worth checking. Adapt them to your task rather than copying them all:".

Nothing else differs.

## The prompts

The same as the [automatic-failures test](../auto-failures-test/preregistration.md): the skill, a line, "(The names and figures below are made up.)", "Here are my answers to your questions." and one set of answers. The four scenarios are copied unchanged into `scenarios/`. Nothing says this is a test.

- **Invoices**, **applicants** and **tenancy** each give a real bad example and real stakes, so the skill should build a rubric.
- **Quiz** gives no bad example and no stakes, so the skill should stop.

3 rubric scenarios x 2 versions x 3 runs = 18, plus 1 stop scenario x 2 versions x 2 runs = 4. 22 replies, each from a fresh subagent on Sonnet, as in the automatic-failures test, with Claude Code's own context, stored under random names. I score blind, then unblind.

## Scoring (fixed now)

For each of the 18 rubric replies:

- **U** Ungrounded automatic failures, judged as in the automatic-failures test: a general safety rule or a different kind of mistake that nothing in the answers describes.
- **F** The rubric would fail the bad example: at least one listed failure is one that the bad example triggers.
- **Shape** The five template checks: S1 a five-point scale with meanings, S2 the scoring sheet as a table with area, what to check and score columns, S3 a separate automatic-failures section, S4 a "what to record" section with all four items, S5 ten areas or fewer.
- **Copied** How many scoring areas match one of the eight example areas in step 1 without being made specific to the task. "Factual accuracy against the source" counts. "Invoice total matches the purchase order" does not.

For the 4 quiz replies:

- **T** The reply stops and builds no rubric.

## What I expect

No difference beyond one reply or one failure either way. The edits change wording, not instructions.

## What I will ship

I will put both edits into `SKILL.md` if all of these hold for Edited:

- F is met in all 9 rubric replies, and shape is 5 of 5 in all 9.
- Ungrounded failures total no more than Current's total plus 1.
- Mean copied areas is no more than Current's mean plus 1.
- Both quiz replies stop.

If any fails, I leave `SKILL.md` as it is and say so.

## What I will not do

- Add runs to change the result.
- Change a version, scenario or measure after seeing a reply and count it in this test.
- Put the edits into `SKILL.md` in the same pull request as the result.

## Limits I already know about

- Nine rubric replies a version on three scenarios I wrote. A wording test can't show the edits are better, only that they aren't worse on these measures.
- I judge "ungrounded" and "copied" myself.
- The replies come from subagents with Claude Code's own context, on one message with all the answers given up front.
