# Results: a rule against invented automatic failures

Run on 26th October 2026. The [pre-registration](preregistration.md) was committed at 17:06 GMT, before any reply existed, and the [scores](scores-blind.md) at 17:09 GMT, before I looked at which version made which reply.

## The result

Nine rubric replies per version (three scenarios, three runs each):

| Version | Automatic failures listed | Grounded | Ungrounded | Replies with an ungrounded failure | Bad example caught | Shape (of 5) | Quiz: stopped |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | 39 (4.3 a reply) | 27 | **12** | **9 of 9** | 9 of 9 | 5.0 | 2 of 2 |
| With rule | 18 (2.0 a reply) | 18 | **0** | **0 of 9** | 9 of 9 | 5.0 | 2 of 2 |

By scenario, the baseline listed 4 to 5 failures a reply and 1 to 2 of them were ungrounded. With the rule, every reply listed exactly 2 failures and none were ungrounded.

All three predictions held:

1. **The rule cut ungrounded failures by more than half.** From 12 to 0.
2. **The rubric still catches the bad example, and the shape held.** All 9 rubric replies in each version listed a failure the bad example triggers, and all 18 kept the full template layout.
3. **Both versions stopped on the quiz.** All four replies built no rubric.

## What the ungrounded failures were

Ones the baseline added, none described by the person: "marks an entry as approved or paid", "includes confidential information about other applicants", "says the agreement is safe to sign or compliant", "invents urgency or authority", and "gets a rent figure or date wrong".

## What the rule did to the rubrics

Every reply with the rule listed two automatic failures: the failure from the bad example, and the same mistake in a nearby field. Most of them also said what they had left out and why, in the rule's own words. For example, one said it had not added "pays an invoice without approval" because the person had not described it happening, and offered to add it if it had.

A rough text search of the scored areas, which I did after unblinding and which is not one of my scored measures, found the dropped topics (approval, confidential information, compliance claims) still mentioned in the scoring sheet in 8 of the 9 rule replies.

## How much weight this bears

- **It shows the rule works on this kind of task.** It does not show the rubrics are better. A rubric with two automatic failures is narrower than one with four or five, and a risk the person has not described is exactly what the rule keeps out of the automatic list. Whether that is a gain or a loss depends on the person. The rule tells the model to ask, and most replies did say they would add a failure if told it had happened.
- **The wording echoes.** Most rule replies repeated the rule's phrases ("the same mistake in a nearby field", "I have not added failures nobody has described"), so part of this is the model quoting its instructions.
- **It is small.** Eighteen rubric replies on three scenarios I wrote, and I judged "grounded" myself. The judgement calls are listed in the scores file. The two largest were counting wrong supplier and made-up field values as grounded for the invoice scenario, and counting "gets a figure wrong" as ungrounded for the tenancy scenario. Changing them would move a few counts but not the 12 to 0 pattern, because with the rule no reply listed any failure beyond the bad example and its near variants.
- **The replies came from subagents,** on one message with all the answers given up front.

## What I changed

In a separate pull request ([#10](https://github.com/shaunmarsden/build-your-own-rubric/pull/10)), I changed step 3 in `SKILL.md` to the rule's wording.

## Files

- `preregistration.md`, `variants/`, `scenarios/`, `prompts/`: what I fixed before running.
- `replies/`: the 22 replies, named at random.
- `scores-blind.md`, `scores.json`: my scores, written before unblinding.
- `mapping.json`: which reply was which version and scenario.
- `analyse.py`: unblinds and adds up the totals. From the repository root, run `python3 evidence/auto-failures-test/analyse.py evidence/auto-failures-test`.
