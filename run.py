from vertex_ai import image_gen

prompt_keywords = ["cheese burger", "fastfood"]

generated_icon = image_gen.generate_icon(keywords_list=prompt_keywords)
image_gen.make_white_background_transparent(image_path=generated_icon)

print(generated_icon)
