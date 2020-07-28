#  we will create drop down menu here 
import tkinter as tk 
from tkinter import ttk 

win = tk.Tk()
win.title("Python GUI")

def func() :
    print("Hello Dev")


# creating a menubar 

mainMenu = tk.Menu(win )

# creating a dropdown menubar 
fileMenu = tk.Menu(mainMenu , tearoff = 0 )
# to prevent the tearoff , we pass an argument `tearoff` with the value = 0 

# adding menus to the dropdown menu `fileMenu`
fileMenu.add_command(label = "New File" , command = func )
fileMenu.add_command(label = "New Window" , command = func)
fileMenu.add_separator()  # adding a separator between the menus in the dropdown menubar 
fileMenu.add_command (label = "Open File" , command = func)
mainMenu.add_cascade(label = "file" , menu = fileMenu)

mainMenu.add_command(label = "Edit" , command= func)
mainMenu.add_command(label = "Selection" , command = func)
mainMenu.add_command(label = "View" , command = func)
mainMenu.add_command(label = "Run" , command = func)

win.config(menu = mainMenu)




win.mainloop() 
