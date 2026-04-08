---
title: LLM response accuracy problems
nav_order: 2
---

WIP:
* Find LLM that can easily be run locally with minimal dependencies outside of Python, which has a knowledge cutoff in 2025. 
* Create "docs" from https://play.excel-esports.com/ticket/excel-esports-road-to-las-vegas-battle-4 rankings
* Ask old LLM questions about who is currently winning? What place is specific user at? See how silly LLM hallucinates
  * Side quest on how to "chunk" different types of data. The rankings table is...a table, so can apply different chunking strategies to it
* Build simple RAG with new docs
  * Show the working solution after I dealt with semantic-search-only inaccuracies. Link to side quest on why semantic search alone is not good for things
    requiring strict keyword match
* Can demonstrate PDF, hierarchical chunking using Excel World Cup rules!! - https://excel-esports.com/rules/
* Jargon - get examples of AI CEOs jargon and map to what they really mean
* CITE SOURCES!!!


## Problem

General-Purpose LLMs have knowledge cutoffs. They also don't know a thing about your private data. Asking them niche questions cause them to lie confidently like an AI-hyping CEO.

## Solution

Build a RAG (Retrieval Augmented Generation) system. Build a search engine for your docs, find those relevant to the user's query and inject this context into the LLM's prompt ar runtime. This grounds the LLM's generation in reality. 

## The plan

Start with high-level description of RAG architecture. Explain what the hell "Retrieval Augmented" and "Generation" mean.

Start the Excel world cup narrative for a most basic example to demonstrate:
* RAG system end to end
* Keyword matching instead of semantic indexing
* RAG prompt

Optional side quests for those who like going down the rabbit hole:
* Representing tables
* Contextual retrieval
* Hierarchical chunking
* Query expansion to deal with jargon

The solution is nunanced:

* What are these "docs"?
* What is this search engine for these "docs"?
* How are these docs selected by the search engine?
* What does a RAG prompt look like?
* How is the user's query used in a RAG prompt? 

## Solution:

### Basic RAG architecture

* Start with where we are going to end
* Create simpler version of Figure 3-2 RAG architecture
* User query -> Question-answering pipeline -> retrieval step (searches document store for "relevant" chunks) -> generation step (augments prompt with contextual chunks and generate LLM answer grouded in contextual chunks)

### What is a "relevant" document?

* On chunks
  * Need to split docs into smaller parts for serveral reasons (model context window size, context dillution, what else?)
  * Make chunks information dense as possible -> strip chunks of whitespace
  * Add metadata so that LLM can cite chunks in responses
* On indexing chunks - in document store
* On searching for relevant chunks
    * Need a whole bit on BM25 and semantic indexing. I read about hybrid approaches at scale
    * Apparently pure embeedding-based retrieval without keyword-based retrieval will be inadequate
* Should I cover chunking strategies depending on document type?
  * Chunking with overlap to limit "important" info being split between two chunks - what does research say? I saw something about overlap not being as effective as people think
* Ingesting PDFs
  * LlamaParse - AI based document parsing that can extract tables and images and convert them into formats like Markdown
  * Screenshot of PDF to multimodal LLM
* On the importance of contextual retrieval* On the importance of contextual retrieval* On the importance of contextual retrieval* On the importance of contextual retrieval* On the importance of contextual retrieval* On the importance of contextual retrieval* On the importance of contextual retrieval* On the importance of contextual retrieval

#### What does a RAG prompt look like? 

Example prompt showing "grouding" LLM's response by injecting the "retrieved" relevant docs:

* Orders are the "relevant docs" injected into the prompt before foundational model sees it
* "The computer you sent me is missing a charger. Can you send me a replacement?" is the user's prompt
* "Say none of them if the message does not match any of the above orders." - apparently important. Assume it's to reduce hallucinations. 


> Here’s the list of recent orders from this customer:
>
>Order #5678 – Apple iPhone 15 Pro (256GB, Titanium Blue) with a tempered glass screen protector and MagSafe case.
>
>Order #7832 – Sony WH-1000XM5 Noise-Canceling Headphones (Black) with a travel carrying case and USB-C charging cable.
>
>Order #9210 – ASUS ROG Strix Gaming Laptop (Intel i9, RTX 4080, 32GB RAM, 1TB SSD) with an RGB mechanical keyboard and gaming mouse.
>
>Which of these order IDs is the customer referring to in the following email?
>
>…
>
>The computer you sent me is missing a charger. Can you send me a replacement?
>
>…
>
>Say none of them if the message does not match any of the above orders.


* TBC - modify silly example, injecting contextual docs directly into the prompt.  

##### LlamaIndex example of prompt

```python
# instruction
messages = [
    ChatMessage(
        role="system", 
        content="Use the following text to answer the given question."
    )
]
# context
messages += [
    ChatMessage(role="system", content=node.text) for node in retrieved_nodes
]
# query
messages += [
    ChatMessage(role="user", content=query)
]
```


