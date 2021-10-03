###############################################################################
#                    PicCheck | Get Color Data from picture                   #
###############################################################################
#                                                                             #
#   Table Of Contents                                                         #
#                                                                             #
#       1. Read Picture                                                       #
#       2. Get Hexa / RGB                                                     #
#       3. Compare 2 pictures (colorimetric distance)                         #
#                                                                             #
###############################################################################
#                                 IMPORTS                                     #
###############################################################################

import sys, os, numpy, colour, xlsxwriter
from PIL import Image
from datetime import datetime
from math import sqrt
from collections import Counter

###############################################################################
#                                 DECLARE                                     #
###############################################################################

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")

workbook = xlsxwriter.Workbook(dt_string+"-PicCheck.xlsx")

worksheet = workbook.add_worksheet("% ColorDiff")
worksheet2 = workbook.add_worksheet("Delta-E")
worksheet3 = workbook.add_worksheet("I1 ColorHexa")
worksheet4 = workbook.add_worksheet("I2 ColorHexa")
worksheet5 = workbook.add_worksheet("I1 ColorRGB")
worksheet6 = workbook.add_worksheet("I2 ColorRGB")
worksheet7 = workbook.add_worksheet("I1 ColorOccurences")
worksheet8 = workbook.add_worksheet("I2 ColorOccurences")

###############################################################################
#                                FUNCTIONS                                    #
###############################################################################

def getIMG(file):
    image = Image.open(file)
    return image

#-----------------------------------------------------------------------------#

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

#-----------------------------------------------------------------------------#

def getDELTA_E_VALUE(c1,c2):
     Lab_1 = colour.XYZ_to_Lab(c1)
     Lab_2 = colour.XYZ_to_Lab(c2)
     RGB = colour.XYZ_to_sRGB(Lab_1 / 100)
     RGB2 = colour.XYZ_to_sRGB(Lab_2 / 100)
     delta_E = colour.delta_E(RGB, RGB2, method='CIE 1976')
     return delta_E

#-----------------------------------------------------------------------------#

def getDiff(c1,c2):
    _r = c1[0];                     __r = c2[0];
    _g = c1[1];                     __g = c2[1];
    _b = c1[2];                     __b = c2[2];

    p1 = (_r / 255) * 100;          _p1 = (__r / 255) * 100;
    p2 = (_g / 255) * 100;          _p2 = (__g / 255) * 100;
    p3 = (_b / 255) * 100;          _p3 = (__b / 255) * 100;

    perc1 = round((p1+p2+p3)/3)
    perc2 = round((_p1+_p2+_p3)/3)

    result=abs(perc1 - perc2);
    return result

#-----------------------------------------------------------------------------#

def getPixelOcc(image):
    with image as img:
        width, height = img.size
        rgb_img = img.convert('RGB')
        r, g, b = rgb_img.getpixel((1, 1))

        pixels = list(rgb_img.getdata())
        myList = Counter(pixels).most_common()
        return myList;

#-----------------------------------------------------------------------------#

def generate(image,image2):

    with image as img:

        width, height = img.size
        rgb_img = img.convert('RGB')
        pixels = list(rgb_img.getdata())

        width, height = image2.size
        rgb_img2 = image2.convert('RGB')
        pixels2 = list(rgb_img2.getdata())

        for i in range(len(getPixelOcc(image))):
                print("PART-1 : ",round(i/len(getPixelOcc(image))*100),"% [",i,"/",len(getPixelOcc(image)),"]")
                worksheet7.write(i,0,(str(getPixelOcc(image)[i][0])))
                worksheet7.write(i,1,getPixelOcc(image)[i][1])
        for i in range(len(getPixelOcc(image2))):
                print("PART-2 : ",round(i/len(getPixelOcc(image2))*100),"% [",i,"/",len(getPixelOcc(image2)),"]")
                worksheet8.write(i,0,(str(getPixelOcc(image2)[i][0])))
                worksheet8.write(i,1,getPixelOcc(image2)[i][1])

        for a in range(height):
            print("PART-3 : ",round(a/height)*100,"% [",a,"/",height,"]")
            for b in range(width):
                i1=rgb_img.getpixel((b,a))
                i2=rgb_img2.getpixel((b,a))
                worksheet.write(a,b, getDiff(i1,i2))
                worksheet2.write(a,b, getDELTA_E_VALUE(i1,i2))
                worksheet3.write(a,b, rgb_to_hex(i1))
                worksheet4.write(a,b, rgb_to_hex(i2))
                worksheet5.write(a,b, str(i1))
                worksheet6.write(a,b, str(i2))

    print(' - - - - - END - - - - - ');
    print('  ');
    print("File generated : =", dt_string)

#-----------------------------------------------------------------------------#

def checkFile(path):
    if(os.path.exists(path)):
        if os.path.isfile(path):
            return True;
        elif os.path.isdir(path):
            return False;
    else:
        print('The location doesn\'t exist')

###############################################################################
#                                   MAIN                                      #
###############################################################################

if checkFile(sys.argv[1])==True and checkFile(sys.argv[2])==True:
    image = getIMG(sys.argv[1])
    image2 = getIMG(sys.argv[2])

    print("START :", now)
    generate(image,image2)
    filename = dt_string+"-PicCheck.txt"
    fin = datetime.now()
    print("END :",fin.strftime("%d-%m-%Y-%H-%M-%S"))

workbook.close()
