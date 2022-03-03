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
#####################################################################################################################################
# For XLSX report


# Get the DELTA-E distance value between 2 colors
def getDELTA_E_VALUE(c1, c2):
    Lab_1 = colour.XYZ_to_Lab(c1)
    Lab_2 = colour.XYZ_to_Lab(c2)
    RGB = colour.XYZ_to_sRGB(Lab_1 / 100)
    RGB2 = colour.XYZ_to_sRGB(Lab_2 / 100)
    return colour.delta_E(RGB, RGB2, method='CIE 1976')


# Get the level of color Difference between 2 colors
def getDiff(c1, c2, mode):
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


# Get RGB gap between 2 colors
def getGap(c1, c2):
    _r = c1[0];                     __r = c2[0];
    _g = c1[1];                     __g = c2[1];
    _b = c1[2];                     __b = c2[2];

    r = _r - __r;
    g = _g - __g;
    b = _b - __b;

    return r, g, b;


# For put data in sheet with style
def getDifferences(sheet, cell_x, cell_y, i1, i2, format1, format2):
    if getDiff(i1, i2, 1) == 0:
        sheet.write(cell_x, cell_y, getDiff(i1, i2, 1), format1)
    elif getDiff(i1, i2, 1) >= 0.01 and getDiff(i1, i2, 1) < 1:
        sheet.write(cell_x, cell_y, getDiff(i1, i2, 1), format2)
    else:
        sheet.write(cell_x, cell_y, getDiff(i1, i2, 1))


# Get List of ColorDifferences
def getColorDifferences(image1, image2,):

    matched_pixels = []

    for index_x in range(image1.height):
        for index_y in range(image1.width):

            i1 = image1.getpixel((index_y, index_x))
            i2 = image2.getpixel((index_y, index_x))

            if getDiff(i1, i2, 1) == 0:
                matched_pixels.append(0)
    return len(matched_pixels)
