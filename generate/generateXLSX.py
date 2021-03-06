import xlsxwriter
from system import utils as u

import xlsxwriter

#####################################################################################################################################
#                                                                XLSX                                                               #
#####################################################################################################################################

# N-COLLECT

NOR_COL = xlsxwriter.Workbook(u.dt_string+"/data/color/normal/n-collect-"+u.xlsName)
ncol_1 = NOR_COL.add_worksheet("I1 ColorHexa")
ncol_2 = NOR_COL.add_worksheet("I2 ColorHexa")
ncol_3 = NOR_COL.add_worksheet("I1 ColorRGB")
ncol_4 = NOR_COL.add_worksheet("I2 ColorRGB")
ncol_5 = NOR_COL.add_worksheet("I1 ColorRGBA")
ncol_6 = NOR_COL.add_worksheet("I2 ColorRGBA")
ncol_7 = NOR_COL.add_worksheet("I1 ColorOccurences")
ncol_8 = NOR_COL.add_worksheet("I2 ColorOccurences")

# N-COMPARE

NOR_COM = xlsxwriter.Workbook(u.dt_string+"/data/color/normal/n-compare-"+u.xlsName)
ncom_1 = NOR_COM.add_worksheet("% ColorDiff")
ncom_2 = NOR_COM.add_worksheet("% ColorDiff Decimal Number")
ncom_3 = NOR_COM.add_worksheet("ColorGap")
ncom_5 = NOR_COM.add_worksheet("Delta-E")

#####################################################################################################################################

# G-COLLECT

GRA_COL = xlsxwriter.Workbook(u.dt_string+"/data/color/grayscale/g-collect-"+u.xlsName)
gcol_1 = GRA_COL.add_worksheet("I1 ColorHexa")
gcol_2 = GRA_COL.add_worksheet("I2 ColorHexa")
gcol_3 = GRA_COL.add_worksheet("I1 ColorRGB")
gcol_4 = GRA_COL.add_worksheet("I2 ColorRGB")
gcol_5 = GRA_COL.add_worksheet("I1 ColorRGBA")
gcol_6 = GRA_COL.add_worksheet("I2 ColorRGBA")
gcol_7 = GRA_COL.add_worksheet("I1 ColorOccurences")
gcol_8 = GRA_COL.add_worksheet("I2 ColorOccurences")

# G-COMPARE

GRA_COM = xlsxwriter.Workbook(u.dt_string+"/data/color/grayscale/g-compare-"+u.xlsName)
gcom_1 = GRA_COM.add_worksheet("% BrightnessDiff")
gcom_2 = GRA_COM.add_worksheet("% BrightnessDiff Decimal Number")
gcom_3 = GRA_COM.add_worksheet("BrightnessGap")
gcom_5 = GRA_COM.add_worksheet("Delta-E")

#####################################################################################################################################
#                                                              STYLES                                                               #

format_img1 = NOR_COM.add_format()
format_img2 = GRA_COM.add_format()

format_img1_near = NOR_COM.add_format()
format_img2_near = GRA_COM.add_format()

format_img1.set_bg_color("#80FF00")
format_img2.set_bg_color("#80FF00")

format_img1_near.set_bg_color("#d2eeaa")
format_img2_near.set_bg_color("#d2eeaa")

#                                                                                                                                   #
#####################################################################################################################################
# normal/compression
NOR_DCT_1 = xlsxwriter.Workbook(u.dt_string+"/data/dct/img1/n-dct-matrix-"+u.xlsName)


# decompressed steps
ndct_1_1 = NOR_DCT_1.add_worksheet("DCT Input Matrix")
ndct_1_2 = NOR_DCT_1.add_worksheet("DCT Coeff. Value")
ndct_1_3 = NOR_DCT_1.add_worksheet("Dequantization Values")
ndct_1_4 = NOR_DCT_1.add_worksheet("IDCT Coeff. Values")



NOR_DCT_2 = xlsxwriter.Workbook(u.dt_string+"/data/dct/img2/n-dct-matrix-"+u.xlsName)

# decompressed steps

ndct_2_1 = NOR_DCT_2.add_worksheet("DCT Input Matrix")
ndct_2_2 = NOR_DCT_2.add_worksheet("DCT Coeff. Value")
ndct_2_3 = NOR_DCT_2.add_worksheet("Dequantization Values")
ndct_2_4 = NOR_DCT_2.add_worksheet("IDCT Coeff. Values")


wrap_format_1 = NOR_DCT_1.add_format({'text_wrap': True,'border': True})
wrap_format_2 = NOR_DCT_2.add_format({'text_wrap': True,'border': True})

