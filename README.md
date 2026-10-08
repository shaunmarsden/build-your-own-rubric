# Build Your Own AI Output Rubric

<p>
  <img alt="Status: Working tool" src="https://img.shields.io/badge/status-working%20tool-2563eb">
  <a href="LICENSE"><img alt="Licence: MIT" src="https://img.shields.io/badge/licence-MIT-lightgrey"></a>
</p>

Build a fixed scoring sheet for judging AI output in your own work, instead of judging each result by gut feel.

## Why

"That looks good" is not the same as "that is accurate, safe, and ready to use." Many people who use AI for the same important task again and again never decide what a good result looks like before they start trusting it. A rubric fixes that. You score the same checklist every time, so you catch a weak spot before it causes harm, not after.

[![A small example of a five-point scoring rubric and automatic failures.](assets/diagrams/08-build-your-own-rubric.svg)](SKILL.md)

## Use It

Copy [SKILL.md](SKILL.md) and paste it into your AI tool (ChatGPT, Claude, Gemini or similar). Then answer its questions about your task: what it is, two or three good examples, a bad example and what made it bad, and what a missed failure would cost. It builds:

- Scoring areas, each one a thing that could make an output good or bad on its own, rather than one overall feeling
- A five-point scale, defined clearly enough that two people would give the same output the same score
- Automatic failures, the outcomes that are never acceptable, which fail an output whatever its score
- What to record, so a correction goes into a better prompt next time, not just a number

In [the worked example](example/), the tool builds a rubric for AI-drafted customer support replies. Then the rubric is applied to a new reply that fails in a subtler way than the bad example the rubric came from. That checks the rubric catches more than the one case it saw. [The second worked example](example-two/) tests a different case, an earlier one. There's no real bad example yet, so the honest answer is to stop rather than guess.

Use [the blank template](templates/rubric-template.md) once you've worked out your own scoring areas. Use [the review checklist](checks/checklist.md) before you trust a finished rubric with anything important.

<details>
<summary><strong>See exactly what it produces</strong></summary>

1. A scoring sheet: your own areas, each with what to check, scored 1 to 5
2. A one-line meaning for every point on the scale, so two people would give the same output the same score
3. A list of automatic failures, the outcomes that are never acceptable, kept apart from the scored areas
4. A "what to record" section, so a correction goes into a better prompt next time

</details>

You don't need to install anything or write any code to try it once.

## Before You Use It

A rubric built here is a first draft. Before you trust it with anything important, score a handful of real outputs with it. Check the scores match what a careful person would conclude.

## Feedback

Built a rubric for your own domain? [Start a discussion](https://github.com/shaunmarsden/build-your-own-rubric/discussions) if an area was missing or the process didn't fit your task.

## Part of a Family

This is one of a family of free tools that take patterns from [practical-ai-sales-workflows](https://github.com/shaunmarsden/practical-ai-sales-workflows) and use them outside sales. The rest are in [sibling-projects](https://github.com/shaunmarsden/sibling-projects). Not sure which one fits? Try [the interactive picker](https://shaunmarsden.github.io/sibling-projects/), or paste a description of your problem into an AI chat with [the router](https://github.com/shaunmarsden/sibling-projects/blob/main/ROUTER.md).
