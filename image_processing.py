from PIL import Image
import random

def replace_colors(input_image_path, output_image_path, colors, num_squares):
    image = Image.open(input_image_path).convert('RGB')
    width, height = image.size
    print(num_squares,width,height)
    pixel_size = int(min(width / num_squares, height / num_squares))+1
    pixels = image.load()
    unique_colors = set()
    for y in range(image.height):
        for x in range(image.width):
            unique_colors.add(pixels[x, y])

    color_map = {color: random.choice(colors) for color in unique_colors}

    for y in range(image.height):
        for x in range(image.width):
            pixels[x, y] = color_map[pixels[x, y]]

    image = image.resize(
        (width // pixel_size, height // pixel_size),
        resample=Image.NEAREST
    )

    image = image.resize(
        (width, height),
        resample=Image.NEAREST
    )

    image.save(output_image_path)
