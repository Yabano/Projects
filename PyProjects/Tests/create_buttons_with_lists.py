from tkinter import *

root = Tk()


def func(name):
    print(name)


mylist = ['item1', 'item2', 'item3', "item4", "item5", "item6", "item7", "item8", "item9", "item10", "item11", "item12"]

for item in mylist:
    button = Button(root, text=item, command=lambda x=item: func(x))
    button.pack()

root.mainloop()
