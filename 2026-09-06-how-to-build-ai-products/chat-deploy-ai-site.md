---
title: "Deploy AI Site"
date: 2026-09-09T13:11:47+08:00
source: "https://chatgpt.com/c/6aa0c42c-b0b0-83ec-845a-116eab8985b8"
---

# User

I have an application that needs to use LLMs as part of its feature set. For example, answering a question from data that the user types in. When I create this as a ChatGPT site, it works fine, but then I'm not able to deploy it for others to be able to use. If I publish it, say on Cloudflare or GitHub or some other place, then I'm not sure how I could go about using the AI features. Can you explain in really simple terms, the most concise way possible, what's the easiest and right solution for me, so that I can expose a simple site to at least a few people, or maybe even publicly, and it should be able to incorporate AI features without too much cost on my side.

# ChatGPT

The simplest solution for your case is: deploy the whole app on Cloudflare Pages/Workers, and use Cloudflare Workers AI from a tiny server-side function.

The architecture is just:

`Browser → your Cloudflare site → /api/ask → LLM → answer`

The important bit is that the browser should not call an LLM API directly. If you put an OpenAI/Anthropic API key into JavaScript running in the browser, anyone can steal it. Instead, one small server-side function receives the user's question, calls the model, and returns the answer.

Cloudflare makes this unusually simple because Pages Functions/Workers can call Workers AI directly through an `AI` binding—no separate server and, for Cloudflare's own models, no API key management. [Cloudflare Docs+1](https://developers.cloudflare.com/pages/functions/bindings/?utm_source=chatgpt.com)

Conceptually, your backend can be almost this small:

```
export async function onRequestPost({ request, env }) {
  const { question } = await request.json();

  const result = await env.AI.run(
    "@cf/google/gemma-4-26b-a4b-it",
    { prompt: question }
  );

  return Response.json(result);
}
```

Then your existing webpage does:

```
const answer = await fetch("/api/ask", {
  method: "POST",
  body: JSON.stringify({ question })
}).then(r => r.json());
```

For a prototype shared with a few people, this may cost essentially nothing: Cloudflare currently gives Workers AI 10,000 neurons/day free; beyond that it is usage-priced. [Cloudflare Docs](https://developers.cloudflare.com/workers-ai/platform/pricing/?utm_source=chatgpt.com)

So I would rank the choices:

1. **Cloudflare Pages + Pages Function + Workers AI — easiest for you.** One deployment, no server, no exposed secret, generous free allowance.
2. **Cloudflare Pages/Worker + OpenAI/Anthropic API — use this when model quality matters more.** Same architecture; store the API key as a Cloudflare secret. You pay per token.
3. **GitHub Pages alone — don't.** It is basically static hosting, so you still need a backend somewhere else to protect the API key.

The useful mental model is therefore:

> A public AI app needs only two things: a webpage and a tiny private function that makes the LLM call.

You do **not** need to run a server, manage GPUs, set up a database, or build authentication initially. Cloudflare can provide both halves of the application. [Cloudflare Docs](https://developers.cloudflare.com/pages/functions/?utm_source=chatgpt.com)

For something public, I would add one cheap safety measure: rate-limit `/api/ask` so one person cannot burn through your allowance. For a handful of known users, you can probably deploy first and add this afterwards.
