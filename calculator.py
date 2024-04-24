from tkinter import *


root = Tk()
root.title("Simple Calculator")                     #For Title
root.geometry("570x600")                            #PageSize "widthxheight"
root.resizable(False, False)
root.configure(bg="Black")
root.iconbitmap('calculator-icon.ico')              #Icon

#Founction for button and Calculations
equation = ""                                       #gobal Variable
def show(value):                                    #function for show buttons value
    global equation
    equation += value
    result_label.config(text=equation, fg="#FF8000")

def clear():                                        #functon for Clear Button
    global equation
    equation = ""
    result_label.config(text=equation)

def calculate():                                   #function for result Button
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""
    result_label.config(text=result)

#Calculator Display
result_label = Label(root,width=25,height=2,text="",font=("arial",30),bd=5)
result_label.pack()

# All Buttons
Button(root,text="+",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#3697f6",command=lambda:show("+")).place(x=10,y=120)
Button(root,text="-",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#3697f6",command=lambda:show("-")).place(x=150,y=120)
Button(root,text="*",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#3697f6",command=lambda:show("*")).place(x=290,y=120)
Button(root,text="C",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="blue",command=lambda:clear()).place(x=430,y=120)

Button(root,text="1",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#1F1F1F",command=lambda:show("1")).place(x=10,y=220)
Button(root,text="2",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#1F1F1F",command=lambda:show("2")).place(x=150,y=220)
Button(root,text="3",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#1F1F1F",command=lambda:show("3")).place(x=290,y=220)
Button(root,text="%",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#3697f6",command=lambda:show("%")).place(x=430,y=220)

Button(root,text="4",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#1F1F1F",command=lambda:show("4")).place(x=10,y=320)
Button(root,text="5",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#1F1F1F",command=lambda:show("5")).place(x=150,y=320)
Button(root,text="6",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#1F1F1F",command=lambda:show("6")).place(x=290,y=320)
Button(root,text="/",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#3697f6",command=lambda:show("/")).place(x=430,y=320)

Button(root,text="7",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#1F1F1F",command=lambda:show("7")).place(x=10,y=420)
Button(root,text="8",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#1F1F1F",command=lambda:show("8")).place(x=150,y=420)
Button(root,text="9",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#1F1F1F",command=lambda:show("9")).place(x=290,y=420)

Button(root,text="0",width=11,height=1,font="arial 30 bold",bd=1,fg="white",bg="#1F1F1F",command=lambda:show("0")).place(x=10,y=510)
Button(root,text=".",width=5,height=1,font="arial 30 bold",bd=1,fg="white",bg="#1F1F1F",command=lambda:show(".")).place(x=290,y=510)
Button(root,text="=",width=5,height=3,font="arial 30 bold",bd=1,fg="white",bg="yellow",command=lambda:calculate()).place(x=430,y=420)


root.mainloop()