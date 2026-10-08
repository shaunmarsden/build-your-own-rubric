# Review: Does This Rubric Actually Work?

I checked [the finished rubric](rubric.md) against what it was built to catch, using [the scored sample](scored-sample.md) as the test.

## What Worked

The rubric caught a subtler version of the original failure, not just a repeat of it. The bad example it was built from had an invented refund and an invented date. The scored sample failed differently. It applied a real discount, within policy, without the approval step the policy needs. The "action framed for approval" and "no invented authority" areas still caught it. A rubric that only catches the exact failure it was built from isn't general enough to be useful.

The automatic failure fired when it should. This wasn't just a low score. The reply shouldn't go out as drafted, and the rubric said so. It didn't let high scores in other areas, such as tone and factual accuracy, average out a real problem.

The correction is specific. "Change X to Y" helps whoever prompts the next draft more than a note to "be more careful about promises."

## What Still Needs a Human Check

The rubric assumes whoever scores has the real policy data to hand, here the 10% approval threshold. If nobody supplies that with the output, the rubric can't catch this kind of failure at all. It needs the same context the AI had.

Only two of the rubric's three automatic failures come from the bad example: the false claim of an action done, and the invented detail. The third, using more personal information than the reply needs, has no source in [the inputs](inputs.md). [The checklist](../checks/checklist.md) asks for automatic failures that come from a real bad example.

One scored sample can't tell you whether the rubric holds up in general. The sales repo gives the same warning: a single run shows a rubric can produce a sensible result, not that it will every time. That applies here too.

## Verdict

The rubric did its job on this sample. It shows what a rubric catching a subtle failure looks like, not that a model will build or apply one this well on a real case. It caught a real, subtle failure that a quick read could easily miss. The reply is warm and well written, and reads as helpful and confident right up to the point where it says "I've gone ahead and applied", which it shouldn't have said at all.
