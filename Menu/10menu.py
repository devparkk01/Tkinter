#  we will replicate the menubar in vs code 
import tkinter as tk 
from tkinter import ttk 

win = tk.Tk()
win.title("Python GUI")

def func() :
    print("Hello Dev")

mainMenu = tk.Menu(win ) # menubar 

fileMenu = tk.Menu (mainMenu  , tearoff = 0 ) # To prevent the tearoff , we pass an argumet `tearoff` with the value 0 
fileMenu.add_command(label = "New File" , command = func )
fileMenu.add_command(label = "New Window" , command = func )
fileMenu.add_separator() 
fileMenu.add_command(label = "Open File" , command = func )
fileMenu.add_command(label = "Open Folder" , command = func )
fileMenu.add_command(label = "Open Workspace" , command = func )
fileMenu.add_separator()
fileMenu.add_command(label = "Save" , command = func )
fileMenu.add_command(label = "Save As" , command = func )

editMenu = tk.Menu(mainMenu , tearoff = 0 )

editMenu.add_command(label = "Undo" , command = func)
editMenu.add_command(label = "Redo" , command = func)
editMenu.add_separator()
editMenu.add_command(label = "Cut" , command = func)
editMenu.add_command(label = "Copy" , command = func)
editMenu.add_command(label = "Paste" , command = func)

selectionMenu = tk.Menu(mainMenu , tearoff  = 0 )
selectionMenu.add_command(label = "Select all" , command = func)
selectionMenu.add_command(label = "Expand Selection" , command = func)

mainMenu.add_cascade(label = 'File' , menu = fileMenu)
mainMenu.add_cascade(label = 'Edit' , menu = editMenu)
mainMenu.add_cascade(label = 'Selection' , menu = selectionMenu)


mainMenu.add_command ( label= "View" , command = func )




win.config( menu = mainMenu)
win.mainloop() 