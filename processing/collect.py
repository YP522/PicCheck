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
from system import utils as u
from PIL import Image, ImageStat
from collections import Counter
import numpy as np
import difflib
#####################################################################################################################################

def getPixelOcc(image):
    with image as img:
        rgb_img = img.convert('RGB')
        pixels = list(rgb_img.getdata())
        return Counter(pixels).most_common()

def getPixelColor(image,mode,x,y):

    image_rgb = image.convert('RGB')
    image_rgba = image.convert('RGBA')

    if mode == 'rgb':
        return image_rgb.getpixel((y,x))

    if mode == 'rgba':
        r,g,b,a = image_rgba.getpixel((y,x))
        return r,g,b,a

    if mode == 'hexa':
        # return str(image.getpixel((y,x))[0:3])
        return '#%02x%02x%02x' % image_rgb.getpixel((y,x))

def setOccurences(image,index,sheet):
    sheet.write(index,0,(str(getPixelOcc(image)[index][0])))
    sheet.write(index,1,getPixelOcc(image)[index][1])

def getColorOccurences(image1,image2):
    with image1 as img1:
        t1 = list(img1.getdata())
    with image2 as img2:
        t2 = list(img2.getdata())

    sm= difflib.SequenceMatcher(None,t1,t2)
    return sm.ratio(),sm.ratio()*100

def getColorAverage(image1,image2):
    avg1 = ImageStat.Stat(image1)
    avg2 = ImageStat.Stat(image2)

    return avg1.mean, avg2.mean

def getColorDominante(image1,image2):
    with image1 as img1:
        t1 = list(img1.getdata())[0]
    with image2 as img2:
        t2 = list(img2.getdata())[0]

    sm= difflib.SequenceMatcher(None,t1,t2)
    return t1, t2, sm.ratio()*100;