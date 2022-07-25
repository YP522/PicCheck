from system import utils as u
from pathlib import Path

def create_folders():
    """
    Create folders for the project
    """
    Path(u.dt_string+"/data/color/normal").mkdir(parents=True, exist_ok=True)
    Path(u.dt_string+"/data/color/grayscale").mkdir(parents=True, exist_ok=True)
    Path(u.dt_string+"/report/assets/themes").mkdir(parents=True, exist_ok=True)

    Path(u.dt_string+"/data/dct/img1/tiles/").mkdir(parents=True, exist_ok=True)  
    Path(u.dt_string+"/data/dct/img2/tiles/").mkdir(parents=True, exist_ok=True) 

    Path(u.dt_string+"/data/idct/img1/tiles/").mkdir(parents=True, exist_ok=True)  
    Path(u.dt_string+"/data/idct/img2/tiles/").mkdir(parents=True, exist_ok=True) 

