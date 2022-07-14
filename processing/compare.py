# _________________________________________________________________________________________________________________________________ #
#                                                                                                                                   #
#        ________    ___      ________                  ________      ___  ___      _______       ________      ___  ___            #
#       |\   __  \  |\  \    |\   ____\                |\   ____\    |\  \|\  \    |\  ___ \     |\   ____\    |\  \|\  \           #
#       \ \  \|\  \ \ \  \   \ \  \___|                \ \  \___|    \ \  \\\  \   \ \   __/|    \ \  \___|    \ \  \/  /|_         #
#        \ \   ____\ \ \  \   \ \  \        T U r E s   \ \  \        \ \   __  \   \ \  \_|/__   \ \  \        \ \   ___  \        #
#         \ \  \___|  \ \  \   \ \  \____    t u R e S   \ \  \____    \ \  \ \  \   \ \  \_|\ \   \ \  \____    \ \  \\ \  \       #
#          \ \__\      \ \__\   \ \_______\               \ \_______\   \ \__\ \__\   \ \_______\   \ \_______\   \ \__\\ \__\      #
#           \|__|       \|__|    \|_______|                \|_______|    \|__|\|__|    \|_______|    \|_______|    \|__| \|__|      #
#                                                                                                                                   #
# _________________________________________________________________________________________________________________________________ #
#                                                             Machinery                                                             #
#####################################################################################################################################
import colour
from PIL import Image, ImageDraw
#####################################################################################################################################
# For XLSX report


def get_delta_e_value(c1, c2):
    """
    This function takes two colours and returns the delta E value between them
    
    :param c1: The first colour
    :param c2: The color to compare to c1
    :return: The delta_E value.
    """
    lab_1 = colour.XYZ_to_Lab(c1)
    lab_2 = colour.XYZ_to_Lab(c2)
    RGB = colour.XYZ_to_sRGB(lab_1 / 100)
    RGB2 = colour.XYZ_to_sRGB(lab_2 / 100)
    return colour.delta_E(RGB, RGB2, method='CIE 1976')


def get_diff(c1, c2, mode):
    """
    The function takes in two RGB values and returns the difference between the two values.
    
    :param c1: The first color to compare
    :param c2: The color to compare to
    :param mode: 0 = RGB, 1 = average
    :return: The difference between the two colors.
    """
    _r = c1[0];                     __r = c2[0];
    _g = c1[1];                     __g = c2[1];
    _b = c1[2];                     __b = c2[2];

    p1 = (_r / 255) * 100;          _p1 = (__r / 255) * 100;
    p2 = (_g / 255) * 100;          _p2 = (__g / 255) * 100;
    p3 = (_b / 255) * 100;          _p3 = (__b / 255) * 100;

    if mode == 0:
        perc1 = round((p1+p2+p3)/3)
        perc2 = round((_p1+_p2+_p3)/3)
    elif mode == 1:
        perc1 = p1+p2+p3/3
        perc2 = _p1+_p2+_p3/3

    return abs(perc1 - perc2);


def get_gap(c1, c2):
    """
    Given two colors, return the gap between them
    
    :param c1: The first color
    :param c2: The color to compare against
    :return: The difference between the RGB values of the two colors.
    """
    _r = c1[0];                     __r = c2[0];
    _g = c1[1];                     __g = c2[1];
    _b = c1[2];                     __b = c2[2];

    r = _r - __r;
    g = _g - __g;
    b = _b - __b;

    return r, g, b;


def get_differences(sheet, cell_x, cell_y, i1, i2, format1, format2):
    """
    Write the difference between two numbers to a cell in a spreadsheet
    
    :param sheet: the sheet you want to write to
    :param cell_x: the x coordinate of the cell where the difference will be written
    :param cell_y: The column number of the cell you want to write to
    :param i1: The first input dataframe
    :param i2: the second dataframe to compare
    :param format1: format for values that are less than 1% different
    :param format2: format for values that are greater than 0.01 but less than 1
    """
    if get_diff(i1, i2, 1) == 0:
        sheet.write(cell_x, cell_y, get_diff(i1, i2, 1), format1)
    elif get_diff(i1, i2, 1) >= 0.01 and get_diff(i1, i2, 1) < 1:
        sheet.write(cell_x, cell_y, get_diff(i1, i2, 1), format2)
    else:
        sheet.write(cell_x, cell_y, get_diff(i1, i2, 1))


def get_color_differences(image1, image2,):
    """
    Given two images, return the number of pixels that are the same in both images
    
    :param image1: The first image to compare
    :param image2: The image to compare to
    :return: The number of pixels that are the same in both images.
    """

    matched_pixels = []

    for index_x in range(image1.height):
        for index_y in range(image1.width):

            i1 = image1.getpixel((index_y, index_x))
            i2 = image2.getpixel((index_y, index_x))

            if get_diff(i1, i2, 1) == 0:
                matched_pixels.append(0)
    return len(matched_pixels)


def save_matched_pixels(image1, image2, mode):
    """
    Given two images, this function will create a new image where the pixels of the first image are
    retained if and only if the corresponding pixels in the second image are the same
    
    :param image1: The first image to compare
    :param image2: The image to compare against
    :param mode: 
    :return: The image with the matched pixels in alpha.
    """
    width, height = image1.size
    img = Image.new('RGBA', (width,height), (255,0,0,0))

    for index_x in range(height):
        for index_y in range(width):

            i1 = image1.getpixel((index_y, index_x))
            i2 = image2.getpixel((index_y, index_x))

            if get_diff(i1, i2, mode) == 0:
                img.putpixel((index_y, index_x), i1)            
    return img
