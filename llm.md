# What are LLMs?
Large language models (LLMs) are a category of deep learning models trained on immense amounts of data, making them capable of understanding and generating natural language and other types of content to perform a wide range of tasks. 

LLMs are built on a type of neural network architecture called a **transformer** which excels at handling sequences of words and capturing patterns in text.

LLMs work as giant statistical prediction machines that repeatedly predict the next word in a sequence. They learn patterns in their text and generate language that follows those patterns.

LLMs represent a major leap in how humans interact with technology because they are the first AI system that can handle unstructured human language at scale, allowing for natural communication with machines. Where traditional search engines and and other programmed systems used algorithms to match keywords, LLMs capture deeper context, nuance and reasoning. LLMs, once trained, can adapt to many applications that involve interpreting text, like summarizing an article, debugging code or drafting a legal clause. When given agentic capabilities, LLMs can perform, with varying degrees of autonomy, various tasks that would otherwise be performed by humans.

LLMs are easily accessible to the public through interfaces like Anthropic’s Claude, Open AI’s ChatGPT, Microsoft’s Copilot, Meta’s Llama models, and Google’s Gemini assistant, along with its BERT and PaLM models.

# Pretraining large language models
Training starts with a massive amount of data—billions or trillions of words from books, articles, websites, code and other text sources. Data scientists oversee cleaning and pre-processing to remove errors, duplication and undesirable content.  

This text is broken down into smaller, machine-readable units called “tokens,” during a process of “tokenization.” Tokens are smaller units such as words, subwords or characters. This standardizes the language so rare and novel words can be handled consistently.

LLMs are initially trained with self-supervised learning, a machine learning technique that uses unlabeled data for supervised learning. 

Self-supervised learning doesn’t require labeled datasets, but it’s closely related to supervised learning in that it optimizes performance against a "ground truth." In self-supervised learning, tasks are designed such that ground truth can be inferred from unlabeled data. Instead of being told what the “correct output” is for each input, as in supervised learning, the model tries to find patterns, structures or relationships in the data on its own.

## Self-attention
The model passes the tokens through a transformer network. Transformer models, introduced in 2017, are useful due to their self-attention mechanism, which allows them to “pay attention to” different tokens at different moments. 

Self-attention is useful in part because it allows the AI model to calculate the relationships and dependencies between tokens, especially ones that are distant from one another in the text.

Transformer architectures also allow for parallelization, making the process much more efficient than previous methods. These qualities allowed LLMs to handle unprecedentedly large datasets.

Once text is split into tokens, each token is mapped to a vector of numbers called an embedding. Neural networks consists of layers of artificial neurons, where each neuron performs a mathematical operation. Transformers consist of many of these layers, and at each, the embeddings are slightly adjusted, becoming richer contextual representations from layer to layer.

The goal in this process is for the model to learn semantic associations between words, so that words like “bark” and “dog” appear closer together in vector space in an essay about dogs than “bark” and “tree” would, based on the surrounding dog-related words in the essay. Transformers also add positional encodings, which give each token information about its place in the sequence.

To compute attention, each embedding is projected into three distinct vectors using learned weight matrices: a query, a key, and a value. The query represents what a given token is “seeking,” the key represents the information that each token contains, and the value “returns” the information from each key vector, scaled by its respective attention weight.

Alignment scores are then computed as the similarity between queries and keys. These scores, once normalized into attention weights, determine how much of each value vector flows into the representation of the current token. This process allows the model to flexibly focus on relevant context while ignoring less important tokens (like “tree”).

Self-attention thus creates “weighted” connections between all tokens more efficiently than earlier architectures could. The model assigns weights to each relationship between the tokens. LLMs can have billions or trillions of these weights, which are one type of LLM parameter, the internal configuration variables of a machine learning model that control how it processes data and makes predictions. The number of parameters refers to how many of these variables exist in a model, with some LLMs containing billions of parameters. So-called small language models are smaller in scale and scope with comparatively few parameters, making them suitable for deployment on smaller devices or in resource-constrained environments.

During training, the model makes predictions across millions of examples drawn from its training data, and a loss function quantifies the error of each prediction. Through an iterative cycle of making predictions and then updating model weights through backpropagation and gradient descent, the model “learns” the weights in the layers that produce the query, key and value vectors.

Once those weights are sufficiently optimized, they’re able to take in any token’s original vector embedding and produce query, key and value vectors for it that, when interacting with the vectors generated for all the other tokens, will yield “better” alignment scores that in turn result in attention weights which help the model produce better outputs. The end result is a model that has learned patterns in grammar, facts, reasoning structures, writing styles and more.