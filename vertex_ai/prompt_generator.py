import os

import vertexai
from dotenv import load_dotenv
from vertexai.preview.generative_models import GenerativeModel

import config

load_dotenv()

os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

prompt = """
Generate one prompt for imagen model to represents pure icon or a symbol of coffee which will be used later in a logo. \
** Important rules to follow: \
1. The icon should always be with white background. \
2. The icon should always be without any text and without any shadows. \
Return the prompt without any extra text or description.
"""


def generate_text(model_prompt: str) -> str:
    vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
    multimodal_model = GenerativeModel("gemini-1.5-pro-preview-0409")

    # ToDo Configure the model if it's necessary
    # generation_config = GenerationConfig(temperature=1.)

    response = multimodal_model.generate_content(contents=[model_prompt])
    return response.text
