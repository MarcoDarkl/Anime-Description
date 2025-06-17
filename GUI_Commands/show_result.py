import customtkinter as ctk


def show_result(self, text, color):
    result_label = ctk.CTkLabel(
        self,
        text=text,
        text_color=color,
        font=("Arial", 12)
    )
    result_label.place(relx=0.5, rely=0.5, anchor="center")
    self.after(3000, result_label.destroy)