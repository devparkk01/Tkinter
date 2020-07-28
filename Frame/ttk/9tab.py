# we will see how to create tabs/notebooks widget . 
# basic idea about tabs here .

import tkinter as tk 
from tkinter import ttk 

win = tk.Tk()
win.title("Python GUI")
# creating a notebook
nb = ttk.Notebook(win )

# creating a page which is nothing but a frame 
page1 = ttk.Frame(nb )
# creating another frame 
page2 = ttk.Frame(nb)



# adding pages (frames ) to the notebooks 
nb.add(page1 , text ="Tab1")
nb.add(page2 , text = "Tab2") 

# placing notebook `nb`
# we won't use grid() method for placing notebook
# rather we will use pack() method

nb.pack(expand = True , fill = 'both' )


win.mainloop() 