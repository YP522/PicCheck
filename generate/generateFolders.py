import os
from system import utils as u

def create_folders():
    """
    Create folders for the project
    """
    os.makedirs(u.dt_string+"/data/color/normal", exist_ok=True)
    os.makedirs(u.dt_string+"/data/color/grayscale", exist_ok=True)
    os.makedirs(u.dt_string+"/report/assets/themes", exist_ok=True)

    os.makedirs(u.dt_string+"/data/dct/img1/tiles/", exist_ok=True)  
    os.makedirs(u.dt_string+"/data/dct/img2/tiles/", exist_ok=True) 

    os.makedirs(u.dt_string+"/data/idct/img1/tiles/", exist_ok=True)  
    os.makedirs(u.dt_string+"/data/idct/img2/tiles/", exist_ok=True) 