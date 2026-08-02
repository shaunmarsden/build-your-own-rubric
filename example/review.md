# Honest Review: Does This Rubric Actually Work?

Checking [the finished rubric](rubric.md) against what it was built to catch, using [the scored sample](scored-sample.md) as the test.

## What Worked

- **The rubric caught a subtler version of the original failure, not just a repeat of it.** The bad example used to build the rubric had an invented refund and an invented date. The scored sample's failure was different in shape, a genuine, in-policy discount figure applied without the required approval step, and the "action framed for approval" and "no invented authority" areas still caught it. A rubric that only catches the exact failure it was built from is not actually general enough to be useful.
- **The automatic failure fired correctly.** This was not just a low score, the reply genuinely should not go out as drafted, and the rubric said so plainly rather than letting a high total on other areas (tone, factual accuracy) average out a real problem.
- **The correction is specific, not generic.** "Change X to Y" is more useful to whoever prompts the next draft than a general note to "be more careful about promises."

## What Still Needs a Human Check

- The rubric assumes the person using it actually has the real policy data (the 10% approval threshold) available when scoring. If that information is not supplied alongside an output, the rubric cannot catch this category of failure at all, it depends on being fed the same context the AI had.
- One scored sample is not enough to know whether this rubric holds up broadly; the same caution the sales repo applies (a single run shows a rubric can produce a sane result, not that it reliably will) applies just as much here.

## Verdict

The rubric did what it was built to do: it caught a real, subtle failure that a quick read of a warm, well-written reply could easily miss, since the reply reads as helpful and confident right up until the specific detail that it should not have said "I've gone ahead and applied" at all.
