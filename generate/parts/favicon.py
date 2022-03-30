# draw_rectangle.py
from PIL import Image, ImageDraw
from system import utils as u


def generateFavIcon(size, first_color, second_color):
    """
    Generate a square image with a rectangle of the specified color in the center
    
    :param size: The size of the square image
    :param first_color: The first color of the gradient
    :param second_color: The color of the second half of the icon
    """
    image = Image.new("RGB", (size, size), first_color)
    draw = ImageDraw.Draw(image)
    draw.rectangle(((size/2)-1, size, 0, 0), fill=second_color)
    image.save(u.dt_string+'/report/assets/favicon.png')
