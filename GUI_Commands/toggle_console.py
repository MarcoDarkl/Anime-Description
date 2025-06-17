import customtkinter as ctk
from win32gui import GetForegroundWindow as WindowId, ShowWindow as select
from win32con import SW_HIDE as hide, SW_SHOW as show


def toggle_console(self):
    self.console_visible = not self.console_visible
    select(self.running_console, show if self.console_visible else hide)