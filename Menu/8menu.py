# More about menus and menubar 

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

def func() :
    print("Hello Dev")

# creating menubar 

MainMenu = tk.Menu(win ) # created inside win

# creating menus
save = MainMenu.add_command(label = "Save" , command = func )
options = MainMenu.add_command(label = "Options" , command = func)
run = MainMenu.add_command(label = "Run" , command = func)
terminal = MainMenu.add_command(label = "Terminal" , command = func )

#  configuring the menubar 
win.config(menu = MainMenu)



win.mainloop() 
