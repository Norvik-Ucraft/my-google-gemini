import uuid

import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

import config

vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
generation_model = ImageGenerationModel.from_pretrained("imagegeneration@006")
model_prompt = (
    "logo based pure icon of coffee and golden retriever without any text representation with always white background."
)


def generate_icon(prompt: str) -> None:
    icon_id = uuid.uuid4()
    response = generation_model.generate_images(
        prompt=prompt,
        safety_filter_level="block_most",
    )

    response.images[0].save(f"./outputs/photos/{icon_id}.png")

    return icon_id
