# Models API

To discover the available models on a Pico AI Homelab instance, use the Models API. Pico comes with two different endpoints for models: one is compatible with Ollama, the other&#x20;

Pico AI Homelab will only list models that have been downloaded. Unlike Ollama, Pico AI Homelab does not permit client apps to download models directly from the internet. Instead, the Pico administrator can download models through the Pico Settings. This is because many chat clients have non-MLX models hardcoded, which are incompatible with Pico AI Homelab.

* `v1/models`OpenAI-compatible list of available models
* `api/tags` Ollama-compatible list of available models
* `api/ps` Endpoint added for Ollama compatibility. Returns an empty object.
* `api/show` Endpoint added for Ollama compatibiltiy. Returns basic model information

{% hint style="info" %}
The name of the model is always the model's repository name on Hugging Face. For example if a model's URL is `https://huggingface.co/mlx-community/DeepSeek-R1-Distill-Llama-8B-3bit` then then model's name is `DeepSeek-R1-Distill-Llama-8B-3bit`
{% endhint %}

## OpenAI-compatible endpoint

<mark style="color:green;">`GET`</mark> `/v1/models`

OpenAI-compatible list of available models

**Headers**

| Name         | Value              |
| ------------ | ------------------ |
| Content-Type | `application/json` |

**Body**

This endpoint expects an empty body

#### Response

| Name     | Type             | Description            |
| -------- | ---------------- | ---------------------- |
| `data`   | Array of objects | Array of model objects |
| `object` | String           | Always `list`          |

| Name       | Type                  | Description                                               |
| ---------- | --------------------- | --------------------------------------------------------- |
| `id`       | String                | Name of the model                                         |
| `created`  | Date (Unix timestamp) | Last modified date from Hugging Face (on 1.1.3 and newer) |
| `object`   | String                | Always `model`                                            |
| `owned_by` | String                | Always `Pico AI Homelab`                                  |

{% tabs %}
{% tab title="200" %}

```json
{
    "object":"list",
    "data": 
    [
        {
            "object": "model",
            "id": "DeepSeek-R1-Distill-Qwen-14B-8bit",
            "created": 1740592086,
            "owned_by": "Pico AI Homelab"
        },
        {
            "id": "Llama-3.2-3B-Instruct-bf16",
            "created": 1727311814,
            "owned_by": "Pico AI Homelab",
            "object": "model"
        },
    ]
}
```

{% endtab %}
{% endtabs %}

## Ollama-compatible endpoints

<mark style="color:green;">`GET`</mark> `/api/tags`

OpenAI-compatible list of available models

**Body**

This endpoint expects an empty body

**Headers**

| Name         | Value              |
| ------------ | ------------------ |
| Content-Type | `application/json` |

**Response**

| Name     | Type             | Description            |
| -------- | ---------------- | ---------------------- |
| `models` | Array of objects | Array of model objects |

| Name          | Type            | Description                                               |
| ------------- | --------------- | --------------------------------------------------------- |
| name          | String          | The name of the model                                     |
| `size`        | Number          | For now always set to `1000`                              |
| `modified_at` | Date (ISO 8601) | Last modified date from Hugging Face (on 1.1.3 and newer) |
| `digest`      | String          | The SHA digest from Hugging Face                          |
| `model`       | String          | The model's repository name on HuggingFace                |
| `details`     | Object          |                                                           |

| Name                 | Type   | Description                                                       |
| -------------------- | ------ | ----------------------------------------------------------------- |
| `format`             | String | Always returns `mlx`                                              |
| `parent_model`       | String | For now always returns an empty string                            |
| `family`             | String | Model family name, e.g. `DeepSeek R1`                             |
| `quantization_level` | String | Quantization, e.g. `fp16`, `bf16`, `8bit`, `6bit`, `4bit`, `3bit` |
| `parameter_size`     | String | Parameter size of the model                                       |

**Response**

{% tabs %}
{% tab title="200" %}

<pre class="language-json"><code class="lang-json">{
<strong>    "models":
</strong>    [
        {
            "model": "mlx-community\\/DeepSeek-R1-Distill-Qwen-14B-8bit"
            "digest": "2fbbaeaa759a51ea55b6baba8574e340a0a71200",
            "name": "DeepSeek-R1-Distill-Qwen-14B-8bit",
            "size": 15705513889,
            "modified_at": "2025-02-26T17:48:06Z",
            "details": {
                "parameter_size": "14B",
                "family": "DeepSeek R1",
                "parent_model": "",
                "quantization_level": "8bit",
                "format": "mlx"
             },  
        },
        {
            "name": "Llama-3.2-3B-Instruct-bf16",
            "size": 6425528971,
            "digest": "6d88ba43024fef71b10e52e101c7cd4598322601",
            "modified_at": "2024-09-26T00:50:14Z",
            "model": "mlx-community\\/Llama-3.2-3B-Instruct-bf16",
            "details": {
                "parent_model": "",
                "parameter_size": "3B",
                "family": "Llama 3.2",
                "format": "mlx",
                "quantization_level": "bf16"
            }
        }
    ]
}
</code></pre>

{% endtab %}
{% endtabs %}

## Ollama PS

<mark style="color:green;">`GET`</mark> `/api/ps`

Stub for compatibilty with Ollama

**Headers**

| Name         | Value              |
| ------------ | ------------------ |
| Content-Type | `application/json` |

**Body**

This endpoint expects an empty body

#### Response

| Name         | Type   | Description      |
| ------------ | ------ | ---------------- |
| `parameters` | String | Always empty     |
| `template`   | String | Always `Unknown` |
| `license`    | String | Always `Unknown` |
| `modelfile`  | String | Always `Unknown` |

**Response**

{% tabs %}
{% tab title="200" %}

```json
{
  "parameters":"",
  "template":"Unknown",
  "license":"Unknown",
  "modelfile":"Unknown"
}
```

{% endtab %}
{% endtabs %}

### Ollama Show

This endpoint returns nothing
