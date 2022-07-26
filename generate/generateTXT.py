from processing.compression import get_mse, get_psnr, get_ssim
from system import utils as u
from system.pck_S import scan

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
    save_in_logs(f"PSNR : {get_psnr(scan(image1),scan(image2))}")
    save_in_logs(f"SSIM : {get_ssim(scan(image1),scan(image2))}")
    save_in_logs(f"MSE  : {get_mse(scan(image1),scan(image2))}")
    save_in_logs(f"\n\n")

