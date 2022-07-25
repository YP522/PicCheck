# _________________________________________________________________________________________________________________________________ #
#                                                                                                                                   #
#        ________    ___      ________                  ________      ___  ___      _______       ________      ___  ___            #
#       |\   __  \  |\  \    |\   ____\                |\   ____\    |\  \|\  \    |\  ___ \     |\   ____\    |\  \|\  \           #
#       \ \  \|\  \ \ \  \   \ \  \___|                \ \  \___|    \ \  \\\  \   \ \   __/|    \ \  \___|    \ \  \/  /|_         #
#        \ \   ____\ \ \  \   \ \  \        T u r E S   \ \  \        \ \   __  \   \ \  \_|/__   \ \  \        \ \   ___  \        #
#         \ \  \___|  \ \  \   \ \  \____    T U R e s   \ \  \____    \ \  \ \  \   \ \  \_|\ \   \ \  \____    \ \  \\ \  \       #
#          \ \__\      \ \__\   \ \_______\               \ \_______\   \ \__\ \__\   \ \_______\   \ \_______\   \ \__\\ \__\      #
#           \|__|       \|__|    \|_______|                \|_______|    \|__|\|__|    \|_______|    \|_______|    \|__| \|__|      #
#                                                                                                                                   #
# _________________________________________________________________________________________________________________________________ #
#                                                             Machinery                                                             #
#####################################################################################################################################
from itertools import product
from math import log10, sqrt
from pathlib import Path
from PIL import Image

import cv2
import numpy as np
import skimage.metrics as skm
from tqdm import tqdm
import system.utils as u
from generate.generateXLSX import NOR_DCT_1, NOR_DCT_2, ndct_1_1, ndct_1_2, ndct_1_3, ndct_1_4, ndct_2_1, ndct_2_2, ndct_2_3, ndct_2_4

#####################################################################################################################################

d = 8 ;

wrap_format_1 = NOR_DCT_1.add_format({'text_wrap': True,'border': True})
wrap_format_2 = NOR_DCT_2.add_format({'text_wrap': True,'border': True})


def get_compression_level(img, img_file):
    """
    Given an image and its file name, return the compression level
    
    :param img: the image object
    :param img_file: The name of the image file
    :return: The quality of the image.
    """

    path = f"{u.dt_string}/data/{img_file}.png"
    quality = (101-((img.width*img.height)*3)/(Path(path).stat().st_size))
    return quality;


def get_psnr(original, compressed):
    """
    Compute the PSNR of the compressed image and the original image
    
    :param original: The original image
    :param compressed: The compressed image
    :return: the PSNR value for the two images.
    """
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr


def get_ssim(original, compressed):
    """
    Compute the SSIM of the compressed image and the original image
    
    :param original: The original image
    :param compressed: The compressed image
    :return: the SSIM value for the two images.
    """
    return skm.structural_similarity(original, compressed, channel_axis=2)


def get_mse(original, compressed):
    """
    Compute the MSE of the compressed image and the original image
    
    :param original: The original image
    :param compressed: The compressed image
    :return: the MSE value for the two images.
    """
    mse = np.mean((original - compressed) ** 2)
    return mse
    

def format_to_grid_with_commas(matrix):
    """
    Given a matrix, format it to a string with commas between the numbers
    
    :param matrix: the matrix to be formatted
    :return: a string of the matrix with commas and spaces.
    """
    return np.array2string(np.int32(matrix), separator=', ')


def dec_dct(matrix):
    """
    Convert a matrix of integers to floats, perform the DCT on the matrix, then convert the result back
    to integers
    
    :param matrix: The matrix to be converted
    :return: a matrix of the same size as the input matrix.
    """
    block = eval(matrix)
    blockf = np.float32(block)
    dst = cv2.dct(blockf)
    return np.int32(dst)


def dec_inverse_dct(matrix):
    """
    # The function dec_inverse_dct() is the inverse of the function dec_dct(). It takes a string
    representation of a matrix as input and returns a matrix representation of the inverse DCT
    
    :param matrix: The matrix to be processed
    :return: the inverse DCT of the input matrix.
    """
    block = eval(matrix)
    blockf = np.float32(block)
    dst = cv2.dct(blockf)
    block = cv2.idct(dst)
    return np.int32(block)


def up_sampling(array):
    """
    Given a 2D array, return a new 2D array with the array values repeated twice along the first axis
    (axis=0) and twice along the second axis (axis=1)
    
    :param array: the array to be repeated
    :return: The upSampled image.
    """
    return np.array(array.repeat(2, axis=0).repeat(2, axis=1))


def tile(img, d, img_name):
    """
    This function is used to split the image into tiles and save them in a folder. 

    :param img: the image to be compressed
    :param d: The size of the tiles
    :param img_name: the name of the image to be processed
    """
    if img.mode == "RGBA":
        img = img.convert("RGB")
    w, h = img.size
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in tqdm(grid):
        box = (j, i, j+d, i+d)
        out = f'{u.dt_string}/data/dct/{img_name}/tiles/tile_{i}_{j}.jpg'
         
        img.crop(box).save(out)


def write_bloc_in_cell(img,img2):
    """
    This procedure is used to set DCT data in cells and save IDCT Tiles in folder. 

    :param img: 
    :param img2: 
    """    
    w, h = img.size
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in grid:
        x = int(i/d)
        y = int(j/d)
        box = (j, i, j+d, i+d)
 

        out2 = f'{u.dt_string}/data/idct/img1/tiles/tile_{i}_{j}.jpg'
        out3 = f'{u.dt_string}/data/idct/img2/tiles/tile_{i}_{j}.jpg'
        

        # 1 - Decoding
        img8=img.crop(box).convert("L")
        arr=np.array(img8)
        block=arr.tolist()

        ndct_1_1.write(x, y, format_to_grid_with_commas(block), wrap_format_1)
        ndct_1_1.set_row(x, 155)
        ndct_1_1.set_column(x, y, 25)

        # 2 - DCT
        block_dct = dec_dct(str(block))
        ndct_1_2.write(x, y, format_to_grid_with_commas(block_dct), wrap_format_1)
        ndct_1_2.set_row(x, 155)
        ndct_1_2.set_column(x, y, 25)        

        # 3 - DeQuantization
        quantizedimg=img.quantize(256)
        qarr=np.array(quantizedimg)
        qblock=qarr.tolist()

        ndct_1_3.write(x, y, str(qblock), wrap_format_1)
        ndct_1_3.set_row(x, 155)
        ndct_1_3.set_column(x,y, 25)


        # 4 - Inverse DCT
        block_idct=(dec_inverse_dct(format_to_grid_with_commas(block_dct)))

        ndct_1_4.write(x, y, format_to_grid_with_commas(block_idct), wrap_format_1)
        ndct_1_4.set_row(x, 155)
        ndct_1_4.set_column(x, y, 25)
        
        idct_img = Image.fromarray(np.uint8(block_idct))
        idct_img.save(out2)        






        # 1 - Decoding
        img__v2=img2.crop(box).convert("L")
        arr2=np.array(img__v2)
        block_v2=arr2.tolist()

        ndct_2_1.write(x,y,format_to_grid_with_commas(block_v2),wrap_format_2)
        ndct_2_1.set_row(x, 155)
        ndct_2_1.set_column(x,y, 25)

        # 2 - DCT
        block_dct2 = dec_dct(str(block_v2))
        # print(format_to_grid_with_commas(dec_dct(str(block_v2))))
              
        ndct_2_2.write(x, y, format_to_grid_with_commas(block_dct2), wrap_format_1) 
        ndct_2_2.set_row(x, 155)
        ndct_2_2.set_column(x, y, 25)

        # 3 - DeQuantization
        quantizedimg=img2.quantize(256)
        qarr=np.array(quantizedimg)
        qblock_v2=qarr.tolist()

        ndct_2_3.write(x,y,str(qblock_v2),wrap_format_2)
        ndct_2_3.set_row(x, 155)
        ndct_2_3.set_column(x,y, 25)        

        # 4 - Inverse DCT
        block_idct_v2=(dec_inverse_dct(format_to_grid_with_commas(block_dct2)))
        
        ndct_2_4.write(x, y, format_to_grid_with_commas(block_idct_v2), wrap_format_2)
        ndct_2_4.set_row(x, 155)
        ndct_2_4.set_column(x, y, 25)
        
        idct_img = Image.fromarray(np.uint8(block_idct))
        # 
        idct_img.save(out3)

