IMAGEN_MODEL_PROMPT = "Design a minimalist icon of [keywords] in a line art style, transparent background."

PROMPT_GENERATOR_PROMPT = """
Generate one prompt for imagen model to represents pure icon or a symbol of based on the provided keywords from user
which will be used later in a logo. \
** Important rules to follow: \
1. The icon should always be with transparent background. \
2. The icon should always be without any text and without any shadows. \
Return the prompt without any extra text or description.
"""