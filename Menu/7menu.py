# here , we will see how to create a menu 

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python Gui")
#  we will use tk module to create Menu
# we don't use pack() or grid() here 
# instead we are gonna use config() method 


def func() : 
    print("hello Dev")


fileMenu = tk.Menu(win)  # creating a menubar `fileMenu` inside `win`
#  Now we will add menus to the menu bar created 
fileMenu.add_command(label = "Save" ,command =  func ) # adding a menu to the menubar `fileMenu`
# argument `label` specifies the name of the menu created , `command`  argument specifies what function will be 
# called when we click that menu .

win.config(menu = fileMenu) # finally configuring the menubar 




win.mainloop()
