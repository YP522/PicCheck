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
from PIL import Image
from system import utils as u
import numpy as np
import cv2

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
        perc1 = (p1+p2+p3)/3
        perc2 = (_p1+_p2+_p3)/3

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
    # Convert the images to NumPy arrays
    np_image1 = np.array(image1)
    np_image2 = np.array(image2)
    
    # Calculate the differences for all pixels using broadcasting
    differences = np.abs(np_image1 - np_image2)
    
    # Calculate the average differences across color channels
    average_differences = np.mean(differences, axis=2)
    
    # Count the number of pixels with zero differences
    matched_pixels = np.count_nonzero(average_differences == 0)
    
    return matched_pixels


def save_matched_pixels(image1, image2, mode):
    """
    Given two images, this function will create a new image where the pixels of the first image are
    retained if and only if the corresponding pixels in the second image are the same.
    
    :param image1: The first image to compare
    :param image2: The image to compare against
    :param mode: 
    :return: The image with the matched pixels in alpha.
    """
    def pixel_match(pixel1, pixel2):
        return get_diff(pixel1, pixel2, mode) == 0

    width, height = image1.size
    img = Image.new('RGBA', (width, height), (255, 0, 0, 0))

    img.putdata([pixel1 if pixel_match(pixel1, pixel2) else (0, 0, 0, 0) for pixel1, pixel2 in zip(image1.getdata(), image2.getdata())])

    return img


def read_color_palette(name='Viridis'):
    """
    It reads a CSS file and returns a list of colors
    
    :param name: the name of the color palette to use, defaults to Viridis (optional)
    :return: A list of 5 colors.
    """
    filename = u.dt_string+f'/report/assets/themes/{name}.css'
    with open(filename, 'r') as f:
        contents = f.read()
    lines = contents.split('\n')
    if len(lines) == 0:
        raise ValueError(f'Empty file: {filename}')
    elif len(lines) == 1:
        raise ValueError(f'Invalid format: {filename}')
    else:
        levelA = lines[1].split(':')[1].strip()
        levelB = lines[2].split(':')[1].strip()
        levelC = lines[3].split(':')[1].strip()
        levelD = lines[4].split(':')[1].strip()
        levelE = lines[5].split(':')[1].strip()
        return [levelA, levelB, levelC, levelD, levelE]


def heatmap_comparison(original_image, test_image, colormap='Viridis'):
    """
    It takes two grayscale images, calculates the difference between them, and then creates a heat map
    of the difference.
    
    :param original_image: The original image
    :param test_image: The image to compare to the original image
    :param colormap: The name of the colour palette to use, defaults to Viridis (optional)
    :return: The heatmap_comparison function returns an image that is a combination of the original
    image and the heatmap.
    """
    # Load the CSS file for the colour scheme
    levels = read_color_palette(colormap)
    
    # Display information on colour levels
    print(f"Color palette'{colormap}':")
    for i, level in enumerate(levels):
        print(f"  {level}: {i*100/(len(levels)-1):.1f}% of differences")
    print()

    # Normalize grayscale images to a range of values between 0 and 1
    original_normalized = np.array(original_image) / 255.0
    test_normalized = np.array(test_image) / 255.0

    # Calculate the normalized difference between the two grayscale images
    diff_normalized = np.abs(original_normalized - test_normalized)

    # Create the colour palette
    colors = [np.array(tuple(int(c[i:i+2], 16) for i in (1, 3, 5))) for c in levels]
    color_indices = np.digitize(diff_normalized, np.linspace(0, 1, len(levels) + 1)[1:-1])
    color_palette = np.array(colors)[color_indices]

    # Calculate the percentage use of each colour level
    color_counts = np.bincount(color_indices.flatten(), minlength=len(levels))
    color_percentages = color_counts / np.sum(color_counts)

    # Display information on the colours used
    print("Colors used :")
    for i, level in enumerate(levels):
        print(f"  {level}: {color_counts[i]:d} pixels ({color_percentages[i]*100:.1f}%)")
    print()

    # Convert the heat map to an image
    heatmap_image = Image.fromarray(np.uint8(color_palette))

    # Overlay the original image and the heat map with 50% transparency
    output_image = Image.blend(original_image.convert('RGB'), heatmap_image, 0.5)

    return output_image