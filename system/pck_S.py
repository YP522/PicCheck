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
from PIL import Image
import numpy as np
from system.pck_M import *
from generate.generateFolders import createFolders
from system import utils as u
import os
#####################################################################################################################################


def checkFile(path):
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


def getIMG(file):
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
    return np.array(getIMG(img))


def run(img1, img2):
    """
    :param img1: The first image to compare
    :param img2: The image to compare with
    """
    g_i1 = getIMG(img1).convert('RGBA');
    g_i2 = getIMG(img2).convert('RGBA');

    if((checkFile(img1) and checkFile(img2)) != True):
        u.log(f"{u.bad} {u.errors[0]}")
    else:
        u.log(f"{u.good} Files exists !")

        if(g_i1.size != g_i2.size):
            u.log(f"{u.bad} {u.errors[1]}")
        else:
            u.log(f"{u.good} File {g_i1.size} and file {g_i2.size} is equal !")
            u.log(f"\n{u.prefix}")

            createFolders()            

            launchCollect(g_i1, g_i2)
            u.log("  [1/3] End process of color collection...")

            launchCompare(g_i1, g_i2)
            u.log("  [2/3] End process of color compare...")

            launchCompress(g_i1, g_i2)
            u.log("  [3/3] End process of color compress...")

            u.log(f"\n{u.prefix} \n{u.prefix} {u.good} End of PicCheck Consultation. Find results and Enjoy !")
            u.log(u.slogan)
            u.log(f"\n{u.prefix} Please see report at : {u.dt_string}/report/report.html")
