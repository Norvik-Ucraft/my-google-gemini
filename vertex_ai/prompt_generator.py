import os

import vertexai
from dotenv import load_dotenv
from vertexai.preview.generative_models import GenerativeModel, GenerationConfig

import config
from vertex_ai import constants

load_dotenv()

os.getenv("GOOGLE_APPLICATION_CREDENTIALS")


def generate_prompt(keywords: list) -> str:
    """
    Generate a prompt based on keywords.
    :param keywords: list of keywords provided from user.
    :return: Generated prompt based on keywords.
    """
    vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
    multimodal_model = GenerativeModel("gemini-1.5-pro-preview-0409")

    # ToDo Configure the model if it's necessary
    generation_config = GenerationConfig(max_output_tokens=32, stop_sequences="\n")

    response = multimodal_model.generate_content(
        contents=[f"{constants.PROMPT_GENERATOR_PROMPT}\nKeywords: {keywords}"], generation_config=generation_config
    )
    return response.text
