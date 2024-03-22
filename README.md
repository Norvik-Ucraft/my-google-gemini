# my-google-gemini

## Models List
* `chat-bison-001`: A legacy text-only model optimized for chat conversations.
  * `input_token_limit`: 4096
  * `output_token_limit`: 1024
  * `temperature`: 0.25
* `text-bison-001`: A legacy model that understands text and generates text as an input.
  * `input_token_limit`: 8196
  * `output_token_limit`: 1024
  * `temperature`: 0.7
* `embedding-gecko-001`: Obtain a distributed representation of a text.
  * `input_token_limit`: 1024
  * `output_token_limit`: 1
  * `temperature`: None
* `gemini-1.0-pro`: The best model for scaling across a wide range of tasks.
  * `input_token_limit`: 30720
  * `output_token_limit`: 2048
  * `temperature`: 0.9
* `gemini-1.0-pro-001`: The best model for scaling across a wide range of tasks. This is stable model that supports tuning.
  * `input_token_limit`: 30720
  * `output_token_limit`: 2048
  * `temperature`: 0.9
* `gemini-1.0-pro-latest`: The best model for scaling across wide range of tasks. This is the latest model.
  * `input_token_limit`: 30720
  * `output_token_limit`: 2048
  * `temperature`: 0.9
* `gemini-1.0-pro-vision-latest`: The best image understanding model to handle a broad range of applications.
  * `input_token_limit`: 12288
  * `output_token_limit`: 4096
  * `temperature`: 0.4
* `gemini-pro`: The best model for scaling across a wide range of tasks.
  * `input_token_limit`: 30720
  * `output_token_limit`: 2048
  * `temperature`: 0.9
* `gemini-pro-vision`: The best image understanding model to handle a broad range of applications.
  * `input_token_limit`: 12288
  * `output_token_limit`: 4096
  * `temperature`: 0.4
* `embedding-001`: Obtain a distributed representation of a text.
  * `input_token_limit`: 2048
  * `output_token_limit`: 1
  * `temperature`: None
* `aqa`: Model trained to return answers to questions that are grounded in provided sources, along with estimating answerable probability.
  * `input_token_limit`: 7168
  * `output_token_limit`: 1024
  * `temperature`: 0.2
