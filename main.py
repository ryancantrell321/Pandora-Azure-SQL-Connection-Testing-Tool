"""
Created on TUE Dec 19 2023:
@author: RYANCANTRELL321
Organization: Pandora Dynamics LLP
@email: pandoradynamics@gmail.com
Program Name: PANDORA DATABASE CONNECTION TESTER (AZURE SQL)

"""
from src.gui_initialization import *
from splash_screen import SplashScreen
from src.mechanisms.dependencies_checker import dependencies


dependencies("requirements.txt")


# Configuration:
class AzureSQLConnectionTester:
    def __init__(self, master):
        self.drivers = None
        self.password_entry = None
        self.username_entry = None
        self.database_entry = None
        self.server_entry = None
        self.driver_entry = None
        self.selected_driver = tk.StringVar()
        self.master = master
        master.title("PANDORA MICROSOFT AZURE SQL CONNECTION TESTING TOOL")
        master.geometry("500x500+400+100")
        master.resizable(False, False)

        configure_icon(self.master, "src/img/ico/icons8-database-94.ico")
        configure_bg_image(self.master, "src/img/bg_abstract.jpg", 500, 500)
        create_widgets(self)

        self.show_password_var = tk.BooleanVar()
        self.show_password_var.set(False)

        show_pwd_checkbox = ctk.CTkCheckBox(self.master, text="Show", variable=self.show_password_var,
                                            checkbox_width=25, width=20, bg_color="black", fg_color="#005e80",
                                            hover_color="#e6e6e6", command=lambda: toggle_password_visibility(self))
        show_pwd_checkbox.place(x=390, y=175)


if __name__ == "__main__":
    splash_root = ctk.CTk()
    splash = SplashScreen(splash_root)
    splash_root.mainloop()
    splash_root.update()

    window = ctk.CTk()
    app = AzureSQLConnectionTester(window)
    window.mainloop()
