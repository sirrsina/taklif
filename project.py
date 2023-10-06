from tkinter import *


def check():
    if noon>10:
        lbl_noon.config(text="Barbari 10")
    if noon<0:
        lbl_noon.config(text="Barbari 0")

def check1():
    if noon1>50:
        lbl_noon1.config(text="Lavash 50")
    if noon1<0:
        lbl_noon1.config(text="Lavash 0")

def up():
    global noon
    noon = noon+1
    lbl_noon.config(text=f"Barbari {noon}")
    check()
def down():
    global noon
    noon = noon-1
    lbl_noon.config(text=f"Barbari {noon}")
    check()
def up1():
    global noon1
    noon1 = noon1+5
    lbl_noon1.config(text=f"Lavash {noon1}")
    check1()
def down1():
    global noon1
    noon1 = noon1-5
    lbl_noon1.config(text=f"Lavash {noon1}")
    check1()
noon = 0
noon1 = 0
root = Tk()
btn1 = Button(root, text="Up", command=up)
lbl_noon = Label(root,text=0, bg='green')
btn2 = Button(root, text="Down", command=down)
btn1.pack()
lbl_noon.pack()
btn2.pack()
btn1 = Button(root, text="Up", command=up1)
lbl_noon1 = Label(root, bg='green')
btn2 = Button(root, text="Down", command=down1)
btn1.pack()
lbl_noon1.pack()
btn2.pack()
mainloop()
