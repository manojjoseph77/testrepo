from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image change")
root.iconbitmap('bbva_logo.ico')
button_quit=Button(root,text='Exit program',command=root.quit)

button_quit.pack()


root.mainloop()
