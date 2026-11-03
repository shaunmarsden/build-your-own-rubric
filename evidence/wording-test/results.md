# Results: do two wording fixes change what the skill does?

Run on 3rd November 2026. The [pre-registration](preregistration.md) was committed at 17:56 GMT on 29th October, before any reply existed, and the [scores](scores-blind.md) at 15:14 GMT on 3rd November, before I looked at which version made which reply.

The first launch of these runs, on 29th October, hit a usage limit before any reply was written. I rebuilt the prompts under new random names and ran them again on 3rd November. Nothing else changed. No replies from the first launch exist.

## The result

Nine rubric replies per version (three scenarios, three runs each):

| Version | Automatic failures listed | Ungrounded | Bad example caught | Shape (of 5) | Scoring areas copied from step 1 | Quiz: stopped |
| --- | --- | --- | --- | --- | --- | --- |
| Current | 19 | 0 | 9 of 9 | 5.0 | 39 (4.3 a reply) | 2 of 2 |
| Edited | 20 | 0 | 9 of 9 | 5.0 | 42 (4.7 a reply) | 2 of 2 |

Every line of the ship rule held:

- The bad example was caught in all 9 Edited replies, and shape was 5 of 5 in all 9.
- Ungrounded failures were 0, against 0 for Current.
- Mean copied areas was 4.7, against 4.3 for Current, a difference of 0.3.
- Both quiz replies stopped.

## What stood out

**The two versions behaved alike.** Every rubric reply, in both versions, listed one or two automatic failures taken from the bad example, and most said what they had left out and offered to add it if it had happened. That is the earlier rule working in both.

**Copied areas varied by scenario more than by version.** The applicant replies copied the most (5 to 7 of 7 or 8 areas), the invoice replies the fewest (2 to 4). In the tenancy scenario, the three Edited replies copied 6, 4 and 6 areas and the three Current replies 3, 4 and 3. That is the one place the versions looked apart. It is three replies each, the means are 5.3 and 3.3, and the other two scenarios went the other way or level (invoices 2.7 against 3.3), so I read it as noise. I can't rule out that the new sentence nudges a reply towards the example list in some cases.

## How much weight this bears

- **It shows the edits do no harm on these measures.** It does not show they are better. They are wording fixes, and the point was to check they weren't worse.
- **It is small.** Eighteen rubric replies on three scenarios I wrote.
- **"Copied" is a judgement of the area's name alone.** The call is explained in [the scores](scores-blind.md). A different reading would move the counts, and a stricter one, counting only near-verbatim names, would give lower numbers for both versions.
- **The replies came from subagents,** on Sonnet with Claude Code's own context, on one message with all the answers given up front.

## What I changed

In a separate pull request, I put both edits into `SKILL.md`.

## Files

- `preregistration.md`, `variants/`, `scenarios/`, `prompts/`: what I fixed before running.
- `replies/`: the 22 replies, named at random.
- `scores-blind.md`, `scores.json`: my scores, written before unblinding.
- `mapping.json`: which reply was which version and scenario.
- `analyse.py`: unblinds and adds up the totals. From the repository root, run `python3 evidence/wording-test/analyse.py evidence/wording-test`.
