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
#                                                               System                                                              #
#####################################################################################################################################
from generate.generateFolders import create_folders
from generate.generateTXT import generate_txt
from generate.generateHTML import generate_html
from processing.compression import write_bloc_in_cell
from generate.generateCSS import generate_default_themes, generate_report_css

from PIL import Image
from system.pck_M import launch_collect, launch_compare, launch_compress, NOR_DCT_1, NOR_DCT_2

from system import utils as u

import numpy as np
import os
#####################################################################################################################################


def check_file(path):
    """
    Check if the path is a file or a directory
    
    :param path: The path to the file or directory
    :return: A boolean value. True if the path is a file, False if the path is a directory.
    """
    if(os.path.exists(path)):
        if os.path.isfile(path):
            return True;
        elif os.path.isdir(path):
            return False;
        else:
            print('The location doesn\'t exist')


def get_img(file):
    """
    This function takes a file path as an argument and returns an image object
    
    :param file: The path to the image file
    :return: A PIL Image object.
    """
    return Image.open(file)


def scan(img):
    """
    This function takes in an image and returns a numpy array of the image
    
    :param img: The image to be scanned
    :return: The function scan returns an array of the image.
    """
    return np.array(img)


def run(img1, img2):
    """
    :param img1: The first image to compare
    :param img2: The image to compare with
    """
    g_i1 = get_img(img1).convert('RGBA');
    g_i2 = get_img(img2).convert('RGBA');

    if((check_file(img1) and check_file(img2)) != True):
        u.log(f"{u.bad} {u.errors[0]}")
    else:
        u.log(f"{u.good} Files exists !")

        if(g_i1.size != g_i2.size):
            u.log(f"{u.bad} {u.errors[1]}")
        else:
            u.log(f"{u.good} File {g_i1.size} and file {g_i2.size} is equal !")
            u.log(f"\n{u.prefix}")

            create_folders()
            generate_report_css()
            generate_default_themes()          

            launch_collect(g_i1, g_i2)
            u.log("  [1/3] End process of color collection...")

            launch_compare(g_i1, g_i2)
            u.log("  [2/3] End process of color compare...")

            launch_compress(g_i1, g_i2)
            u.log("  [3/3] End process of color compress...")

            generate_txt(g_i1,g_i2)
            generate_html(g_i1,g_i2)
            write_bloc_in_cell(g_i1,g_i2)

            NOR_DCT_1.close()
            NOR_DCT_2.close()            

            u.log(f"\n{u.prefix} \n{u.prefix} {u.good} End of PicCheck Consultation. Find results and Enjoy !")
            u.log(u.slogan)
            u.log(f"\n{u.prefix} Please see report at : {u.dt_string}/report/report.html")

