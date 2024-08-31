import customtkinter

class Checkbox:
    def __init__(self) -> None:
        self.var = customtkinter.BooleanVar()

    def get_checkbox_value(self):
        print(self.var.get())


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        chk = Checkbox()
        check_frame = customtkinter.CTkFrame(self)
        check_frame.pack()

        check_box = customtkinter.CTkCheckBox(master=check_frame, variable=chk.var)
        check_box.pack()

        submit = customtkinter.CTkButton(self, command=lambda: chk.get_checkbox_value())
        submit.pack()

    # Call the get_checkbox_value() function


if __name__ == "__main__":
    app = App()
    app.mainloop()

