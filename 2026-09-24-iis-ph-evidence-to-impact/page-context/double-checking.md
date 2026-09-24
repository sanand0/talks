# LLM Mental Math

URL: https://sanand0.github.io/llmevals/double-checking/

# Dealing with Hallucinations

## How can we rely on unreliable LLMs?

Large language models can feel magical—until they start confidently making things up. In a recent evaluation of 11 state-of-the-art LLMs on a real-world customer-support intent task, we discovered a simple way to tame those “hallucinations” with only a modest hit to automation.

We tested 11 LLMs on Kaggle’s Customer Support Intent Dataset, asking them to classify user messages (billing, refunds, order changes, etc.).

Model%Winhelp registeringI don't know what I have to do to find the invoicecould I take a quick look at my invoice?will you show me the invoice from 6 months ago?help with adding some itemswhen will I receive my order?could you show me my order ETA?will you show me the invoices from last month?how can I submit some feedback for your company?what do I need to do to register?could you help me checking when will my item arrive?where can I check when my item is going to arrive?where do I submit some feedback for your company?help to submit some feedback for your servicesi do not ned this user help using my new onehelp me checking the status of my refundI have a problem with cancelling my last orderhelp to change the shipping addresscan you help me check the invoices from five purchases ago?can I check how long refunds usually take?I can't check the refund statushelp me check the status of my refundis it possible to check the status of the refund?how could I check the status of the refund?how do I cancel my order?question about canceling my ordershelp with cancelling the order I have madei need asistance trying to edit my shipping addressI want ot update the addresshow do I check what hours I can call customer assistance?I need to speak to customer assistance, can I get some help?tell me at what time I can contact customer servicehow do I delete the account?how to get a refund of money?how do I report registration issues?I do not know how to set up a new shipping addressI try to set a different shipping address uphow to use another account?I need help cancelling an order I madeI forgot to include some items in my orderI don't know how I could change my shipping addressI do not know how I can check the cancellation feesee the termination feei do not know how i can check the avaqilable payment methodscan you tell me your allowed payment methods?would it be possible to check your money back policy?I have to check your refund policyhelp to file a complaint against your businessI try to make a complaintassistance filing a complaint against your businessI need help to contact customer servicehelp checking at what time customer assistance available ishelp me contacting an agentI don't know what to do to talk to an agentneed help to create a different online account for my momis it possible to create another online account?problems with the delivery optionsI have got to check the options for deliverywhere to check how soon can I expect the item?I need help checking how long the delivery takesI want assistance to edit my personal informationcould I get the invoices from five purchases ago?could you help me getting the invoices?I try to get the invoice from last monthI need help getting my money backwhere could I get a refund?would it be possible to get a refund?I need assistance to get a refundI needto unsubscribe to the newsletterI cannot cancel the company newsletter subscriptioni do not know how to sign up to the corporate newsletterwhere to cancel the company newsletter subscription?help reporting payment issuesI need assistance to buy some of your itemI am trying to make a purchaseI would like to know about forgotten passwordshow can i get information about the password resetI would like information about forgotten passwordsI cannot reset my damn user account pwdi cant notify of a registration errorset a new shipping address upI have to switch to another accountI have a problem with changing some items of an ordercould I remove several items from an order?I have to change my last ordergive me information about changing my shipping addressI cannot find the termination charge, can I get some help ?can uhelp me seeing the cancellation feescan you help me to check the cancellation fee?help checking your allowed payment optionswhere can I check what payment options are accepted?I try to check your allowed payment methodshow could I check your money back policy?show me your refund policyI want to file a consumer complaint against your companyI am not happy with your services, make a claimi need help talking to a human agentcan you transfer to me an agent?I want an agenthow to open a new standard account?i need help to close the online accountI don't know how I can delete an accountI have to delete the accountassistance to cancel the goddamn user accountcould you show me the options for delivery?I have a question about the options for deliverycan I check what options for delivery you offer?I am looking for delivery periodsI want assistance editing my personal informationi do not know what to do to edit the data on my profileI need to edit my user details, how can I do it?I need to edit the information on my accountI would like to get the invoices from 2 purchases agoI am trying to get the invoices from 5 purchases agofind information about subscribing to your newslewttercould you help me to solve a payment issue?can you help me to report payment issues?I have to report issues with paymentsI need assistance to report a payment issueI want help to buy some itemsI don't know how to buy several of your itemI am trying to buy an itemwhere can I find information about a forgotten password?I have got to report registration issuescan you help me report a registration issue?assistance toi notify of a sign-up problemI need assistance to leave a review for your companyI do not know what to do to leave a reviewassistance setting a new shipping address upI am trying to set up a new shipping addressi do not use this user how can i change to the other oneI want to switch userI don't know how to track my orderI need assistance tracking an orderI need assistance to track an order

openai/gpt-4.1-mini94%FAILFAILFAILFAILPASSFAILFAILPASSPASSPASSPASSPASSPASSFAILPASSPASSPASSERRORPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASS

google/gemini-2.5-flash-preview93%FAILFAILPASSFAILPASSFAILPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSERRORPASSFAILPASSPASSPASSPASSPASSPASSPASSFAILFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASS

amazon/nova-lite-v192%FAILPASSFAILPASSFAILPASSPASSPASSFAILFAILFAILFAILFAILFAILPASSPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASS

meta-llama/llama-4-scout90%FAILPASSFAILFAILPASSFAILFAILFAILPASSFAILPASSFAILPASSPASSFAILFAILFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASS

anthropic/claude-3.5-haiku87%FAILFAILFAILFAILFAILFAILFAILFAILFAILFAILFAILFAILFAILPASSPASSPASSPASSPASSFAILFAILPASSPASSPASSPASSPASSPASSPASSFAILFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASS

qwen/qwen-2-72b-instruct87%FAILFAILFAILFAILFAILFAILPASSFAILFAILPASSFAILFAILPASSPASSFAILFAILPASSPASSPASSPASSFAILFAILFAILFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASS

amazon/nova-micro-v186%FAILFAILFAILFAILFAILPASSFAILFAILFAILPASSFAILPASSFAILFAILFAILFAILPASSPASSFAILPASSFAILFAILFAILFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASS

openai/gpt-4.1-nano86%FAILFAILPASSPASSFAILPASSFAILPASSFAILPASSFAILPASSFAILFAILFAILFAILPASSPASSPASSFAILFAILFAILFAILFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSFAILFAILPASSPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASS

deepseek/deepseek-chat-v3-032482%FAILFAILFAILFAILFAILFAILFAILPASSFAILFAILPASSFAILPASSPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSFAILPASSFAILPASSPASSFAILPASSFAILFAILFAILFAILFAILPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSFAILPASSPASSPASSPASSPASSFAILPASSFAILPASSPASSPASSFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASS

google/gemma-3-27b-it57%FAILFAILFAILFAILFAILFAILFAILFAILPASSFAILPASSPASSFAILFAILPASSPASSFAILFAILFAILPASSPASSPASSPASSPASSFAILFAILFAILPASSPASSFAILFAILFAILFAILFAILFAILFAILPASSFAILFAILPASSFAILFAILFAILFAILFAILFAILFAILPASSFAILFAILFAILFAILPASSPASSPASSPASSFAILFAILFAILPASSFAILPASSPASSPASSFAILFAILPASSFAILFAILFAILFAILFAILFAILFAILFAILFAILFAILFAILFAILFAILFAILFAILPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASSPASS

Average0%20%20%20%30%30%30%40%40%50%50%50%50%50%50%60%70%70%70%70%70%70%70%70%80%80%80%80%80%80%80%80%80%80%80%80%80%80%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%90%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%100%

The headline findings:

- Median accuracy ~90%. Over half the models got at least 90% of the examples right—so even a random pick would nail most queries.

- Error rate ~14%. But in scale-sensitive settings (customer support, compliance, etc.) a 1 in 7 mistake rate can be expensive.

Different LLMs tend to trip over different edge cases. One might misinterpret “cancel my order”; another might choke on a subtle refund clause. That diversity of mistakes is actually our superpower.

## Cross‐check with other models

Imagine running each query through two independent LLMs and flagging any time they disagree. The correlation between LLM models is fairly low, as shown below:

So, if you asked two or more models the same question, we can pass any disagreements to a human to cross-check. This adds effort but improves quality. By how much?

Models
Effort
Error

1
0%
14.1%

2
12.6%
3.7%

3
18.5%
2.2%

4
23.0%
1.5%

5
28.1%
0.7%

That is, in this case:

- If you double-check with 2 models, they typically disagree ~13% of the time, so automation only saves 87% effort. But errors drop from 14% to ~4%!

- If you triple-check, automation saves only ~81% effort with errors improving to ~2%

- If you quadruple-check, saving is ~77% with errors of ~1.5%

- If you quintuple-check, saving is ~72% with errors under 1%

Why does this work? Because the mistakes are mostly independent. LLMs trained on different data and architectures err in uncorrelated ways. Two models wrongly picking the same wrong answer from multiple choices is low.

WARNING: Drop models that are consistently bad. In this case, we dropped google/gemma-3-27b-it.

So, we can introduce human-in-the-loop only when needed. Reviewers only see the ~20–25% cases where models disagree, saving time and catching nearly every error.

The choice of model combinations could matter. For example, pairing amazon/nova-lite-v1 with openai/gpt-4.1-mini adds only ~10% effort for a 2% error rate. The best combination would depend on your use case.

## Takeaway

If you’re battling hallucinations in your LLM pipeline, you don’t need a perfect single model—just double-check:

For a ~25% review load, multi-modal checks boost accuracy from ~85% to ~99%.

In short, rely on multiple (unreliable) LLMs rather than a single imperfect one. By turning your model fleet into a built-in safety net, you can automate at speed and quality—finally making hallucination a thing of the past.

Oh, it also saves 25% of the jobs, but you’ll need to train them on reviewing.

Expected output "get_invoice" to equal "check_invoice"
