from pathlib import Path
import cv2
from Anime_Data.get_season_paths import *

def get_times(paths, Season):
    time = []
    target_paths = paths if Season == 2 else get_season_paths(paths)
    
    for file in target_paths:
        cap = cv2.VideoCapture(file)
        try:
            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration = frame_count / fps
            time.append(round(duration))
        finally:
            if cap.isOpened():
                cap.release()
    return time