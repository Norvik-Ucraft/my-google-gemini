import google.generativeai as genai

import config

genai.configure(api_key=config.GEMINI_API_KEY)

for models in genai.list_models():
    print(models)
