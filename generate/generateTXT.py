from processing.compression import MSE, PSNR, SSIM
from system import utils as u

import numpy as np
import time

def saveInLogs(data):
    with open(u.dt_string+'/report/report.txt', 'a') as f:
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f.write(u.prefix+" "+str(t)+" » "+data+"\n")


def generateTXT(image1,image2):
    saveInLogs(f"SIZE : {image1,image2}")
    saveInLogs(f"ENTROPY IM1 : {image1.entropy()} ENTROPY IM2 : {image2.entropy()}")
    saveInLogs(f"EXIF IM1 : {image1.getexif()} EXIF IM2 : {image2.getexif()}")
    saveInLogs(f"\n\n")
    saveInLogs(f"PSNR : {PSNR(np.array(image1),np.array(image2))}")
    saveInLogs(f"SSIM : {SSIM(np.array(image1),np.array(image2))}")
    saveInLogs(f"MSE  : {MSE(np.array(image1),np.array(image2))}")
    saveInLogs(f"\n\n")

