from tkinter import *
import math

root = Tk()
root.title("Simple Calculator")

def Back():
    oldval=e.get()
    e.delete(0,END)
    l=len(oldval)
    e.insert(0,oldval[0:l-1])

def Division():
    global oldNumber
    global mathcalc
    mathcalc="div"
    oldNumber=e.get()
    e.delete(0,END)

def Multiplication():
    global oldNumber
    global mathcalc
    mathcalc="mul"
    oldNumber=e.get()
    e.delete(0,END)

def Subtraction():
    global oldNumber
    global mathcalc
    mathcalc="sub"
    oldNumber=e.get()
    e.delete(0,END)

def Addition():
    global oldNumber
    global mathcalc
    mathcalc="add"
    oldNumber=e.get()
    e.delete(0,END)

def Inverse():
    oldNumber=e.get()
    e.delete(0,END)
    e.insert(0,1/float(oldNumber))

def Square():
    oldNumber=e.get()
    e.delete(0,END)
    e.insert(0,float(oldNumber)*float(oldNumber))

def SquareRoot():
    oldNumber=e.get()
    result=math.sqrt(float(oldNumber))
    e.delete(0,END)
    e.insert(0,result)

def Percentage():
    newNumber=e.get()
    e.delete(0,END)
    result=float(newNumber)/100
    e.insert(0,result) 
   

def Equal():
    newNumber=e.get()
    e.delete(0,END)
    if mathcalc=="div":
        result=float(oldNumber)/float(newNumber)
        e.insert(0,result)
    elif mathcalc=="mul":
        result=float(oldNumber)*float(newNumber)
        e.insert(0,result)
    elif mathcalc=="sub":
        result=float(oldNumber)-float(newNumber)
        e.insert(0,result)
    elif mathcalc=="add":
        result=float(oldNumber)+float(newNumber)
        e.insert(0,result)    
    else:
        exit
                    
    

def button_click(newval):    
    oldval=e.get()
    if oldval=="0" :
        oldval=""
            
       
    e.delete(0,END)
    e.insert(0,str(oldval)+str(newval))

def Clear():
    global oldNumber
    global mathcalc
    mathcalc=""
    oldNumber=0
    e.delete(0,END)

def ClearError():
    e.delete(0,END)

def Plusminus():
    oldval=float(e.get())*-1
    e.delete(0,END)
    e.insert(0,oldval)   
    




#Creating Entry box
e=Entry(root,font=("Calibri",20), borderwidth=3)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


button_pcent = Button(root, text="%",padx=24,pady=20,command=Percentage)
button_ce = Button(root, text="CE",padx=20,pady=20,command=ClearError)
button_c = Button(root, text="C",padx=20,pady=20,command=Clear)
button_back = Button(root, text="<",padx=20,pady=20,command=Back)

button_inv = Button(root, text="1/x",padx=19,pady=20,command=Inverse)
button_sqr = Button(root, text="x^2",padx=18,pady=20,command=Square)
button_sqroot = Button(root, text="Sqrt",padx=15,pady=20,command=SquareRoot)
button_div = Button(root, text="÷",padx=20,pady=20,command=Division)

button_7 = Button(root, text="7",padx=24,pady=20,command=lambda: button_click(7))
button_8 = Button(root, text="8",padx=24,pady=20,command=lambda: button_click(8))
button_9 = Button(root, text="9",padx=20,pady=20,command=lambda: button_click(9))
button_multi = Button(root, text="X",padx=20,pady=20,command=Multiplication)

button_4 = Button(root, text="4",padx=24,pady=20,command=lambda: button_click(4))
button_5 = Button(root, text="5",padx=24,pady=20,command=lambda: button_click(5))
button_6 = Button(root, text="6",padx=20,pady=20,command=lambda:button_click(6))
button_sub = Button(root, text="-",padx=20,pady=20,command=Subtraction)

button_1 = Button(root, text="1",padx=24,pady=20,command=lambda: button_click(1))
button_2 = Button(root, text="2",padx=24,pady=20,command=lambda: button_click(2))
button_3 = Button(root, text="3",padx=20,pady=20,command=lambda: button_click(3))
button_add = Button(root, text="+",padx=20,pady=20,command=Addition)

button_plusminus = Button(root,text="+/-",padx=19,pady=20,command=Plusminus)
button_0 = Button(root, text="0",padx=24,pady=20,command=lambda: button_click(0))
button_dot = Button(root, text=".",padx=20,pady=20,command=lambda: button_click("."))
button_equal = Button(root, text="=",padx=20,pady=20,command=Equal)

button_pcent.grid(row=1,column=0)
button_ce.grid(row=1,column=1)
button_c.grid(row=1,column=2)
button_back.grid(row=1,column=3)

button_inv.grid(row=2,column=0)
button_sqr.grid(row=2,column=1)
button_sqroot.grid(row=2,column=2)
button_div.grid(row=2,column=3)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_multi.grid(row=3,column=3)

button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)
button_sub.grid(row=4,column=3)

button_1.grid(row=5,column=0)
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2)
button_add.grid(row=5,column=3)

button_plusminus.grid(row=6,column=0)
button_0.grid(row=6,column=1)
button_dot.grid(row=6,column=2)
button_equal.grid(row=6,column=3)




root.mainloop()
