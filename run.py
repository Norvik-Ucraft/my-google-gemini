from vertex_ai import logo_generator

for _ in range(6):
    generated_image_bytes = logo_generator.generate_logo(["car", "mechanic", "engine"])
    detected_text = logo_generator.extract_image_info(generated_image_bytes)
    logo_generator.make_background_transparent(image_bytes=generated_image_bytes, background_color_threshold=50)
