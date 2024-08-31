from tkinter import *
import random

widowmaker = [
    "Cote D'Azur",
    "Pale Serpent",
    "Ange De La Mort",
    "Cyberdevil",
    "Medusa",
    "Winter",
    "Rose"

]

cassidy = [
    "Mystery Man",
    "Invisible Man",
    "Space Raider",
    "Forest Ranger"

]

ashe = [
    "Poolside",
    "Warlock",
    "Socialite"

]

pharah = [
    "Security Chief",
    "Hades",
    "Sky Centurion"

]

soldier = [
    "Strike Commander Morrison",
    "Bug Hero",
    "Space Raider",
    "Venom"

]

def randomizer(num):
    clean()
    global answer
    answer = answer + str(num)

    # escolher skin
    if answer == "Widowmaker":
        answer = random.choice(widowmaker)
        answer_label.set(answer)

    if answer == "Cassidy" :
        answer = random.choice(cassidy)
        answer_label.set(answer)

    if answer == "Ashe":
        answer = random.choice(ashe)
        answer_label.set(answer)

    if answer == "Phara":
        answer = random.choice(pharah)
        answer_label.set(answer)

    if answer == "Soldier76":
        answer = random.choice(soldier)
        answer_label.set(answer)

def clean():
    global answer
    answer = ""
    answer_label.set("")



wind = Tk()
wind.geometry("600x600")
wind.config(background="white")
wind.title("Overwatch skin randomizer")

#labels


answer = ""
answer_label = StringVar()

label = Label(wind,textvariable=answer_label,font=("",20), width=24, height=2)
label.pack()

frame = Frame(wind)
frame.pack()

#button

button = Button(frame,text="Widowmaker", height=2, width=11, font=20, command= lambda : randomizer("Widowmaker"))
button.grid(row=0,column=0)

button2 = Button(frame, text="Cassidy", height=2, width=11, font=20, command= lambda : randomizer("Cassidy"))
button2.grid(row=0, column=1)

button3 = Button(frame, text="Ashe", height=2, width=11, font=20, command= lambda : randomizer("Ashe"))
button3.grid(row=0, column=2)

button4 = Button(frame, text="Phara", height=2, width=11, font=20, command= lambda : randomizer("Phara"))
button4.grid(row=0, column=3)

button5 = Button(frame,text="Soldier76", height=2, width=11, font=20, command= lambda : randomizer("Soldier76"))
button5.grid(row=0,column=4)


wind.mainloop()







