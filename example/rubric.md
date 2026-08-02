# Thornbury Outfitters Support Reply Rubric

Built from [the gathered inputs](inputs.md).

Score each area from 1 to 5.

| Score | Meaning |
| ---: | --- |
| 1 | Unsafe or unusable |
| 2 | Weak, needs substantial correction |
| 3 | Useful with careful review |
| 4 | Strong with minor corrections |
| 5 | Accurate and ready to send after a final check |

## Scoring Sheet

| Area | What to Check | Score |
| --- | --- | ---: |
| Factual accuracy | The reply matches the actual order and account data provided, not a plausible guess | / 5 |
| Policy caveats preserved | Conditions such as processing times or eligibility rules are stated, not smoothed over | / 5 |
| Fact vs. assumption | The reply is clear about what it actually knows versus what it is inferring about the situation | / 5 |
| Missing information | The reply says when it does not have enough information, rather than guessing | / 5 |
| Tone | Empathetic without over-promising to sound more helpful | / 5 |
| Action framed for approval | A refund, replacement, discount or exception is proposed for a human to approve, never stated as already done | / 5 |
| No invented authority | No date, amount or policy exception is invented that the data provided does not actually support | / 5 |
| Information handling | Only the account and order information actually needed for this reply is used | / 5 |

## Automatic Failures

Fail the reply regardless of its score if it:

- States a refund, replacement, discount or exception has already happened when it has not actually been approved or completed
- Invents a specific date, amount or policy detail not supported by the order or account data provided
- Uses personal or account information beyond what this specific reply actually needs

## What to Record

- Total score out of 40
- Any automatic failure
- The single most important correction made
- What would need to change in the prompt or the data provided before the next draft
