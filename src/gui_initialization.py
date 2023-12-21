import tkinter as tk
import customtkinter as ctk
import os
from PIL import ImageTk, Image
from src.mechanisms.azure_tester import test_azure_sql_connection
from src.mechanisms.button_mechanisms import *
from src.mechanisms.entry_field_mechanisms import *


# UI:
def create_widgets(self):
    create_entry(self, "Server:", 25)
    create_entry(self, "Database:", 75)
    create_entry(self, "Username:", 125)
    pwd_entry(self, "Password:", 175)
    create_driver_dropdown(self, 225)

    # buttons:
    test_button = ctk.CTkButton(master=self.master, width=160, text="TEST CONNECTION", font=("Helvetica", 15, "bold"),
                                fg_color="#004d1a", bg_color="#010119", hover_color="#003311",
                                command=lambda: test_azure_sql_connection(self))
    test_button.place(x=75, y=275)

    reset_button = ctk.CTkButton(master=self.master, width=160, text="RESET", font=("Helvetica", 15, "bold"),
                                 fg_color="#66001a", bg_color="black", hover_color="#33000d",
                                 command=lambda: reset_button_click(self))

    reset_button.place(x=270, y=275)

    help_button = ctk.CTkButton(master=self.master, width=160, text="HELP", font=("Helvetica", 15, "bold"),
                                fg_color="#1a0033", bg_color="black", hover_color="#330066",
                                command=lambda: help_button_click(self))
    help_button.place(x=75, y=325)

    license_button = ctk.CTkButton(master=self.master, width=160, text="LICENSE", font=("Helvetica", 15, "bold"),
                                   fg_color="#93931f", bg_color="black", hover_color="#b3b300",
                                   command=lambda: license_button_click(self))
    license_button.place(x=270, y=325)

    install_button = ctk.CTkButton(master=self.master, width=160, text="INSTALL DRIVER",
                                   font=("Helvetica", 15, "bold"), fg_color="#994f00", bg_color="black",
                                   hover_color="#804200", command=lambda: install_driver_button_click(self))
    install_button.place(x=75, y=375)

    about_button = ctk.CTkButton(master=self.master, width=160, text="ABOUT",
                                 font=("Helvetica", 15, "bold"), fg_color="#993366", bg_color="black",
                                 hover_color="#73264d", command=lambda: about_button_click(self))
    about_button.place(x=270, y=375)

    exit_button = ctk.CTkButton(master=self.master, width=160, text="EXIT", font=("Helvetica", 15, "bold"),
                                fg_color="#005e80", bg_color="black", hover_color="#00384d",
                                command=lambda: quit())
    exit_button.place(x=175, y=425)

    # Footer:
    cp_text = "© 2023 PANDORA DYNAMICS LLP. All Rights Reserved."
    footer = ctk.CTkLabel(master=self.master, width=500, text=cp_text, fg_color="#00394d")
    footer.place(x=0, y=475)


def configure_icon(master, icon_path):
    master.iconbitmap(icon_path)


def configure_bg_image(master, bg_image_path, bw, bh):

    script_dir = os.path.dirname(__file__)
    bg_image_path = os.path.join(script_dir, bg_image_path)

    bg = Image.open(bg_image_path)
    bg = bg.resize((bw, bh))
    bg_image = ImageTk.PhotoImage(bg)
    bg_label = ctk.CTkLabel(master=master, image=bg_image, text="")
    bg_label.pack()


