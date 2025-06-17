import customtkinter as ctk
from pathlib import Path
import sys
from customtkinter import CTkImage
from PIL import Image
from memory_profiler import profile
from GUI_Commands.create_action import create_action
from GUI_Commands.hide_settings import hide_settings
from GUI_Commands.show_settings import show_settings
from GUI_Commands.show_result import show_result
from GUI_Commands.toggle_console import toggle_console
from GUI_Commands.update_theme import update_theme
from GUI_Commands.open_file_dialog import open_file_dialog



class AnimeDCApp(ctk.CTk):
    
    @profile
    def __init__(self, running_console):
        
        
        
        self.running_console = running_console
        
        super().__init__()
        
        
        
        self.title("Anime DC")
        self.geometry("500x800")
        self.iconbitmap("Media/icon.ico")
        self.resizable(False, False)
        self.console_visible = False



        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        
        self.bg_photo = CTkImage(
            light_image=Image.open(Path("Media/background_night.jpg")),
            size=(500, 800) 
        )

        self.background_label = ctk.CTkLabel(self, image=self.bg_photo, text="")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        

        self.title_label = ctk.CTkLabel(
            self,
            text="Anime DC",
            font=("Arial Bold", 28),
            text_color="#3498db"
        )
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")


        self.entry = ctk.CTkEntry(
            self,
            width=300,
            height=40,
            placeholder_text="Please enter your anime folder path...",
            corner_radius=10,
            font=("Arial", 14)
        )
        self.entry.place(relx=0.65, rely=0.3, anchor="e")
        
        self.browse_button = ctk.CTkButton(
            self,
            text="Browse",
            command=lambda : open_file_dialog(self=self),
            width=100,
            height=40
        )
        self.browse_button.place(relx=0.7, rely=0.3, anchor="w")


        self.create_btn = ctk.CTkButton(
            self,
            text="Create",
            width=150,
            height=40,
            corner_radius=10,
            font=("Arial Bold", 16),
            fg_color="#2980b9",
            hover_color="#2c3e50",
            command=lambda : create_action(self=self)
        )
        self.create_btn.place(relx=0.5, rely=0.4, anchor="center")


        self.settings_btn = ctk.CTkButton(
            self,
            text="⚙",
            width=35,
            height=35,
            corner_radius=17,
            
            hover_color=("#d0d0d0", "#2c3e50"),
            command=lambda: show_settings(self.settings_frame) 
        )
        self.settings_btn.place(relx=0.95, rely=0.05, anchor="ne")


        self.settings_frame = ctk.CTkFrame(
            self,
            width=500,
            height=800,
            fg_color=("white", "#2c3e50"),
            corner_radius=0
        )
        

        self.night_mode_var = ctk.BooleanVar(value=True)
        self.night_switch = ctk.CTkSwitch(
            self.settings_frame,
            text="Night Mode 🌙",
            font=("Arial", 14),
            progress_color="#3498db",
            variable=self.night_mode_var,
            command=lambda : update_theme(self=self)
        )
        self.night_switch.place(relx=0.5, rely=0.4, anchor="center")


        self.console_switch = ctk.CTkSwitch(
            self.settings_frame,
            text="Console 💻",
            font=("Arial", 14),
            progress_color="#3498db",
            command=lambda : toggle_console(self=self)
        )
        self.console_switch.place(relx=0.5, rely=0.5, anchor="center")


        self.back_btn = ctk.CTkButton(
            self.settings_frame,
            text="Back ↩",
            width=100,
            command=lambda: hide_settings(self.settings_frame)
        )
        self.back_btn.place(relx=0.5, rely=0.6, anchor="center")
        
        self.credit_label_1 = ctk.CTkLabel(
            self.settings_frame,
            text="Developer : Marco_darkl",
            text_color=("#7f8c8d", "#95a5a6"),
            font=("Arial", 10)
        )
        self.credit_label_1.place(relx=0.5, rely=0.86, anchor="center")
        
        
        self.credit_label_2 = ctk.CTkLabel(
            self.settings_frame,
            text="Thanks to Leonardo.ai for arranging the photos",
            text_color=("#7f8c8d", "#95a5a6"),
            font=("Arial", 10)
        )
        self.credit_label_2.place(relx=0.5, rely=0.94, anchor="center")
        
        self.credit_label_sp = ctk.CTkLabel(
            self.settings_frame,
            text="Special thanks to DeepSeek for his help with the code",
            text_color=("#7f8c8d", "#95a5a6"),
            font=("Arial", 10)
        )
        self.credit_label_sp.place(relx=0.5, rely=0.9, anchor="center")



 

