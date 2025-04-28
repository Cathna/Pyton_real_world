from tkinter import *



window=Tk()

#test functions using the print function to check it works
def km_to_miles():
    #print(e1_value.get())
    #the blow converts any numbers into floats for the multiplication
    miles=float(e1_value.get()) *1.6
    t1.insert(END,miles)

b1=Button(window, text="Button",command=km_to_miles)
#two options for placing a widget, pack or grid
#b1.pack()
b1.grid(row=0, column=0)
#Entry is a text entry widget
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0, column=1)

t1=Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()