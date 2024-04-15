import uuid

import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

import config
from vertex_ai import constants

vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
generation_model = ImageGenerationModel.from_pretrained("imagegeneration@006")


def generate_icon(keywords_list: list) -> str:
    """
    Generate an icon from provided prompt.
    :param keywords_list: Keywords that we got from users.
    :return: generated image unique id
    """
    keywords = ", ".join(keywords_list)
    prompt = constants.IMAGEN_MODEL_PROMPT.replace("[keywords]", keywords)
    icon_id = uuid.uuid4()

    response = generation_model.generate_images(
        prompt=prompt,
        safety_filter_level="block_most",
    )

    response.images[0].save(f"./outputs/photos/{icon_id}.png")
    return icon_id
