import customtkinter as ctk
import threading , cProfile
from memory_profiler import profile
from Anime_Data.get_chapterss import *
from Anime_Data.get_name import *
from Anime_Data.get_paths import *
from Anime_Data.get_season_paths import *
from Anime_Data.get_seasons import *
from Anime_Data.get_times import *
from Anime_Data.save import *
from GUI_Commands.show_result import *


@profile
def create_action(self):
    path = self.entry.get().strip()
    if not path:
        show_result(self,"Error: Empty path!", "#e74c3c")
        return
     
    try:
        
        profiler = cProfile.Profile()
        profiler.enable()
        
        def G_name() :
            global name
            name = get_name(path)
            
        
        def G_season_and_paths() :
            global paths , Season
            paths , Season = get_paths(path)
        
        def G_seasons() : 
            global seasons
            seasons = get_seasons(paths)
            
        def G_chapters() :
            global chapters    
            chapters = get_chapters(paths , Season=Season)
            
        def G_time() :  
            global time  
            time = get_times(paths, Season=Season)
        
        t1 = threading.Thread(target=G_season_and_paths)
        t2 = threading.Thread(target=G_name)
        t3 = threading.Thread(target=G_seasons)
        t4 = threading.Thread(target=G_chapters)
        t5 = threading.Thread(target=G_time)
        
        t1.start()
        
        t1.join()
        
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        
        
        t2.join()  
        t3.join()  
        t4.join()  
        t5.join()
        
        
        
             
        save(path, name, seasons, chapters, time, Season)
        show_result(self,"Description File Created!", "#2ecc71")
        print("Description File Created!\n")
        print(f"Description Location : {path}")
        profiler.disable()
        profiler.print_stats(sort='cumtime')
    except Exception as e:

        show_result(self, f"Error: {str(e)}", "#e74c3c")
        profiler.disable()
        profiler.print_stats(sort='cumtime')
        
