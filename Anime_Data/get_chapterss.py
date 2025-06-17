from pathlib import Path
from Anime_Data.get_season_paths import *



def get_chapters(paths, Season):
    return len(paths) if Season == 2 else len(get_season_paths(paths))