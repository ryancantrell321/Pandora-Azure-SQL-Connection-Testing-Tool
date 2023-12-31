from tkinter import messagebox
import tkinter as tk
import webbrowser as web
import customtkinter as ctk


# Driver selector
def create_driver_dropdown(self, y_position):
    ctk.CTkLabel(self.master, text="Driver:", fg_color="black",
                 bg_color="black", font=("Helvetica", 15), padx=20).place(x=35, y=y_position)
    self.drivers = ["Select ODBC Driver", "{ODBC Driver 17 for SQL Server}", "{ODBC Driver 18 for SQL Server}"]
    self.selected_driver.set(self.drivers[0])

    driver_dropdown = ctk.CTkComboBox(self.master, variable=self.selected_driver, values=self.drivers, width=200)
    driver_dropdown.configure(fg_color="#b3b3b3", bg_color="black", text_color="black", button_hover_color="white",
                              state="readonly", dropdown_fg_color="white", dropdown_text_color="black",
                              dropdown_hover_color="black")
    driver_dropdown.place(x=175, y=y_position)


# reset:
def reset_button_click(self):
    for entry_name in ["server_entry", "database_entry", "username_entry", "password_entry"]:
        entry = getattr(self, entry_name)
        entry.delete(0, tk.END)

        self.selected_driver.set(self.drivers[0])


# help info:
def help_button_click(self):
    text = "To use this program, fill in all the blank fields and select an appropriate ODBC driver installed in your system.\n\nUsage Guidelines:\n\n1. Server: The URL or IP of your Azure SQL Database server.\n2. Database: The name of the target database.\n3. Username: Your database username.\n4. Password: Your database password.\n5. Driver: Select the appropriate ODBC Driver installed in your       system.\n6. After this, click on 'Test Connection' to test whether or not       your connection credentials are correct.\n7. To clear the fields, click the 'RESET' button.\n8. To see the License, click the 'LICENSE' button\n9. To quit the program, click the 'EXIT' button."
    text2 = "IMPORTANT NOTES:\nThis program expects that you have a stable internet connection and already have an ODBC driver installed in your system. If not, please install the driver from the official Microsoft Website by clicking on the 'Install Driver' Button."
    text3 = "In case of a successful connection, a message box with success status will pop up.\n\nIn case of a failed or unstable connection, a message box detailing error reasons will popup."
    messagebox.showinfo("Help", f"{text}\n\n{text2}\n\n{text3}")


# license info:
def license_button_click(self):
    text = """Pandora Database Connection Tester (AZURE SQL) © 2023 by Pandora Dynamics LLP is licensed under CC BY-ND 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-nd/4.0/"""
    messagebox.showinfo("LICENSE", f"{text}")
    web.open("https://creativecommons.org/licenses/by-nd/4.0/")


# Install Driver:
def install_driver_button_click(self):
    text = "Once you click 'Ok', you will be redirected to official Microsoft website where you can download the ODBC Driver from.\n\nLink:\nhttps://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16"
    messagebox.showinfo("Install ODBC Driver", f"{text}")
    web.open("https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16")


# About:
def about_button_click(self):
    text = """Presenting the Panddora Azure SQL Connection Testing Tool —a streamlined tool crafted to aid developers in verifying the correctness of their Azure SQL database credentials.\n\nThis application is portable, eliminating the need for installation, and places a premium on security by abstaining from logging or storing any received or inputted information.\n\nDevelopers can employ this tool to ascertain the external accessibility of the intended database for their ongoing system development."""
    mail_text = """For any issues, bugs or queries, contact us at: pandoradynamics@gmail.com"""
    cp_text = "© 2023 PANDORA DYNAMICS LLP. All Rights Reserved."
    messagebox.showinfo("About", f"{text}\n\n{mail_text}\n\n{cp_text}")

