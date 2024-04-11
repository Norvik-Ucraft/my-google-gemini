import os

import vertexai
from dotenv import load_dotenv
from vertexai.preview.generative_models import GenerativeModel, GenerationConfig

import config

load_dotenv()

os.getenv("GOOGLE_APPLICATION_CREDENTIALS")


def generate_text() -> str:
    vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
    multimodal_model = GenerativeModel("gemini-1.5-pro-preview-0409")

    generation_config = GenerationConfig(max_output_tokens=10, temperature=0.5, stop_sequences="\n")

    response = multimodal_model.generate_content(
        contents=["continue the story: once upon a time there was a cat."], generation_config=generation_config
    )
    return response


print(generate_text())
