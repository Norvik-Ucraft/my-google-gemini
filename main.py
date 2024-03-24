import google.generativeai as genai

import config

genai.configure(api_key=config.GEMINI_API_KEY)
product_description_generator = genai.GenerativeModel("gemini-pro")

prompt = "What do you know about gemini model?"

# Simple generation process
simple_generation = product_description_generator.generate_content(contents=prompt)
generated_response = simple_generation.text

# Safety check
check_safety = simple_generation.prompt_feedback

# Streaming while the content is generated
streamed_generation = product_description_generator.generate_content(contents=prompt, stream=True)
for chunk in streamed_generation:
    print(chunk.text)
