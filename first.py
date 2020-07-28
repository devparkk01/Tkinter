from tkinter import *

root = Tk()

root.title("Python Gui")
root.geometry("600x400") # default size when it opens
root.minsize(400 , 400 )  # minsize after changing the size
root.maxsize(800 , 600) # maxsize after changing the size

first_label = Label(text = "This is a label")
first_label.pack()


root.mainloop()
