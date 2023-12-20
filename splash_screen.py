# SplashScreen.py

from tkinter import ttk
import customtkinter
from src.gui_initialization import *


class SplashScreen:
    def __init__(self, master):
        self.progress_var = None
        self.master = master
        master.title("PANDORA MICROSOFT AZURE SQL CONNECTION TESTING TOOL")
        master.geometry("500x500+400+100")
        master.resizable(False, False)
        master.overrideredirect(True)

        configure_bg_image(self.master, "src/img/splash.png", 500, 700)

        self.create_widgets()

    def create_widgets(self):

        self.progress_var = tk.DoubleVar()
        progress_bar = ttk.Progressbar(self.master, variable=self.progress_var, length=400, mode="determinate")
        progress_bar.place(x=50, y=450)
        self.load_data()

    def load_data(self):
        for i in range(101):
            self.progress_var.set(i)
            self.master.update_idletasks()
            self.master.update()
            self.master.after(25)
        self.master.after(2100, self.master.destroy)


# Run
if __name__ == "__main__":
    splash_root = customtkinter.CTk()
    splash = SplashScreen(splash_root)
    splash_root.mainloop()
