from tkinter import *
import functools
from Skin_Data_Base import *
import customtkinter
import random


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # config window
        self.title("overwatch")
        self.geometry(f"{1300}x{600}")

        # frame config
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=0)

        # frame to display the skin
        self.skin_frame = customtkinter.CTkFrame(self)
        self.skin_frame.grid(row=0, column=1, ipadx=300, padx=20, pady=30)

        text = ""
        text_label = StringVar()

        self.label = customtkinter.CTkLabel(self.skin_frame, textvariable=text_label,
                                            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label.pack()

        # frame to display the hero buttons
        self.tank_frame = customtkinter.CTkFrame(self)
        self.tank_frame.grid(row=2, column=0, padx=10, pady=15, sticky="n")
        self.damage_frame = customtkinter.CTkFrame(self)
        self.damage_frame.grid(row=2, column=1, padx=10, pady=15, sticky="n")
        self.support_frame = customtkinter.CTkFrame(self)
        self.support_frame.grid(row=2, column=2, padx=10, pady=15, sticky="n")

        btn_list = []

        def create_button(mas, btn_num, columns, func_list, mas_list):
            column = 0
            row = 0
            while btn_num != 0:
                for i in range(btn_num):
                    if column <= columns:
                        button = customtkinter.CTkButton(master=mas, text=func_list[i], width=110, height=40,
                                                         command=lambda: randomizer(mas_list))
                        button.grid(row=row, column=column)
                        column += 1
                        btn_list.append(button)
                    else:
                        row += 1
                        button = customtkinter.CTkButton(master=mas, text=func_list[i], width=110, height=40,
                                                         command=lambda: randomizer(mas_list))
                        button.grid(row=row, column=0)
                        column = 1
                        btn_list.append(button)
                break
        create_button(mas=self.tank_frame, btn_num=11, columns=2, func_list=tank_names,mas_list= tank_heroes)
        create_button(mas=self.damage_frame, btn_num=17, columns=4, func_list=damage_names,mas_list=damage_heroes)
        create_button(mas=self.support_frame, btn_num=8, columns=2, func_list=support_names,mas_list=support_heroes)

        def randomizer(hero):
            clean()

            global text

            text = text + str(hero)

            text = random.choice(hero)
            text_label.set(text)

        def clean():
            global text

            text = ""

            text_label.set("")


if __name__ == "__main__":
    app = App()
    app.mainloop()
