# Chat API

Pico AI Homelab supports the following OpenAI and Ollama-compatible endpoints for chat:

* `v1/chat/`completions OpenAI-compatible chat API
* `api/chat` Ollama-compatible chat API
* `api/generate` Ollama-compatible completion API

These endpoints are conform OpenAI and Ollama. Pico supports message content types `text`, `image_url`, and `video_url`.

Pico supports both LLM and VLM models. To discover which models have been downloaded and are available to clients, use the [models API](https://pico-1.gitbook.io/homelab/basics/models-api).

### Request

<mark style="color:green;">`POST`</mark> `/v1/chat`

<mark style="color:green;">`POST`</mark> `/api/chat`

<mark style="color:green;">`POST`</mark> `/api/generate`

<table><thead><tr><th width="221">Name</th><th width="159">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>model</code></td><td>String</td><td>Name of the embeddings model, e.g. <code>all-MiniLM-L6-v2</code></td></tr><tr><td><code>messages</code></td><td>Array of messages</td><td>String or strings to embed</td></tr><tr><td><code>stream</code></td><td>Optional boolean</td><td>If true or nil, the response will be streamed to the client per token</td></tr><tr><td><code>reasoning</code></td><td>Optional enum</td><td>See reasoning</td></tr><tr><td><code>chat_template_kwargs</code></td><td>Optional dictionary</td><td>See reasoning</td></tr><tr><td><code>max_tokens</code></td><td>Optional integer</td><td>Deprecated, use <code>max_completion_tokens</code> instead.</td></tr><tr><td><code>max_completion_tokens</code></td><td>Optional integer</td><td>Upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens</td></tr><tr><td><code>temperature</code></td><td>Optional float</td><td>What sampling temperature to use</td></tr><tr><td><code>frequency_penalty</code></td><td>Optional float</td><td></td></tr><tr><td><code>top_p</code></td><td>Optional float</td><td></td></tr><tr><td><code>user</code></td><td>Optional string</td><td>Ignored by Pico</td></tr><tr><td><code>format</code></td><td>Optional string</td><td>Ignored by Pico</td></tr><tr><td><code>options</code></td><td>Optional object</td><td>See Ollama options</td></tr><tr><td><code>think</code></td><td>Optional boolean</td><td>Enables or disables reasoning (conform Ollama API). Available from 1.1.18</td></tr></tbody></table>

#### Reasoning

Pico supports the OpenAI, vLLM, and Ollama way of enabling and disabling reasoning. The `reasoning` (OpenAI API-compatible) and `enable_thinking` options (vLLM API-compatible) are supported in Pico 1.1.14 and later, the `think` option (Ollama API-compatible) from 1.1.18.

{% hint style="info" %}
Note that setting the reasoning options is optional. If no reasoning option is supplied, the model will use its default settings, which is often reasnoning enabled.
{% endhint %}

#### OpenAI-compatible Reasoning

Unlike OpenAI, Pico does not implement reasoning levels (`low`, `medium`, `high`); only binary ON or OFF states are supported. Requests specifying `low` will be interpreted by Pico as Reasoning = Off. Note that Pico also supports non-OpenAI standard values `on`, `off`, and `none` .

| Name      | Type            | Description              |
| --------- | --------------- | ------------------------ |
| `effort`  | Enum            | See below                |
| `summary` | Optional string | This property is ignored |

<table><thead><tr><th width="142">Name</th><th>Description</th></tr></thead><tbody><tr><td><code>low</code></td><td>Pico interprets this condition as: Reasoning mode disabled</td></tr><tr><td><code>medium</code></td><td>Pico interprets this condition as: Reasoning mode enabled</td></tr><tr><td><code>high</code></td><td>Pico interprets this condition as: Reasoning mode enabled</td></tr><tr><td><code>on</code></td><td>Reasoning mode enabled</td></tr><tr><td><code>off</code></td><td>Reasoning mode disabled</td></tr><tr><td><code>none</code></td><td>Reasoning mode disabled</td></tr></tbody></table>

#### vLLM-compatible Reasoning

Alternatively, use the vLLM API by setting key `enable_thinking` to `true` or `false` in `chat_template_kwargs`&#x20;

#### Ollama-compatible Reasoning

`think` is an optional boolean.&#x20;

{% hint style="info" %}
As of Pico AI Server 1.1.18, the `thinking` field in the response is **not** supported yet, meaning that thinking responses will be streamed as a regular response.
{% endhint %}
