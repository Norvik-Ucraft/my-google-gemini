from vertex_ai import image_gen

prompt_keywords = ["tech", "betting", "money"]

generated_icon = image_gen.generate_icon(keywords_list=prompt_keywords, name="Alexian")
image_gen.make_white_background_transparent(image_path=generated_icon)
print(generated_icon)

tested = """
["angus", "steak", "restaurant", "cozy"],
["payment gateway", "online transaction"],
["chinese food", "noodle", "soup"],
["wine", "glass", "bottle", "waiter"],
["italian", "pizza"],
["football", "mascot"],
["football", "mascot", "eagle"],
["Spanish", "bachata", "concert hall"]
"""
