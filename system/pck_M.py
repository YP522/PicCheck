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
from generate.generateXLSX import *
from generate.generateHTML import *
from generate.generateTXT import *

from processing.collect import *
from processing.compare import *
from processing.compression import tile

from system import utils as u

#####################################################################################################################################

def launchCollect(image1, image2):
    """
    This function is used to collect the color data from the images and save it in a spreadsheet
    
    :param image1: the first image to compare
    :param image2: the second image to compare with the first one
    """
    u.log("  [1/3] Start process of color collection...")   
    width, height = image1.size

    image1.save(u.dt_string+"/data/img1.png")
    image2.save(u.dt_string+"/data/img2.png")

    # Declare grayscale image
    la_image1 = image1.convert('LA');
    la_image2 = image2.convert('LA');

    # Save grayscale image
    la_image1.save(u.dt_string+"/data/gra_img1.png")
    la_image2.save(u.dt_string+"/data/gra_img2.png")

    for index_x in range(height):
        for index_y in range(width):

        # HEXA extraction for index
            iPxl_hexa1_n = getPixelColor(image1, 'hexa', index_x, index_y)
            iPxl_hexa2_n = getPixelColor(image2, 'hexa', index_x, index_y)

            iPxl_hexa1_g = getPixelColor(la_image1, 'hexa', index_x, index_y)
            iPxl_hexa2_g = getPixelColor(la_image2, 'hexa', index_x, index_y)

        # RGB extraction for index
            iPxl_rgb1_n = getPixelColor(image1, 'rgb', index_x, index_y)
            iPxl_rgb2_n = getPixelColor(image2, 'rgb', index_x, index_y)

            iPxl_rgb1_g = getPixelColor(la_image1, 'rgb', index_x, index_y)
            iPxl_rgb2_g = getPixelColor(la_image2, 'rgb', index_x, index_y)

        # RGBA extraction for index
            iPxl_rgba1_n = getPixelColor(image1, 'rgba', index_x, index_y)
            iPxl_rgba2_n = getPixelColor(image2, 'rgba', index_x, index_y)

            iPxl_rgba1_g = getPixelColor(la_image1, 'rgba', index_x, index_y)
            iPxl_rgba2_g = getPixelColor(la_image2, 'rgba', index_x, index_y)

        # HEXA insertion for index
            ncol_1.write(index_x, index_y, str(iPxl_hexa1_n))
            ncol_2.write(index_x, index_y, str(iPxl_hexa2_n))

            gcol_1.write(index_x, index_y, iPxl_hexa1_g)
            gcol_2.write(index_x, index_y, iPxl_hexa2_g)

        # RGB insertion for index
            ncol_3.write(index_x, index_y, str(iPxl_rgb1_n))
            ncol_4.write(index_x, index_y, str(iPxl_rgb2_n))

            gcol_3.write(index_x, index_y, str(iPxl_rgb1_g))
            gcol_4.write(index_x, index_y, str(iPxl_rgb2_g))

        # RGBA insertion for index
            ncol_5.write(index_x, index_y, str(iPxl_rgba1_n))
            ncol_6.write(index_x, index_y, str(iPxl_rgba2_n))

            gcol_5.write(index_x, index_y, str(iPxl_rgba1_g))
            gcol_6.write(index_x, index_y, str(iPxl_rgba2_g))

    for index_1 in range(len(getPixelOcc(image1))):
        setOccurences(image1, index_1, ncol_7)
    for index_1 in range(len(getPixelOcc(la_image1))):
        setOccurences(la_image1, index_1, gcol_7)

    for index_2 in range(len(getPixelOcc(image2))):
        setOccurences(image2, index_2, ncol_8)
    for index_2 in range(len(getPixelOcc(la_image2))):
        setOccurences(la_image2, index_2, gcol_8)

    NOR_COL.close()
    GRA_COL.close()

# #####################################################################################################################################


def launchCompare(image1, image2):
    u.log("  [2/3] Start process of color compare...")  
    width, height = image1.size

    image1 = image1.convert('RGB');
    image2 = image2.convert('RGB');
    # Declare grayscale

    limage1 = image1.convert('RGB');
    limage2 = image2.convert('RGB');

    mat_nor_0 = saveMatchedPixels(image1,image2,0)
    mat_nor_1 = saveMatchedPixels(image1,image2,1) 

    mat_gra_0 = saveMatchedPixels(image1,image2,0)
    mat_gra_1 = saveMatchedPixels(image1,image2,1)  

    mat_nor_0.save(u.dt_string+"/data/matched_nor_0.png")
    mat_nor_1.save(u.dt_string+"/data/matched_nor_1.png")

    mat_gra_0.save(u.dt_string+"/data/matched_gra_0.png")
    mat_gra_1.save(u.dt_string+"/data/matched_gra_1.png")

    for index_x in range(height):
        for index_y in range(width):

            # duplicate all calls with grayscale images
            i1 = image1.getpixel((index_y, index_x))
            i2 = image2.getpixel((index_y, index_x))

            ncom_1.write(index_x, index_y, getDiff(i1, i2, 0))

            getDifferences(ncom_2, index_x, index_y, i1, i2, format_img1, format_img1_near)           

            ncom_3.write(index_x, index_y, str(getGap(i1, i2)))
            ncom_5.write(index_x, index_y, getDELTA_E_VALUE(i1, i2))

            # duplicate all calls with grayscale images
            la_i1 = limage1.getpixel((index_y, index_x))
            la_i2 = limage2.getpixel((index_y, index_x))

            gcom_1.write(index_x, index_y, getDiff(la_i1, la_i2, 0))

            getDifferences(gcom_2, index_x, index_y, la_i1, la_i2, format_img2, format_img2_near)

            gcom_3.write(index_x, index_y, str(getGap(la_i1, la_i2)))
            gcom_5.write(index_x, index_y, getDELTA_E_VALUE(la_i1, la_i2))

    NOR_COM.close()
    GRA_COM.close()


#     # XLSX report
# #####################################################################################################################################


def launchCompress(image1, image2):
    u.log("  [3/3] Start process of color compress...")
    tile(image1,8,'img1')
    tile(image2,8,'img2')

