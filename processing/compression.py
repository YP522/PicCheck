from PIL import Image
import system.utils as u
from pathlib import Path

# $quality = (101-(($width*$height)*3)/$filesize); in php

def getCompressionLevel(img,imgFile):

    path = f"{u.dt_string}/data/{imgFile}.png"
    quality = (101-((img.width*img.height)*3)/(Path(path).stat().st_size))    
    return quality;
