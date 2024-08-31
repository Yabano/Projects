import customtkinter

class Ct(customtkinter.CTkToplevel):
    def teste(self):
        self.title("teste1")
        self.geometry(f"{100}x{100}")
        Ct.mainloop() 

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("teste")
        self.geometry(f"{600}x{500}")

        self.testeframe = customtkinter.CTkFrame(master=self, bg_color="blue")
        self.testeframe.grid(row=0,column=0)

        self.button = customtkinter.CTkButton(master=self.testeframe, text="teste",command=Ct.teste())
        self.button.grid(row=0,column=0,)


if __name__ == "__main__":
    app = App()
    app.mainloop()