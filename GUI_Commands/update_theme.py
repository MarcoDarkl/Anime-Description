import customtkinter as ctk
from customtkinter import CTkImage
from pathlib import Path
from PIL import Image


def update_theme(self):

    if hasattr(self, 'background_label'):
        self.background_label.destroy()

    bg_image_path = (
        Path("Media/background_night.jpg") 
        if self.night_mode_var.get() 
        else Path("Media/background_light.jpg")
    )

    try:

        self.bg_image = CTkImage(
            light_image=Image.open(bg_image_path),
            dark_image=Image.open(bg_image_path),
            size=(500, 800)
        )


        self.background_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.lower() 
        
        
        if self.night_mode_var.get():
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")
        
    except FileNotFoundError:
        print(f"Error: File {bg_image_path} not found!")

        self.background_label = ctk.CTkLabel(self, text="", 
                                           fg_color=("#FFFFFF", "#2c3e50"))
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)