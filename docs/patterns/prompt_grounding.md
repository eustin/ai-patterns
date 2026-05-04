---
title: Prompt Grounding
nav_order: 2
---

# TL;DR

> Problems:
> * My LLM is hallucinating about stuff that isn't in its training data
> * My LLM wasn't trained on our private data so it can't answer questions about it.
> * I can't afford to train or fine tune an LLM. How can I make it aware of latest data? etc
> 
> Solution: Inject "relevant" documents directly into the LLM prompt to ground it in reality. Force it to answer based solely on the provided context documents. Ask it to cite sources.

# Excel World Championships. Oh hell yeah.

* Road to Las Vegas happening now. Want to find out who won Battle I of the qualifier rounds.
* Get LLM with knowlege cutoff in past.
* Show snippets of the setup code.
* Ask who won battle I - get bullshit answer
* Problem: LLM clearly doesn't know a thing about the qualifiers. Not in training data. It also sounds so confident while being so bloody wrong (sounds like people I've met in my career)

## Prompt Grounding

* Solution: LLM is off with the fairies. It has done too much acid. Bring it back to reality by grounding its response in "reality". How do we do that? Via a special prompt.
* Note that this is part of the RAG, which we will be working towards across multiple patterns
* Show RAG prompt example, along with links to LangChain docs and the Anthropic docs. 
* Point out the defensive instructions to avoid indirect prompt injection.

## Resolution

* Let's throw a bucket of ice on the LLM's face and tell it to snap out of it.
* Show the full prompt again, but this time with the contextual docs injected
* Ask question again, and get the answer.

## What we haven't covered

* This is a number one bullshit toy scenario - we haven't touched on how to find relevant docs to inject, nor have we touched what the hell a "doc" is. We will cover them off in future patterns about document chunking, indexing and retrieval.
* Haven't touched on getting LLM to cite sources so you can trust it. Will do that in document chunking.

# Let's talk business: Giving LLMs access to your private data

* We are Synergy.ai. 
* We have top secret internal documents we want our LLM to know about. But because they are top secret, they aren't in the LLM's training data, nor do we want it to be in the training data.
* Let's illustrate how injecting private documents at "runtime", one of which contains the answer, helps reduce the LLM's level of bullshit.  
* Say we have internal documents our LLM doesn't have access to:

> - CEO Hype Rate for June 2026 was 800 Altmans, up 3,000% year on year.
> - Our top model, AgiForRealsiesThisTime, is...like...too powerful for public consumption...maaaan. It's a game ch4ng0rrrr!!!
> - In 2026, our Engineer AI Disillusion Rate was 10,000 Anthropics, increasing 1,337% from the prior year.

* Ask it the question - how many anthropics is the engineer AI disillusion index?
* See bullshit response
* Ground it in the exact same prompt as before and ask same question.
* Show answer
