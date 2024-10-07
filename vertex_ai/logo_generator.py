import uuid
import logging

import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

import config
from vertex_ai import constants

vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
generation_model = ImageGenerationModel.from_pretrained(constants.IMAGEN_3_MODEL)


def generate_logo(keywords_list: list) -> str:
    """
    Generate a logo based on the provided keywords.
    :param keywords_list: Provided list of business keywords.
    :return: PNG path.
    """
    logging.info("Starting to generate logo...")
    keywords = " ".join(keywords_list)

    logo_generator = generation_model.generate_images(
        prompt=f"Generate a creative minimalistic logo for my website that captures: {keywords}. With fill-in styling on a white background. The icon should be simple yet artistic, with unique design elements that make it stand out, using only black color without any text or additional content.",
        aspect_ratio="1:1",
        person_generation="dont_allow",
        safety_filter_level="block_some",
        negative_prompt="no lettering, no shadows",
    )

    image_id = str(uuid.uuid4())
    image_path = f"./generated_logos/logo-{image_id[:4]}.png"
    logo_generator.images[0].save(image_path)

    return image_path
