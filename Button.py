from tkinter import *

root = Tk()

def myClick():
    myLabel=Label(root,text="Clicked on the button")
    myLabel.grid(row=2,column=1)
    #myLabel.pack()
    
#Creating a Button Widget,
myButton1 = Button(root, text="Click 1",state=DISABLED)
myButton2=Button(root, text="Click 2",padx=50,pady=10,command=myClick,fg="blue",bg="red")
#Shoving it onto the screen
myButton1.grid(row=5,column=0)
myButton2.grid(row=6,column=0)

root.mainloop()
