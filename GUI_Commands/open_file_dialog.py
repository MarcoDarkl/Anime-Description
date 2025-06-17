from tkinter import filedialog

def open_file_dialog(self):
    folder_path = filedialog.askdirectory(
        title="Select a Folder",
        mustexist=True
    )
    if folder_path:
        self.entry.delete(0, "end")
        self.entry.insert(0, folder_path)