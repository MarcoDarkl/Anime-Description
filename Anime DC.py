from win32gui import GetForegroundWindow as WindowId, ShowWindow as select
from win32con import SW_HIDE as hide, SW_SHOW as show
from GUI import AnimeDCApp
from Data.ascii_art import ascii_art
import threading



def art():
    ascii_art()

        
        
        
def console() :
    global running_console
    running_console = WindowId()
    select(running_console, hide)


t1 = threading.Thread(target=art)
t2 = threading.Thread(target=console)

t1.start () ,t2.start()

t1.join() ,t2.join()
if __name__ == "__main__":
    app = AnimeDCApp(running_console)
    app.mainloop()