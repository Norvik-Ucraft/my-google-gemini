import io
import math
import uuid
import logging
from collections import Counter

import numpy as np
import vertexai
from PIL import Image
from rembg import remove
from google.cloud import vision
from vertexai.preview.vision_models import ImageGenerationModel

import config

IMAGEN_3_MODEL = "imagen-3.0-generate-001"

vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
generation_model = ImageGenerationModel.from_pretrained(IMAGEN_3_MODEL)


def generate_logo(keywords_list: list):
    """
    Generate a logo based on the provided keywords.
    :param keywords_list: Provided list of business keywords.
    :return: PNG path.
    """
    logging.info("Starting to generate logo...")

    logo_generator = generation_model.generate_images(
        prompt=f"Generate a creative logo based on the keywords [{keywords_list}], using only two colors: one for the logo and one for the background. The logo should be clean and minimalistic, reflecting the theme with smooth, flowing shapes or geometric elements. Ensure there are no letters, numbers, or shadows. The background color must contrast with the logo color to create a clear distinction between the two, enhancing the overall visual appeal.",
        aspect_ratio="1:1",
        person_generation="dont_allow",
        safety_filter_level="block_some",
        guidance_scale=999999999999999999999999.0,
        negative_prompt="CHARACTERS, SHADOWS, WORDS, NUMBERS",
        add_watermark=False,
    )

    image_id = str(uuid.uuid4())
    image_path = f"./generated_logos/logo-{image_id[:4]}.png"
    logo_generator.images[0]._pil_image.show()
    logo_generator.images[0].save(image_path)
    logging.info(image_path)

    return logo_generator.images[0]._image_bytes


def extract_image_info(image_bytes: bytes) -> tuple:
    """
    Extracting necessary information from the image.
    :param image_bytes: bytes format of an image.
    :return: tuple that contains all the necessary information.
    """
    try:
        client = vision.ImageAnnotatorClient()
        image = vision.Image(content=image_bytes)
        text_detection = client.text_detection(image=image).full_text_annotation.text

        return text_detection
    except Exception as e:
        message = f"Something went wrong with extracting information from the image, message: {e}"
        logging.error(message, exc_info=True)


def make_background_transparent(image_bytes: bytes, background_color_threshold: int = 50):
    def __color_distance(c1, c2):
        return math.sqrt(sum((comp1 - comp2) ** 2 for comp1, comp2 in zip(c1, c2)))

    img = Image.open(io.BytesIO(image_bytes)).convert("RGBA")
    pixels = np.array(img)[:, :, :3]
    pixels = pixels.reshape((-1, 3))
    counter = Counter(map(tuple, pixels))
    background_color = counter.most_common(1)[0][0]

    # remove background using rembg
    img = remove(img, alpha_matting_foreground_threshold=255, alpha_matting_background_threshold=0)

    # remove additional background pixels based on pixel color for further background cleaning
    data = img.getdata()
    new_data = []
    for item in data:
        r, g, b = item[:3]
        dist = __color_distance((r, g, b), background_color)
        if dist < background_color_threshold:
            new_data.append((r, g, b, 0))
        else:
            new_data.append(item)
    img.putdata(new_data)

    image_id = str(uuid.uuid4())
    image_path = f"./generated_logos_without_background/logo-{image_id[:4]}.png"
    img.save(image_path)
