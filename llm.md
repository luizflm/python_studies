# What are LLMs?
Large language models (LLMs) are a category of deep learning models trained on immense amounts of data, making them capable of understanding and generating natural language and other types of content to perform a wide range of tasks. LLMs are built on a type of neural network architecture called a transformer which excels at handling sequences of words and capturing patterns in text.

LLMs work as giant statistical prediction machines that repeatedly predict the next word in a sequence. They learn patterns in their text and generate language that follows those patterns.

LLMs represent a major leap in how humans interact with technology because they are the first AI system that can handle unstructured human language at scale, allowing for natural communication with machines. Where traditional search engines and and other programmed systems used algorithms to match keywords, LLMs capture deeper context, nuance and reasoning. LLMs, once trained, can adapt to many applications that involve interpreting text, like summarizing an article, debugging code or drafting a legal clause. When given agentic capabilities, LLMs can perform, with varying degrees of autonomy, various tasks that would otherwise be performed by humans.

LLMs are the culmination of decades of progress in natural language processing (NLP) and machine learning research, and their development is largely responsible for the explosion of artificial intelligence advancements across the late 2010s and 2020s. Popular LLMs have become household names, bringing generative AI to the forefront of the public interest. LLMs are also used widely in enterprises, with organizations investing heavily across numerous business functions and use cases.

LLMs are easily accessible to the public through interfaces like Anthropic’s Claude, Open AI’s ChatGPT, Microsoft’s Copilot, Meta’s Llama models, and Google’s Gemini assistant, along with its BERT and PaLM models.

# Pretraining large language models
Training starts with a massive amount of data—billions or trillions of words from books, articles, websites, code and other text sources. Data scientists oversee cleaning and pre-processing to remove errors, duplication and undesirable content.  
This text is broken down into smaller, machine-readable units called “tokens,” during a process of “tokenization.” Tokens are smaller units such as words, subwords or characters. This standardizes the language so rare and novel words can be handled consistently.

LLMs are initially trained with self-supervised learning, a machine learning technique that uses unlabeled data for supervised learning. Self-supervised learning doesn’t require labeled datasets, but it’s closely related to supervised learning in that it optimizes performance against a "ground truth." In self-supervised learning, tasks are designed such that ground truth can be inferred from unlabeled data. Instead of being told what the “correct output” is for each input, as in supervised learning, the model tries to find patterns, structures or relationships in the data on its own.

# Fine-tuning large language models
After training (or in the context of additional training, “pretraining”), LLMs can be fine-tuned to make them more useful in certain contexts. For example, a foundational model trained on a large dataset of general knowledge can be fine-tuned on a corpus of legal Q&As in order to create a chatbot for the legal field.

## Supervised fine-tuning
Fine-tuning most often happens in a supervised context with a much smaller, labelled dataset. The model updates its weights to better match the new ground truth (in this case, labeled data).

While pretraining is intended to give the model broad general knowledge, fine-tuning adapts a general-purpose model to specific tasks like summarization, classification or customer support. These functional adaptations represent new types of tasks. Supervised fine-tuning produces outputs closer to the human-provided examples, requiring far fewer resources than training from scratch.

Supervised fine-tuning is also useful for domain-specific customization, such as training a model on medical documents so it has the ability to answer healthcare-related questions. 

## Reinforcement learning from human feedback
[TO LEARN]