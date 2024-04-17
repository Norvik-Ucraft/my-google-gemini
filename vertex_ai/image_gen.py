import uuid
import logging
from typing import Optional

import vertexai
from PIL import Image
from vertexai.preview.vision_models import ImageGenerationModel

import config
from vertex_ai import constants

vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
generation_model = ImageGenerationModel.from_pretrained("imagegeneration@006")


def generate_icon(keywords_list: list) -> Optional[str]:
    """
    Generate an icon from provided prompt.
    :param keywords_list: Keywords that we got from users.
    :return: Generated image unique id
    """
    try:
        keywords = ", ".join(keywords_list)
        prompt = constants.TEMP_PROMPT.replace("[keywords]", keywords)
        icon_id = uuid.uuid4()

        response = generation_model.generate_images(
            prompt=prompt, safety_filter_level="block_most", negative_prompt="low quality", aspect_ratio="4:3"
        )
        image_path = f"./outputs/transparent_bg/{icon_id}.png"
        response.images[0].save(image_path)

        return image_path
    except Exception as e:
        message = f"Something went wrong with generating icons, message: {e}"
        logging.error(message, exc_info=True)


def make_white_background_transparent(image_path: str, tolerance: int = 20) -> None:
    """
    Make a white background a transparent image.
    :param image_path: Generated image path.
    :param tolerance: Tolerance for a white background.
    """
    image = Image.open(image_path)
    image = image.convert("RGBA")
    bg_color = image.getpixel((0, 0))

    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel_color = image.getpixel((x, y))
            if all(abs(pixel_color[i] - bg_color[i]) <= tolerance for i in range(3)):
                image.putpixel((x, y), (0, 0, 0, 0))

    image.save("transparent_image.png", format="PNG")
