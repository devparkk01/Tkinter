import tkinter as tk
from tkinter import ttk

#  creating a window
win = tk.Tk()
# default size , width * height
win.geometry("300x500")
# to prevent gui from being resizable , i.e , We can't change the size of
# gui . We need to use resizable() method

win.resizable( 0 , 0 )
win.title("Python Gui")

#  ttk stands for themed tkinter . It's like a sub module inside tkinter
# We can create nice widgets with the help of ttk
# Some of the most common widgets include Label ,Frame , Button , Entry , Combobox, Notebook ,
# Radiobutton , CheckButton , MenuButton


# Creating a label
labelOne = ttk.Label(win , text = "Label One" , foreground = "red" , background = "grey", width = 10 )
# above code is only going to create a label , if we run the code now , we won't see it in the gui
#  This is because we haven't packed it , in other words  we haven't yet placed it in our gui .
# In order to place it , we can use two methods , pack() and grid() .

labelOne.grid(row = 0 , column = 0 , sticky = tk.W)
#  Now since we've placed it , we can see the label now .

#  creating another label
labelTwo = ttk.Label(win , text = "Label Two" , foreground = "#76ad98",  background = "grey" ,width = 10)
#  Now place the label
labelTwo.grid(row = 1 , column = 0 ,sticky = tk.W)


win.mainloop()
