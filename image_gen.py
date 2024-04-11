import uuid

import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

import config

vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
generation_model = ImageGenerationModel.from_pretrained("imagegeneration@006")

prompt = (
    "logo based pure icon of coffee and golden retriever without any text representation with always white background"
)
response = generation_model.generate_images(
    prompt=prompt,
)

response.images[0].save(f"./images/{uuid.uuid4()}.png")
