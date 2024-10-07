IMAGEN_3_MODEL = "imagen-3.0-generate-001"

IMAGEN_MODEL_PROMPT = "Design a very minimalistic icon of [keywords] in a black fill in style, no extra lines around the icon, no gradient, transparent background."

TEMP_PROMPT = "A clean, single flat icon, employing a black fill-in style, highlights [keywords], absent of gradients or shadows, against a flawless, bright white background."

PROMPT_GENERATOR_PROMPT = """
Generate one prompt for imagen model to represents pure icon or a symbol of based on the provided keywords from user
which will be used later in a logo. \
** Important rules to follow: \
1. The icon should always be with transparent background. \
2. The icon should always be without any text and without any shadows. \
Return the prompt without any extra text or description.
"""

first_prompt = """
Generate a creative minimalistic logo for my website that captures: [keywords]. With fill-in styling on a white background. The icon should be simple yet artistic, with unique design elements that make it stand out, using only black color without any text or additional content.
"""
