from pathlib import Path
from Anime_Data.get_season_paths import *



def save(path, name, seasons, chapters, time, Season):
    

    
    file_path = Path(path) / "Description.txt"
    avg_time = sum(time) / len(time)
    total_time = sum(time)
    
    min = f"{int(avg_time // 3600)}:{int((avg_time % 3600) // 60):02d}:{int(avg_time % 60):02d}"
    max = f"{int(total_time // 3600)}:{int((total_time % 3600) // 60):02d}:{int(total_time % 60):02d}"
    
    with open(file_path, "w", encoding="utf-8") as file:
        content = f"""————————————————————————————Anime————————————————————————————
        
Name : {name}
        
Seasons : {1 if Season == 2 else seasons}
        
Episodes : {chapters}
        
T. Time : {max}
        
Avg. Time : {min}
        
—————————————————————————————————————————————————————————————"""
        file.write(content)