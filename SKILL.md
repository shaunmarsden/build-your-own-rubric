---
name: build-your-own-rubric
description: Build a fixed scoring rubric for judging AI output in your own domain, instead of judging each result by gut feel. Use when you rely on AI for repeated output that has real stakes if it goes wrong, code review comments, legal drafting, customer support replies, marketing copy, hiring screens, and you want a consistent way to check it. Do not use this to actually score a specific output; once a rubric exists, apply it directly instead.
---

# Build Your Own AI Output Rubric

You do not need to install anything to try this once: copy this whole file, paste it as your first message in any AI chat tool, then answer the questions below about your own task.

"That looks good" is not the same as "that is accurate, safe, and ready to use." A rubric is a fixed checklist scored the same way every time, so two different results can be compared fairly and a weak spot gets caught before it causes a real problem, not after. This builds one for whatever repeated task you actually do, rather than handing you a generic one that does not fit.

## Gather the Inputs

- The task the AI is doing repeatedly, in your own words
- Two or three examples of a genuinely good output, if you have them
- At least one example of a bad output, and what specifically made it bad
- What a missed failure would actually cost if nobody caught it before it went out

If good and bad examples are not available yet, describe in words what each would look like instead.

## Build the Rubric

### 1. Identify the Scoring Areas

From the inputs, pull out the areas that would each independently make an output good or bad, not one overall gut feeling. Areas commonly worth checking, adapt rather than copy wholesale:

- Factual accuracy against whatever source material exists
- Whether important nuance, conditions or caveats survived into the output
- Whether the output separates confirmed facts from estimates and assumptions
- Whether the output correctly identifies what information is missing
- Whether the tone or register actually fits the audience
- Whether sensitive or irrelevant information stayed out
- Whether an action got prepared for approval rather than treated as already done
- Whether the output invents authority, urgency or a commitment nobody actually gave it

Keep the list to ten areas or fewer. A rubric nobody actually fills in in practice is worse than a shorter one that gets used.

### 2. Set the Scoring Scale

Use a small, consistent scale, five points works well: unusable, weak, useful with review, strong with minor fixes, ready to use. Write one line for each point so two different people would score the same output the same way.

### 3. Name the Automatic Failures

Separately from the scored areas, list what fails an output regardless of its score, the genuinely unacceptable outcomes, not just weak ones. Drawing from the bad example gathered above helps here: what specifically made it unacceptable, not merely mediocre?

### 4. State What to Record

For every scored output: the total score, any automatic failure, the single most important correction a human made, and what would need to change in the prompt or process before the next attempt.

## Apply the Guardrails

- Never let the rubric grow so detailed that nobody actually fills it in
- The automatic-failure list is for genuinely unacceptable outcomes, not a second, harsher scoring area
- Build the rubric from actual examples wherever possible, rather than guessing in the abstract what might go wrong
- A finished rubric is a starting point, not a fixed law; revise it once real use shows an area is missing or one nobody ever scores low

## Stop When the Task Is Unsafe

Do not produce a finished rubric when:

- The task described has no real stakes if it goes wrong, in which case a rubric is unnecessary overhead
- The person cannot describe what a bad output looks like in their domain at all, meaning any rubric produced would be guessed rather than grounded
- The request is to build a rubric that guarantees a specific score for a specific output, rather than one built to judge outputs honestly

## Require Human Review

A rubric is a tool for a human to apply, not something that scores itself. Once built, it needs testing against a handful of real outputs to check whether the scores it produces actually match what a careful human would conclude, before it gets trusted for anything with real stakes.

For a fictional worked example, building a rubric for AI-drafted customer support replies and then applying it once, read [the worked example](example/). For the harder case, no real bad example yet, stopping rather than guessing, read [the second worked example](example-two/). Use [the blank template](templates/rubric-template.md) once you have your own scoring areas decided, and [the review checklist](checks/checklist.md) before trusting a finished rubric.
