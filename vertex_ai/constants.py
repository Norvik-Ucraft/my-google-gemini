IMAGEN_MODEL_PROMPT = "Design a very minimalistic icon of [keywords] in a black fill in style, no extra lines around the icon, no gradient, transparent background."

TEMP_PROMPT = "A flat icon with black fill-in about [keywords], no gradient and with transparent background."

PROMPT_GENERATOR_PROMPT = """
Generate one prompt for imagen model to represents pure icon or a symbol of based on the provided keywords from user
which will be used later in a logo. \
** Important rules to follow: \
1. The icon should always be with transparent background. \
2. The icon should always be without any text and without any shadows. \
Return the prompt without any extra text or description.
"""
