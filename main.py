# Imports
from tkinter import *
from tkinter import messagebox
import os
import webbrowser

# Functions
def check_adb(): # Check ADB Devices
    print("\n*PLEASE CHECK THE TERMINAL FOR MORE INFO AND PROGRESS*")
    if messagebox.askokcancel("Warning!", "Are you sure about that?"):
        try:
            messagebox.showinfo("Info", "Please wait..." + "\nFinding ADB Devices...")
            os.system('adb devices')
        except:
            messagebox.showerror("Error!", "Could not execute command!")

def check_fastboot(): # Check Fastboot Devices
    print("\n*PLEASE CHECK THE TERMINAL FOR MORE INFO AND PROGRESS*")
    if messagebox.askokcancel("Warning!", "Are you sure about that?"):
        try:
            messagebox.showinfo("Info", "Please wait..." + "\nFinding Fastboot Devices...")
            os.system('fastboot devices')
        except:
            messagebox.showerror("Error!", "Could not execute command!")

def check_device(): # Check Device Model (fastboot getvar product)
    print("\n*PLEASE CHECK THE TERMINAL FOR MORE INFO AND PROGRESS*")
    messagebox.showinfo("Info", "Please make sure to boot into Bootloader (Fastboot) Mode before doing this action.")
    if messagebox.askokcancel("Warning!", "Are you sure about that?"):
        try:
            messagebox.showinfo("Info", "Please wait..." + "\nFinding Device Model...")
            os.system('./fastboot getvar product')
        except:
            messagebox.showinfo("Info", "Device Model: " + "dd")

def bootloader_mode(): # Enter Bootloader (Fastboot) Mode
    print("\n*PLEASE CHECK THE TERMINAL FOR MORE INFO AND PROGRESS*")
    if messagebox.askokcancel("Warning!", "Are you sure about that?"):
        try:
            messagebox.showinfo("Info", "Please wait..." + "\nEntering Bootloader (Fastboot) Mode...")
            os.system('./adb reboot bootloader')
        except:
            messagebox.showerror("Error!", "Could not execute command!")

def unlock_bootloader():
    print("\n*PLEASE CHECK THE TERMINAL FOR MORE INFO AND PROGRESS*")
    if messagebox.askokcancel("Warning", "You are about to UNLOCK THE BOOTLOADER ON YOUR PIXEL!!! *NOTE: by unlocking the BOOTLOADER, your Pixel will be fully wiped, yout Pixel's warranty will be VOID and some things will be broken on your Pixel!!!*"):
        if messagebox.askokcancel("Warning!", "Are you sure about that?"):
            try:
                messagebox.showinfo("Info", "Please wait..." + "\nUnlocking Bootloader...")
                os.system('./fastboot flashing unlock')
            except:
                messagebox.showerror("Error!", "Could not execute command!")

def lock_bootloader():
    print("\n*PLEASE CHECK THE TERMINAL FOR MORE INFO AND PROGRESS*")
    if messagebox.askokcancel("Warning!", "Are you sure about that?"):
        try:
            messagebox.showinfo("Info", "Please wait..." + "\nLocking Bootloader...")
            os.system('./fastboot oem lock')      
        except:
            messagebox.showerror("Error!", "Could not execute command!")

def exit_bootloader():
    print("*\nPLEASE CHECK THE TERMINAL FOR MORE INFO AND PROGRESS*")
    if messagebox.askokcancel("Warning!", "Are you sure about that?"):
        try:
            messagebox.showinfo("Info", "Please wait..." + "\nExiting Bootloader (Fastboot) Mode...")
            os.system('./fastboot reboot')
        except:
            messagebox.showeror("Error!", "Could not execute command!")

def about_app_func():
    messagebox.showinfo("Info", "PyUnlockè by ThatMacCat (KaungZinLin)." + "\n\nThis is an app created to easily Unlock/ Lock the Bootloader on Google Pixels and Stock Android while offering many more useful features." + "\n\nApp Version: PyUnlockè v0.1 (DEV) for Windows" + "\n\nHUGE THANKS FRO USING THIS APP!!!")

def github():
    webbrowser.open("https://github.com/KaungZinLin/PyUnlock")

def yt():
    webbrowser.open("https://youtu.be/dQw4w9WgXcQ")

def yt_2():
    webbrowser.open("https://youtu.be/9WZN3S_j9dQ")

# GUI Setup
window = Tk()

window.title("PyUnlockè")
window.resizable(False, False)
window.config(padx=50, pady=50)

# Labels
welcome_label = Label(text="Welcome to PyUnlockè!", font="20")
welcome_label.grid(row=0, column=0, columnspan=3)

pixel_stock = Label(text="\nGOOGLE PIXELS (and) STOCK ANDROID")
pixel_stock.grid(row=1, column=0, columnspan=3)

universal = Label(text="\nUNIVERSAL")
universal.grid(row=4, column=0, columnspan=3)

about_us = Label(text="\nMORE INFO")
about_us.grid(row=10, column=0, columnspan=3)

unlock = Label(text="Unlock Bootloader: ")
unlock.grid(row=2, column=0)

lock = Label(text="Lock Bootloader: ")
lock.grid(row=3, column=0)

check_adb_label = Label(text="Check ADB Devices: ")
check_adb_label.grid(row=5, column=0)

check_fastboot_label = Label(text="Check Fastboot Devices: ")
check_fastboot_label.grid(row=6, column=0)

check_model = Label(text="Check Device Model: ")
check_model.grid(row=7, column=0)

bootloder_boot = Label(text="Boot Bootloader Mode: ")
bootloder_boot.grid(row=8, column=0)

bootloader_exit = Label(text="Exit Bootloader Mode: ")
bootloader_exit.grid(row=9, column=0)

# Buttons
unlock_button = Button(text="Unlock Bootloader", width=16, command=unlock_bootloader)
unlock_button.grid(row=2, column=1)

lock_button = Button(text="Lock Bootloader", width=16, command=lock_bootloader)
lock_button.grid(row=3, column=1)

check_adb_button = Button(text="Check ADB Devices", width=16, command=check_adb)
check_adb_button.grid(row=5, column=1)

check_fastboot_button = Button(text="Check Fastboot Devices", width=16, command=check_fastboot)
check_fastboot_button.grid(row=6, column=1)

check_model_button = Button(text="Check Device Model", width=16, command=check_device)
check_model_button.grid(row=7, column=1)

enter_bootloader_button = Button(text="Boot Bootloader Mode", width=16, command=bootloader_mode)
enter_bootloader_button.grid(row=8, column=1)

exit_bootloader_button = Button(text="Exit Bootloader Mode", width=16, command=exit_bootloader)
exit_bootloader_button.grid(row=9, column=1)

github_button = Button(text="GitHub", width=15, command=github)
github_button.grid(row=11, column=0)

about_app = Button(text="About App", width=15, command=about_app_func)
about_app.grid(row=11, column=1)

yt_button = Button(text="YouTube...", width=15, command=yt)
yt_button.grid(row=12, column=0)

yt_button_2 = Button(text="YouTube (2)...", width=15, command=yt_2)
yt_button_2.grid(row=12, column=1)

window.mainloop()