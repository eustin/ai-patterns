---
title: Home
layout: home
nav_order: 1
---

{: .highlight }
100% Certified Organic!

Hello, dear reader.

My name is Justin. I go through phases where I am intensely interested in a topic and obsess over it 24/7, often starting at 3AM when I wake up thinking about the topic until I fall asleep on the couch at 9PM. These notes are the result of such a period.

Here are a bunch of AI design patterns. Most patterns come from two great books:

* **Generative AI Design Patterns** by Valliappa Lakshmanan and Hannes Hapke
* **Platform Engineering for Artificial Intelligence** by Duy V. Nguyen (despite its weird wavy charts - you will see what I mean later)

Some of the other patterns come from official documentation. I will try my best to cite the source accurately for each pattern.

I feel "funny" writing about "AI". The hype is irrational and causing many businesses to make harmful decisions that hurt their employees. However, I do believe in solid engineering. That's what I was obsessing over and that's what I want to share with you!

Finally, **I am not an expert in this field**. If anyone claims they are an expert in this rapidly evolving space or brags that their "model" is bigger than someone else's, run. Don't buy into **their** hype. **You** have **real** intelligence. Use it to learn from those who practice the craft rather than from a spokesperson selling a product.

# Personal links

You can find me at ["everyone's least favourite place in the world where we're forced to 'career-peacock' about synergies and be 'humbled and excited' to announce things no one actually gives a crap about".](https://www.linkedin.com/in/justin-m-evans/) (It's just a job, amirite?)

I also (very rarely) write [a blog](https://embracingtherandom.com). I've found ragging on the necessary evil that is LinkedIn cathartic. I also want to rediscover exploring nerdy things "just 'cause", so I want to start writing again. Here are some of my favourite posts. Most of them are unfinished because writing them is an all-encompassing task that eventually tires me out: 

* [Statistical significance intuition](https://embracingtherandom.com/experiments/python/statistical-significance-intuition/): It's a tricky thing to explain. I tried my best to explain it to someone who has no statistical training.
* Learning to Rank post: Embeddings are so hot right now, but this old timer was "embedding sh*t" long before you young'uns.
  * [Part one](https://embracingtherandom.com/machine-learning/tensorflow/ranking/deep-learning/learning-to-rank-part-1/)
  * [Part two](https://embracingtherandom.com/machine-learning/tensorflow/ranking/deep-learning/learning-to-rank-part-2/)
* [Answering a classic interview question involving socks](https://embracingtherandom.com/probability/python/i-have-a-problem-with-socks/)
* Obsessing over Dijkstra and trying to use the "single source shortest path" algorithm to lose weight. Dijkstra opened my eyes to an exciting world where problems could be described using algorithms. I was obsessed about it for many months.
  * [Part one](https://embracingtherandom.com/r/graphs/i-walk-the-train-line-part-un/)
  * [Part two](https://embracingtherandom.com/r/graphs/i-walk-the-train-line-part-deux/)
  * [Part three](https://embracingtherandom.com/r/graphs/algorithms/apis/I-walk-the-train-line-part-trois/)
  * [Part four](https://embracingtherandom.com/r/graphs/algorithms/I-walk-the-train-line-part-quatre/)

# The recipe book

A taste of things to come.

## Increasing LLM response accuracy

* LLM needs access to private data to produce useful responses
* AI doesn't cite sources
* LLM confidently generates bullsh*t 
* Small factual errors in user domain are a legal risk
* Document retrieval fails when user's jargon doesn't exactly match docs
* LLM forgets previous conversation context
* LLM responses are generic and don't capture "brand voice"

## Scaling and performance issues

* Inference latency is too high for real-time app
* RAG inference latency increasing as index grows
* Limits of system (e.g. number of concurrent users) unknown
* Bad input data format (e.g. bad JSON and SQL) force multiple generation loops
* GPU utilisation low due to varying prompt lengths causing breakdown in traditional batching
* Batch pipelines too slow during seasonal traffic spikes
* Our services crash when a provider has an outage

## Cost management

* Token costs unpredictable and vary dramatically across different teams
* Costs driven by (near) identical user requests
* No incentive for teams to optimise costs because everything billed to generic cost bucket
* Full fine-tuning of large model cost-prohibitive for our org
* Cloud bill dominated by routing everything to powerful but expensive large models

## MLOps and data lifecycle

* Training model metrics are nothing like production model metrics
* Characteristics of model training data are nothing like data in production today
* ML pipeline components so coupled that making updates is risky and slow
* Large sync lag between application database and separate vector database making it unsuitable for realtime use cases
* GPUs during model training sitting idle because of I/O bottleneck in preparing training data
* Carefully engineered prompts break each time model provider updates their model

## Security and privacy

* LLM vulnerable to prompt injection and safety bypasses
* Retrieved documents (in RAG) contain PII that should have been redacted
* Manual compliance is a bottleneck to fast dev cycles
* Managing thousands of indices (for RAGs) for "tenants" (i.e. customers in SaaS) is an operational nightmare
* AI infrastructure vulnerable to attacker compromising low-security node (like public API) to gain access to internal-only assets (e.g training data and GPU clusters)
* We don't have a "paper trail" for our data, prompts and model versions
* Managing the plumbing of LLM calls across fragmented apps creates security holes

## Management stuff

* Platform team has become ivory tower that's disconnected from product (and vice versa)

