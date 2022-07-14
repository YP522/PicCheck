from processing.compression import MSE, PSNR, SSIM
from system import utils as u

import numpy as np
import time

def save_in_logs(data):
    with open(u.dt_string+'/report/report.txt', 'a') as f:
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f.write(u.prefix+" "+str(t)+" » "+data+"\n")


def generate_txt(image1,image2):
    save_in_logs(f"SIZE : {image1,image2}")
    save_in_logs(f"ENTROPY IM1 : {image1.entropy()} ENTROPY IM2 : {image2.entropy()}")
    save_in_logs(f"EXIF IM1 : {image1.getexif()} EXIF IM2 : {image2.getexif()}")
    save_in_logs(f"\n\n")
    save_in_logs(f"PSNR : {PSNR(np.array(image1),np.array(image2))}")
    save_in_logs(f"SSIM : {SSIM(np.array(image1),np.array(image2))}")
    save_in_logs(f"MSE  : {MSE(np.array(image1),np.array(image2))}")
    save_in_logs(f"\n\n")

