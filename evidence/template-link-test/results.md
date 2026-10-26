# Results: should the template sit inside the skill?

Run on 26th October 2026. The [pre-registration](preregistration.md) was committed at 15:12 GMT, before any reply existed, and the [scores](scores-blind.md) at 15:17 GMT, before I looked at which version made which reply.

## The result

Six rubric replies per version (three scenarios, two runs each), scored on five shape checks out of five:

| Version | Mean shape score | Replies with all five | Scoring sheet as a table with a score column | Newsletter: stopped |
| --- | --- | --- | --- | --- |
| Current (with the closing links) | 4.0 | 0 of 6 | 0 of 6 | 2 of 2 |
| No links | 4.0 | 0 of 6 | 0 of 6 | 2 of 2 |
| **Inline template** | **5.0** | **6 of 6** | **6 of 6** | **2 of 2** |

All three predictions held:

1. **Inline scored higher than Current.** 5.0 against 4.0.
2. **No links was close to Current.** Identical. The links and the pointers to the worked examples made no difference to the shape.
3. **All three stopped on the newsletter.** Every version, both runs, built no rubric and said why (no bad example, no real cost).

## What separated the versions

One check did all the work: the scoring sheet. Every reply from every version had a scale, a separate list of automatic failures, a "what to record" section with the four items, and ten areas or fewer. Only the inline versions put the areas in a table with an area column, a "what to check" column and a score column. The other twelve replies listed the areas as a numbered list, or as a table with no score column. The inline replies followed the template's layout, headings and wording.

## A second finding: the automatic failures

Every one of the 18 rubric replies, in every version, listed at least one automatic failure that has no basis in the stated bad example. Examples were "says the contract is safe to sign", "is presented as approved" and "gives more than one priority". A few said which failures were their own guesses. The repository's checklist says automatic failures should come from a real bad example, and the skill only says that drawing from the bad example "helps". Putting the template in the skill does not change this. If it matters, it is a different change to the skill, and it would need its own test.

## How much weight this bears

- **It is a layout result.** Inline makes the output follow the template. It says nothing about whether the rubric is a good one.
- **It is small.** Eighteen rubric replies on three made-up scenarios, which I wrote, with a scoring scheme that I wrote. The five shape checks were fixed in advance, but only one of them separated the versions.
- **The replies came from subagents** with Claude Code's own context, on one message with all the answers up front. A real chat may ask the questions one at a time.
- **Some of the inline replies copied the template's wording,** including its opening line, which is the intended effect.

## What I will propose

A separate pull request that changes `SKILL.md`: add the contents of `templates/rubric-template.md` inside the skill under an "Output Format" heading, as in the inline version in `variants/`, and move the closing links to the worked examples, template and checklist out of the skill and into the README, where they already are. I have not made that change here, and I will not make it without your word. A note on size: the inline version is about 170 words longer (1,047 words against 879).

## Files

- `preregistration.md`, `variants/`, `scenarios/`, `prompts/`: what I fixed before running.
- `replies/`: the 24 replies, named at random.
- `scores-blind.md`, `scores.json`: my scores, written before unblinding.
- `mapping.json`: which reply was which version and scenario.
- `analyse.py`: unblinds and adds up the totals. Run it on a folder holding `scores.json` and the mapping file (named `MAPPING_DO_NOT_READ_UNTIL_SCORED.json` there).
