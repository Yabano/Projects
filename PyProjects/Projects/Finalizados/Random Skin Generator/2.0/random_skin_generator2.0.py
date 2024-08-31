from tkinter import *
from db import personagens
import random


def randomizer(hero):
    clean()

    global text

    text = hero

    text = random.choice(personagens[hero])
    text_label.set(text)

def clean():
    global text

    text = ""

    text_label.set("")

# window configs
window = Tk()
window.geometry("500x500")
window.title("Overwatch skin randomizer")
window.config(background="white")
window.resizable(False,False)

# label configs

text = ""
text_label = StringVar()

label = Label(window,textvariable= text_label, height=2, width=20,font=("",25))
label.pack()

# frame config
frame = Frame(window)
frame.pack()

button1 = Button(frame,text="Ashe",width=18,height=2,font=("Consolas",11),command=lambda : randomizer(0))
button1.grid(row=0,column=0)

button2 = Button(frame,text="Bastion", width=18,height=2,font=("Consolas",11),command=lambda :  randomizer(1))
button2.grid(row=0,column=1)

button3 = Button(frame,text="Cassidy",width=18,height=2,font=("Consolas",11),command=lambda : randomizer(2))
button3.grid(row=0,column=2)

button4 = Button(frame,text="Echo", width=18,height=2,font=("Consolas",11),command=lambda :  randomizer(3))
button4.grid(row=1,column=0)

button5 = Button(frame,text="Genji",width=18,height=2,font=("Consolas",11),command=lambda : randomizer(4))
button5.grid(row=1,column=1)

button6 = Button(frame,text="Hanzo",width=18,height=2,font=("Consolas",11),command=lambda : randomizer(5))
button6.grid(row=1,column=2)

button7 = Button(frame,text="Junkrat", width=18,height=2,font=("Consolas",11),command=lambda :  randomizer(6))
button7.grid(row=2,column=0)

button8 = Button(frame,text="Mei", width=18,height=2,font=("Consolas",11),command=lambda :  randomizer(7))
button8.grid(row=2,column=1)

button9 = Button(frame,text="Phara",width=18,height=2,font=("Consolas",11),command=lambda : randomizer(8))
button9.grid(row=2,column=2)

button10 = Button(frame,text="Reaper", width=18,height=2,font=("Consolas",11),command=lambda :  randomizer(9))
button10.grid(row=3,column=0)

button11 = Button(frame,text="Sojourn",width=18,height=2,font=("Consolas",11),command=lambda : randomizer(10))
button11.grid(row=3,column=1)

button12 = Button(frame,text="Soldier: 76",width=18,height=2,font=("Consolas",11),command=lambda : randomizer(11))
button12.grid(row=3,column=2)

button13 = Button(frame,text="Sombra", width=18,height=2,font=("Consolas",11),command=lambda :  randomizer(12))
button13.grid(row=4,column=0)

button14 = Button(frame,text="Symmetra", width=18,height=2,font=("Consolas",11),command=lambda :  randomizer(13))
button14.grid(row=4,column=1)

button15 = Button(frame,text="Torbjörn",width=18,height=2,font=("Consolas",11),command=lambda : randomizer(14))
button15.grid(row=4,column=2)

button16 = Button(window,text="Tracer", width=18,height=2,font=("Consolas",11),command=lambda :  randomizer(15))
button16.place(x=88, y= 332)

button17 = Button(window,text="Widowmaker", width=18,height=2,font=("Consolas",11),command=lambda :  randomizer(16))
button17.place(x=242, y= 332)

window.mainloop()
