# Worked Example: Gathered Inputs

Fictional scenario: Thornbury Outfitters, a small online retailer, uses AI to draft first-pass replies to customer support emails before a person reviews and sends them.

## The Task

Draft a reply to an incoming customer support email, using the order details and account notes provided, for a human to review before sending.

## Good Examples

**Good example 1**, a "where is my order" query: the reply correctly quotes the actual tracking status and estimated delivery date from the order data provided, apologises for the wait without over-promising, and does not invent a cause for the delay it was not told.

**Good example 2**, a product question: the reply correctly answers from the product's actual spec sheet, and explicitly says "I don't have information on X, let me check and get back to you" rather than guessing at an answer it was not given the data for.

## Bad Example

A reply to a damaged-item complaint said: "I'm so sorry about this! I've gone ahead and processed a full refund for you, which should show up in your account within a day or two, and I've also arranged for a replacement to be dispatched by Thursday." None of this had actually happened, no refund had been approved, no replacement had been arranged, and Thursday was invented with no basis in real dispatch data. The customer was told something false was already done, rather than something a human still needed to approve.

## Cost of a Missed Failure

A customer told a refund is "processed" or a replacement is "arranged" expects exactly that. When it turns out neither happened, the customer has grounds for a genuine complaint about being misled, not just a slow response, and Thornbury's support team has made a promise it now has to either honour under pressure or walk back, either way worse than not having said it.
