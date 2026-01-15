# Embeddings API

{% hint style="info" %}
The embeddings API is available from Pico 1.1.12 and newer
{% endhint %}

### Supported models

Unlike LLMs, embedding models are downloaded and loaded into memory dynamically when required. Pre-downloading and persistent caching of embedding models is neither necessary nor supported in Pico AI Server. Due to their compact size, embedding models can be efficiently retrieved on demand.&#x20;

By default, embedding models are stored in `<base-directory>/Embeddings` as specified in the **Models** section of **Settings**.

Embedding models leverage the CoreML-based [Swift-Embeddings](https://github.com/apple/swift-embeddings) library. For more implementation details, refer to the project’s GitHub repository.

<table><thead><tr><th width="465">Name</th><th>Architecture</th></tr></thead><tbody><tr><td><code>all-MiniLM-L6-v2</code></td><td>BERT </td></tr><tr><td><code>msmarco-bert-base-dot-v5</code></td><td>BERT</td></tr><tr><td><code>LaBSE</code></td><td>BERT</td></tr><tr><td><code>gte-base</code></td><td>BERT</td></tr><tr><td><code>bert-base-uncased</code></td><td>BERT</td></tr><tr><td><code>mxbai-embed-large-v1</code></td><td>BERT</td></tr><tr><td><code>roberta-base</code></td><td>RoBERTa </td></tr><tr><td><code>xlm-roberta-base</code></td><td>XLM-RoBERTa</td></tr><tr><td><code>multilingual-e5-large</code></td><td>XLM-RoBERTa</td></tr><tr><td><code>multilingual-e5-small</code></td><td>XLM-RoBERTa</td></tr><tr><td><code>paraphrase-multilingual-mpnet-base-v2</code></td><td>XLM-RoBERTa</td></tr><tr><td><code>xlm-roberta-base-multilingual-en-ar-fr-de-es-tr-it</code></td><td>XLM-RoBERTa</td></tr><tr><td><code>clip-vit-base-patch16</code></td><td>CLIP</td></tr><tr><td><code>clip-vit-base-patch32</code></td><td>CLIP</td></tr><tr><td><code>clip-vit-large-patch14</code></td><td>CLIP</td></tr><tr><td><code>glove-twitter-25</code></td><td>Word2Vec</td></tr><tr><td><code>glove-twitter-50</code></td><td>Word2Vec</td></tr><tr><td><code>glove-twitter-100</code></td><td>Word2Vec</td></tr><tr><td><code>glove-twitter-200</code></td><td>Word2Vec</td></tr><tr><td><code>potion-base-2M</code></td><td>Model2Vec</td></tr><tr><td><code>potion-base-4M</code></td><td>Model2Vec</td></tr><tr><td><code>potion-base-8M</code></td><td>Model2Vec</td></tr><tr><td><code>potion-retrieval-32M</code></td><td>Model2Vec</td></tr><tr><td><code>potion-base-32M</code></td><td>Model2Vec</td></tr><tr><td><code>M2V_base_output</code></td><td>Model2Vec</td></tr><tr><td><code>M2V_base_output</code></td><td>Static</td></tr><tr><td><code>static-similarity-mrl-multilingual-v1</code></td><td>Static</td></tr></tbody></table>

### OpenAI-compatible endpoint

#### Request

<mark style="color:green;">`POST`</mark> `/v1/embeddings`

| Name              | Type                       | Description                                           |
| ----------------- | -------------------------- | ----------------------------------------------------- |
| `model`           | String                     | Name of the embeddings model, e.g. `all-MiniLM-L6-v2` |
| `input`           | String or array of strings | String or strings to embed                            |
| `encoding_format` | Optional string            | This property is ignored                              |
| `user`            | Optional string            | This property is ignored                              |

#### Response

| Name     | Type                       | Description                                           |
| -------- | -------------------------- | ----------------------------------------------------- |
| `model`  | String                     | Name of the embeddings model, e.g. `all-MiniLM-L6-v2` |
| `object` | String                     | Always `list`                                         |
| `data`   | Array of embedding objects | See embedding objects                                 |

| Name        | Type            | Description            |
| ----------- | --------------- | ---------------------- |
| `index`     | Integer         | Index of the embedding |
| `object`    | String          | Always `embedding`     |
| `embedding` | Array of floats | Embedding              |

### Ollama-compatible endpoint

#### Request

<mark style="color:green;">`POST`</mark> `/api/embed`

| Name    | Type                       | Description                                           |
| ------- | -------------------------- | ----------------------------------------------------- |
| `model` | String                     | Name of the embeddings model, e.g. `all-MiniLM-L6-v2` |
| `input` | String or array of strings | String or strings to embed                            |

#### Response

| Name                | Type                     | Description                               |
| ------------------- | ------------------------ | ----------------------------------------- |
| `model`             | String                   | The model used to generate the embeddings |
| `embeddings`        | Array of array of floats | The generated embeddings                  |
| `total_duration`    | Integer                  | Always `nil`                              |
| `load_duration`     | Integer                  | Always `nil`                              |
| `prompt_eval_count` | Integer                  | Always `nil`                              |
