from tkinter import *
from db import *
import customtkinter
import random
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Overwatch Random Skin Generator")
        self.geometry(f"{1450}x{650}")

        # tank heroes
        d_va_image = customtkinter.CTkImage(light_image=Image.open("Images/d_va.png"),
                                            dark_image=Image.open("Images/d_va.png"), size=(80, 100))
        doomfist_image = customtkinter.CTkImage(light_image=Image.open("Images/doomfist.png"),
                                                dark_image=Image.open("Images/doomfist.png"), size=(80, 100))
        junker_queen_image = customtkinter.CTkImage(light_image=Image.open("Images/junker_queen.png"),
                                                    dark_image=Image.open("Images/junker_queen.png"), size=(80, 100))
        orisa_image = customtkinter.CTkImage(light_image=Image.open("Images/orisa.png"),
                                             dark_image=Image.open("Images/orisa.png"), size=(80, 100))
        ramattra_image = customtkinter.CTkImage(light_image=Image.open("Images/ramattra.png"),
                                                dark_image=Image.open("Images/ramattra.png"), size=(80, 100))
        reinhardt_image = customtkinter.CTkImage(light_image=Image.open("Images/reinhardt.png"),
                                                 dark_image=Image.open("Images/reinhardt.png"), size=(80, 100))
        roadhog_image = customtkinter.CTkImage(light_image=Image.open("Images/roadhog.png"),
                                               dark_image=Image.open("Images/roadhog.png"), size=(80, 100))
        sigma_image = customtkinter.CTkImage(light_image=Image.open("Images/sigma.png"),
                                             dark_image=Image.open("Images/sigma.png"), size=(80, 100))
        winston_image = customtkinter.CTkImage(light_image=Image.open("Images/winston.png"),
                                               dark_image=Image.open("Images/winston.png"), size=(80, 100))
        wrecking_ball_image = customtkinter.CTkImage(light_image=Image.open("Images/wrecking_ball.png"),
                                                     dark_image=Image.open("Images/wrecking_ball.png"), size=(80, 100))
        zarya_image = customtkinter.CTkImage(light_image=Image.open("Images/zarya.png"),
                                             dark_image=Image.open("Images/zarya.png"), size=(80, 100))

        # dps heroes
        ashe_image = customtkinter.CTkImage(light_image=Image.open("Images/ashe.png"),
                                            dark_image=Image.open("Images/ashe.png"), size=(80, 100))
        bastion_image = customtkinter.CTkImage(light_image=Image.open("Images/bastion.png"),
                                               dark_image=Image.open("Images/bastion.png"), size=(80, 100))
        cassidy_image = customtkinter.CTkImage(light_image=Image.open("Images/cassidy.png"),
                                               dark_image=Image.open("Images/cassidy.png"), size=(80, 100))
        echo_image = customtkinter.CTkImage(light_image=Image.open("Images/echo.png"),
                                            dark_image=Image.open("Images/echo.png"), size=(80, 100))
        genji_image = customtkinter.CTkImage(light_image=Image.open("Images/genji.png"),
                                             dark_image=Image.open("Images/genji.png"), size=(80, 100))
        hanzo_image = customtkinter.CTkImage(light_image=Image.open("Images/hanzo.png"),
                                             dark_image=Image.open("Images/hanzo.png"), size=(80, 100))
        junkrat_image = customtkinter.CTkImage(light_image=Image.open("Images/junkrat.png"),
                                               dark_image=Image.open("Images/junkrat.png"), size=(80, 100))
        mei_image = customtkinter.CTkImage(light_image=Image.open("Images/mei.png"),
                                           dark_image=Image.open("Images/mei.png"), size=(80, 100))
        pharah_image = customtkinter.CTkImage(light_image=Image.open("Images/pharah.png"),
                                              dark_image=Image.open("Images/pharah.png"), size=(80, 100))
        reaper_image = customtkinter.CTkImage(light_image=Image.open("Images/reaper.png"),
                                              dark_image=Image.open("Images/reaper.png"), size=(80, 100))
        sojourn_image = customtkinter.CTkImage(light_image=Image.open("Images/sojourn.png"),
                                               dark_image=Image.open("Images/sojourn.png"), size=(80, 100))
        soldier_image = customtkinter.CTkImage(light_image=Image.open("Images/soldier.png"),
                                               dark_image=Image.open("Images/soldier.png"), size=(80, 100))
        sombra_image = customtkinter.CTkImage(light_image=Image.open("Images/sombra.png"),
                                              dark_image=Image.open("Images/sombra.png"), size=(80, 100))
        symmetra_image = customtkinter.CTkImage(light_image=Image.open("Images/symmetra.png"),
                                                dark_image=Image.open("Images/symmetra.png"), size=(80, 100))
        torbjorn_image = customtkinter.CTkImage(light_image=Image.open("Images/torbas.png"),
                                                dark_image=Image.open("Images/torbas.png"), size=(80, 100))
        tracer_image = customtkinter.CTkImage(light_image=Image.open("Images/tracer.png"),
                                              dark_image=Image.open("Images/tracer.png"), size=(80, 100))
        widowmaker_image = customtkinter.CTkImage(light_image=Image.open("Images/widowmaker.png"),
                                                  dark_image=Image.open("Images/widowmaker.png"), size=(80, 100))

        # support heroes
        ana_image = customtkinter.CTkImage(light_image=Image.open("Images/ana.png"),
                                           dark_image=Image.open("Images/ana.png"), size=(80, 100))
        baptiste_image = customtkinter.CTkImage(light_image=Image.open("Images/baptiste.png"),
                                                dark_image=Image.open("Images/baptiste.png"), size=(80, 100))
        brigitte_image = customtkinter.CTkImage(light_image=Image.open("Images/brigitte.png"),
                                                dark_image=Image.open("Images/brigitte.png"), size=(80, 100))
        kiriko_image = customtkinter.CTkImage(light_image=Image.open("Images/kiriko.png"),
                                              dark_image=Image.open("Images/kiriko.png"), size=(80, 100))
        lucio_image = customtkinter.CTkImage(light_image=Image.open("Images/lucio.png"),
                                             dark_image=Image.open("Images/lucio.png"), size=(80, 100))
        mercy_image = customtkinter.CTkImage(light_image=Image.open("Images/mercy.png"),
                                             dark_image=Image.open("Images/mercy.png"), size=(80, 100))
        moira_image = customtkinter.CTkImage(light_image=Image.open("Images/moira.png"),
                                             dark_image=Image.open("Images/moira.png"), size=(80, 100))
        zenyatta_image = customtkinter.CTkImage(light_image=Image.open("Images/zenyatta.png"),
                                                dark_image=Image.open("Images/zenyatta.png"), size=(80, 100))

        # grid config
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=0)

        # frame to display the skin
        self.skin_frame = customtkinter.CTkFrame(self)
        self.skin_frame.grid(row=0, column=1, padx=20, pady=30)

        text = ""
        self.text_label = StringVar()

        self.label = customtkinter.CTkLabel(self.skin_frame, textvariable=self.text_label,
                                            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label.pack()

        # appearance mode
        self.appearance_mode_frame = customtkinter.CTkFrame(self)
        self.appearance_mode_frame.grid(row=0, column=0)

        self.appearance_mode_label = customtkinter.CTkLabel(self.appearance_mode_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.appearance_mode_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionemenu.set("Dark")  # default value

        # frame to display the hero buttons
        self.tank_frame = customtkinter.CTkFrame(self,fg_color="transparent")
        self.tank_frame.grid(row=2, column=0, padx=10, pady=15, sticky="n")
        self.damage_frame = customtkinter.CTkFrame(self,fg_color="transparent")
        self.damage_frame.grid(row=2, column=1, padx=10, pady=15, sticky="n")
        self.support_frame = customtkinter.CTkFrame(self,fg_color="transparent")
        self.support_frame.grid(row=2, column=2, padx=10, pady=15, sticky="n")

        # tank heroes
        self.button1 = customtkinter.CTkButton(master=self.tank_frame, text="D_VA", compound="top", image=d_va_image,
                                               text_color="#000000", width=1, height=1, fg_color="#fafafa",
                                               hover_color="#ed6516", command=lambda: self.randomizer(d_va))
        self.button1.grid(row=0, column=0, padx=3, pady=3)

        self.button2 = customtkinter.CTkButton(master=self.tank_frame, text="Doomfist", text_color="#000000", compound="top", image=doomfist_image, width=1, height=1,
                                               fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(doomfist))
        self.button2.grid(row=0, column=1, padx=3, pady=3)

        self.button3 = customtkinter.CTkButton(master=self.tank_frame, text="Junker Queen", text_color="#000000", compound="top", image=junker_queen_image, width=1, height=1,
                                               fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(junker_queen))
        self.button3.grid(row=0, column=2, padx=3, pady=3)

        self.button4 = customtkinter.CTkButton(master=self.tank_frame, text="Orisa", text_color="#000000", compound="top", image=orisa_image, width=1, height=1,
                                               fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(orisa))
        self.button4.grid(row=1, column=0, padx=3, pady=3)

        self.button5 = customtkinter.CTkButton(master=self.tank_frame, text="Ranattra", text_color="#000000", compound="top", image=ramattra_image, width=1, height=1,
                                               fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(ramattra))
        self.button5.grid(row=1, column=1, padx=3, pady=3)

        self.button6 = customtkinter.CTkButton(master=self.tank_frame, text="Reinhardt", text_color="#000000", compound="top", image=reinhardt_image, width=1, height=1,
                                               fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(reinhardt))
        self.button6.grid(row=1, column=2, padx=3, pady=3)

        self.button7 = customtkinter.CTkButton(master=self.tank_frame, text="Roadhog", text_color="#000000", compound="top", image=roadhog_image, width=1, height=1,
                                               fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(roadhog))
        self.button7.grid(row=2, column=0, padx=3, pady=3)

        self.button8 = customtkinter.CTkButton(master=self.tank_frame, text="Sigma", text_color="#000000", compound="top", image=sigma_image, width=1, height=1,
                                               fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(sigma))
        self.button8.grid(row=2, column=1, padx=3, pady=3)

        self.button9 = customtkinter.CTkButton(master=self.tank_frame, text="Winston", text_color="#000000", compound="top", image=winston_image, width=1, height=1,
                                               fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(winston))
        self.button9.grid(row=2, column=2, padx=3, pady=3)

        self.button10 = customtkinter.CTkButton(master=self.tank_frame, text="Wrecking Ball", text_color="#000000", compound="top", image=wrecking_ball_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(wrecking_ball))
        self.button10.grid(row=3, column=0, padx=3, pady=3)

        self.button11 = customtkinter.CTkButton(master=self.tank_frame, text="Zarya", text_color="#000000", compound="top", image=zarya_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(zarya))
        self.button11.grid(row=3, column=1, padx=3, pady=3)

        # dps heroes
        self.button12 = customtkinter.CTkButton(master=self.damage_frame, text="Ashe", text_color="#000000", compound="top", image=ashe_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(ashe))
        self.button12.grid(row=0, column=0, padx=3, pady=3)

        self.button13 = customtkinter.CTkButton(master=self.damage_frame, text="Bastion", text_color="#000000", compound="top", image=bastion_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(bastion))
        self.button13.grid(row=0, column=1, padx=3, pady=3)

        self.button14 = customtkinter.CTkButton(master=self.damage_frame, text="Cassidy", text_color="#000000", compound="top", image=cassidy_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(cassidy))
        self.button14.grid(row=0, column=2, padx=3, pady=3)

        self.button15 = customtkinter.CTkButton(master=self.damage_frame, text="Echo", text_color="#000000", compound="top", image=echo_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(echo))
        self.button15.grid(row=0, column=3, padx=3, pady=3)

        self.button16 = customtkinter.CTkButton(master=self.damage_frame, text="Genji", text_color="#000000", compound="top", image=genji_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(genji))
        self.button16.grid(row=0, column=4, padx=3, pady=3)

        self.button17 = customtkinter.CTkButton(master=self.damage_frame, text="Hanzo", text_color="#000000", compound="top", image=hanzo_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(hanzo))
        self.button17.grid(row=1, column=0, padx=3, pady=3)

        self.button18 = customtkinter.CTkButton(master=self.damage_frame, text="Junkrat", text_color="#000000", compound="top", image=junkrat_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(junkrat))
        self.button18.grid(row=1, column=1, padx=3, pady=3)

        self.button19 = customtkinter.CTkButton(master=self.damage_frame, text="Mei", text_color="#000000", compound="top", image=mei_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(mei))
        self.button19.grid(row=1, column=2, padx=3, pady=3)

        self.button20 = customtkinter.CTkButton(master=self.damage_frame, text="Phara", text_color="#000000", compound="top", image=pharah_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(pharah))
        self.button20.grid(row=1, column=3, padx=3, pady=3)

        self.button21 = customtkinter.CTkButton(master=self.damage_frame, text="Reaper", text_color="#000000", compound="top", image=reaper_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(reaper))
        self.button21.grid(row=1, column=4, padx=3, pady=3)

        self.button22 = customtkinter.CTkButton(master=self.damage_frame, text="Sojourn", text_color="#000000", compound="top", image=sojourn_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(sojourn))
        self.button22.grid(row=2, column=0, padx=3, pady=3)

        self.button23 = customtkinter.CTkButton(master=self.damage_frame, text="Soldier 76", text_color="#000000", compound="top", image=soldier_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(soldier))
        self.button23.grid(row=2, column=1, padx=3, pady=3)

        self.button24 = customtkinter.CTkButton(master=self.damage_frame, text="Sombra", text_color="#000000", compound="top", image=sombra_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(sombra))
        self.button24.grid(row=2, column=2, padx=3, pady=3)

        self.button25 = customtkinter.CTkButton(master=self.damage_frame, text="Symmetra", text_color="#000000", compound="top", image=symmetra_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(symmetra))
        self.button25.grid(row=2, column=3, padx=3, pady=3)

        self.button26 = customtkinter.CTkButton(master=self.damage_frame, text="Torbjörn", text_color="#000000", compound="top", image=torbjorn_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(torbjorn))
        self.button26.grid(row=2, column=4, padx=3, pady=3)

        self.button27 = customtkinter.CTkButton(master=self.damage_frame, text="Tracer", text_color="#000000", compound="top", image=tracer_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(tracer))
        self.button27.grid(row=3, column=0, padx=3, pady=3)

        self.button28 = customtkinter.CTkButton(master=self.damage_frame, text="Widowmaker", text_color="#000000", compound="top", image=widowmaker_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516",  command=lambda: self.randomizer(widowmaker))
        self.button28.grid(row=3, column=1, padx=3, pady=3)

        # support heroes
        self.button29 = customtkinter.CTkButton(master=self.support_frame, text="Ana", text_color="#000000", compound="top", image=ana_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(ana))
        self.button29.grid(row=0, column=0, padx=3, pady=3)

        self.button30 = customtkinter.CTkButton(master=self.support_frame, text="Baptiste", text_color="#000000", compound="top", image=baptiste_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(baptiste))
        self.button30.grid(row=0, column=1, padx=3, pady=3)

        self.button31 = customtkinter.CTkButton(master=self.support_frame, text="Brigitte", text_color="#000000", compound="top", image=brigitte_image, width=1,
                                                height=1, fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(brigitte))
        self.button31.grid(row=0, column=2, padx=3, pady=3)

        self.button32 = customtkinter.CTkButton(master=self.support_frame, text="Kiriko", text_color="#000000", compound="top", image=kiriko_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(kiriko))
        self.button32.grid(row=1, column=0, padx=3, pady=3)

        self.button33 = customtkinter.CTkButton(master=self.support_frame, text="Lucio", text_color="#000000", compound="top", image=lucio_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(lucio))
        self.button33.grid(row=1, column=1, padx=3, pady=3)

        self.button34 = customtkinter.CTkButton(master=self.support_frame, text="Mercy", text_color="#000000", compound="top", image=mercy_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(mercy))
        self.button34.grid(row=1, column=2, padx=3, pady=3)

        self.button34 = customtkinter.CTkButton(master=self.support_frame, text="Moira", text_color="#000000", compound="top", image=moira_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(moira))
        self.button34.grid(row=2, column=0, padx=3, pady=3)

        self.button34 = customtkinter.CTkButton(master=self.support_frame, text="Zenyatta", text_color="#000000", compound="top", image=zenyatta_image, width=1, height=1,
                                                fg_color="#fafafa", hover_color="#ed6516", command=lambda: self.randomizer(zenyatta))
        self.button34.grid(row=2, column=1, padx=3, pady=3)

    def randomizer(self, hero):
        self.clean()
        global text_label, text

        text = hero

        text = random.choice(hero)
        self.text_label.set(text)

    def clean(self):
        global text

        text = ""

        self.text_label.set("")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)




if __name__ == "__main__":
    app = App()
    app.mainloop()
