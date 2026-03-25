---
title: LLM response accuracy problems
nav_order: 2
---

Prerequisites:
* What is a foundational model? 
  * General purpose GenAI models like GPT, Gemini, Claude family etc.
  * Pattern is to use the GenAI models that are agnostic models to build something more "specific" to use case, without training model from scratch.


## Problem:

Chapter 3 Gen ai book:
> Foundational models are closed systems that are limited by their training data. In many cases, you’ll need to give a foundational model additional information. For example, the information may be based on recent events that had not occurred when the foundational model was being trained, or the information may have been private, confidential, or otherwise unavailable to the foundational model trainers.

> It’s impractical to retrain an LLM with additional knowledge or even perform continuing pretraining (CPT) on a foundational model to add knowledge to it. The cost of even a single training run is significant, and information changes so fast that CPT would have to be done very frequently. These costs can add up to tens of millions of dollars,1 so you’ll typically want to use a foundational model as is and add knowledge to it at runtime.

On static knowledge cutoff:
* Can't access info beyond training data collection cutoff, resulting in outdated or inaccurate responses.

On model capacity limits:
* Despite foundational models often being huge, they still have limits as to how much info they can "store"

Lack of access to private data:
* Foundational model trained on "open" data and doesn't include "private" data that might make a Foundational model more useful for an internal use case (e.g. access to internal company reports

On hallucinations:
* LLMs are creative and will end up hallucinating stuff beyond training data.

### Example: 

* TBC - create a silly example, choosing foundational model with training data cut off date in the past, ask it some question about who won the 2026 "something" competition? ans see it hallucinate a response.


### Solution:

Use a RAG to give the foundational model contextual info at runtime.

Ask the LLM to generate response based on a set of "trusted" documents:
* Can "augment" foundatinal model's knowledge by injecting up to date contextual docs into promopt before LLM responds
* Augmenting with external knowledge not in training data overcomes model capacity limits
* Can inject private data at runtime only, solving many privacy issues while making LLM responses more relevant to sensitive internal use cases
* Hallucinations reduced by injecting "relevant" information (i.e. the retrieved documents) and asking it to cite specific sources

#### Basic RAG architecture

* Start with where we are going to end
* Create simpler version of Figure 3-2 RAG architecture
* User query -> Question-answering pipeline -> retrieval step (searches document store for "relevant" chunks) -> generation step (augments prompt with contextual chunks and generate LLM answer grouded in contextual chunks)

#### What is a "relevant" document?

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


