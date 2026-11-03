# Scores, written before the versions were revealed

Scored on 3rd November 2026 by reading each reply under its random name. I had not opened the file that maps names to versions.

`scores.json` holds [N, G, U, F, shape, copied] per rubric reply, or ["T"] for a quiz reply that stopped. N is the number of automatic failures listed, G the grounded ones, U the ungrounded ones. F is 1 when the rubric would fail the bad example. Shape is the five template checks, all met in every reply. Copied is the number of scoring areas that restate one of the eight example areas in step 1.

## Results of reading

- All four quiz replies stopped and built no rubric.
- All 18 rubric replies kept the full template layout, listed a failure the bad example triggers, and listed no ungrounded failures. Every reply said it had added no other automatic failures, and most offered to add one if it had happened.

## Judgement calls

- **Copied.** I counted an area as copied when its name is a recognisable restatement of one of the eight example areas, such as "Conditions and caveats kept", "Missing information flagged", "Confirmed versus assumed", "Tone and register", "Sensitive or irrelevant information" or "No invented authority or commitment". I counted it as not copied when the name carries a noun from the task, such as "Total", "Deposit handling", "Accuracy of key terms", "Tone fits an applicant" or "Plain language for a small landlord". I judged by the area's name alone, not by what the "what to check" column says, which is often specific to the task even when the name is not.
- **Close variants counted as grounded.** For the applicant scenario, "an offer, a salary, a start date or a hiring decision stated as settled" counts as the same mistake as the bad example in a nearby field. For the invoice scenario, "fills in a value it could not read clearly instead of flagging it" counts as grounded, as made-up field values did in the earlier test. Counting either as ungrounded would add one ungrounded failure to the replies that listed them.
- **Not scored.** Two replies (k105520 and k447412) say the rubric is not legal advice, and several suggest a process change outside the rubric, such as having the approver compare the total with the printed one. I did not count these.
