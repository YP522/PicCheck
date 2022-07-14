# _________________________________________________________________________________________________________________________________ #
#                                                                                                                                   #
#        ________    ___      ________                  ________      ___  ___      _______       ________      ___  ___            #
#       |\   __  \  |\  \    |\   ____\                |\   ____\    |\  \|\  \    |\  ___ \     |\   ____\    |\  \|\  \           #
#       \ \  \|\  \ \ \  \   \ \  \___|                \ \  \___|    \ \  \\\  \   \ \   __/|    \ \  \___|    \ \  \/  /|_         #
#        \ \   ____\ \ \  \   \ \  \        T u R e s   \ \  \        \ \   __  \   \ \  \_|/__   \ \  \        \ \   ___  \        #
#         \ \  \___|  \ \  \   \ \  \____    t u R E S   \ \  \____    \ \  \ \  \   \ \  \_|\ \   \ \  \____    \ \  \\ \  \       #
#          \ \__\      \ \__\   \ \_______\               \ \_______\   \ \__\ \__\   \ \_______\   \ \_______\   \ \__\\ \__\      #
#           \|__|       \|__|    \|_______|                \|_______|    \|__|\|__|    \|_______|    \|_______|    \|__| \|__|      #
#                                                                                                                                   #
# _________________________________________________________________________________________________________________________________ #
#                                                             Machinery                                                             #
#####################################################################################################################################
from system import utils as u
from PIL import Image, ImageStat
from collections import Counter
import numpy as np
import difflib
#####################################################################################################################################


def get_pixel_occ(image):
    """
    Given an image, return a list of tuples of the form (pixel, number of occurrences)
    
    :param image: The image to be analyzed
    :return: A list of tuples, where each tuple is a color and the number of times it appears in the
    image.
    """
    with image as img:
        rgb_img = img.convert('RGB')
        pixels = list(rgb_img.getdata())
        return Counter(pixels).most_common()


def get_pixel_color(image, mode, x, y):
    """
    Get the pixel color at a given coordinate
    
    :param image: The image to be processed
    :param mode: The mode parameter determines the format of the returned pixel
    :param x: The x-coordinate of the pixel
    :param y: The y-coordinate of the pixel
    :return: a tuple of RGB values.
    """

    image_rgb = image.convert('RGB')
    image_rgba = image.convert('RGBA')

    if mode == 'rgb':
        return image_rgb.getpixel((y, x))

    if mode == 'rgba':
        r, g, b, a = image_rgba.getpixel((y, x))
        return r, g, b, a

    if mode == 'hexa':
        return '#%02x%02x%02x' % image_rgb.getpixel((y, x))


def set_occurences(image, index, sheet):
    """
    This function takes in an image and an index and writes the occurences of that index to the excel
    sheet
    
    :param image: the image to be analyzed
    :param index: The index of the pixel in the list of pixels
    :param sheet: the sheet to write to
    """
    sheet.write(index, 0, (str(get_pixel_occ(image)[index][0])))
    sheet.write(index, 1, get_pixel_occ(image)[index][1])


def get_color_occurences(image1, image2):
    """
    Given two images, return the ratio of the number of pixels that are the same in both images
    
    :param image1: The first image to compare
    :param image2: The image to compare to
    :return: The ratio of the two images.
    """
    with image1 as img1:
        t1 = list(img1.getdata())
    with image2 as img2:
        t2 = list(img2.getdata())

    sm = difflib.SequenceMatcher(None, t1, t2)
    return sm.ratio(), sm.ratio()*100


def get_color_average(image1, image2):
    """
    This function takes in two images and returns the average color of each image
    
    :param image1: The first image to compare
    :param image2: The image to compare against image1
    :return: The average color of the two images.
    """
    avg1 = ImageStat.Stat(image1)
    avg2 = ImageStat.Stat(image2)

    return avg1.mean, avg2.mean


def get_color_dominante(image1, image2):
    """
    Given two images, the function returns the dominant color of the images
    
    :param image1: The first image to compare
    :param image2: The image to compare with
    :return: a tuple of three values. The first value is the dominant color of the first image. The
    second value is the dominant color of the second image. The third value is the similarity between
    the two dominant colors.
    """
    with image1 as img1:
        t1 = list(img1.getdata())[0]
    with image2 as img2:
        t2 = list(img2.getdata())[0]

    sm = difflib.SequenceMatcher(None, t1, t2)
    return t1, t2, sm.ratio()*100;
