#  it's about frame
from tkinter import *

root = Tk()
root.geometry("600x400")
root.minsize(400, 300)
root.maxsize(800, 600)
root.title("Python gui")
#  creating a frame
f1 = Frame(root , bg ="red" , borderwidth = 6 ,  relief = SUNKEN )
f1.pack(side = "left", fill = "y" )
labelOne = Label(f1 , text ="LabelOne" , fg = "green")
labelOne.pack(padx = 40 , pady = 20 )

#  creting another frame
f2 = Frame(root , bg= "cyan" , borderwidth = 8,  relief = SUNKEN )
f2.pack(side = "top" , fill = "x")

labelTwo = Label(f2 , text= "LabelTwo" , fg = "#dd8808")
labelTwo.pack(pady = 40)


root.mainloop()