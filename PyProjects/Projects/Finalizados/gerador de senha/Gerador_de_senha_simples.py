import string
import customtkinter
import secrets


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        ver = Verify()
        gen = Generator()
        
        self.characters_bool_var = customtkinter.BooleanVar(value=True)
        self.lower_bool_var = customtkinter.BooleanVar(value=False)
        self.upper_bool_var = customtkinter.BooleanVar(value=False)
        self.symbol_bool_var = customtkinter.BooleanVar(value=False)
        self.digits_bool_var = customtkinter.BooleanVar(value=False)
        self.text_strvar = customtkinter.StringVar()
        self.convert_var = customtkinter.StringVar()

        self.title("Password Generator")
        self.geometry(f"{600}x{500}")

        self.grid_columnconfigure((0, 1), weight=0)
        self.grid_rowconfigure((1, 2), weight=0)
        self.grid_columnconfigure(2, weight=1)

        # frame/grid config for Checkboxes
        checkbox_frame = customtkinter.CTkFrame(master=self)
        checkbox_frame.grid(row=1, padx=30, pady=10, ipadx=40, ipady=10, sticky="w")

        grid_0 = customtkinter.CTkCheckBox(master=checkbox_frame, text="Characters", variable=self.characters_bool_var,onvalue=True,offvalue=False,
                                           command=lambda: ver.verify_characters())
        grid_0.grid(padx=10, pady=10, row=0)
        grid_1 = customtkinter.CTkCheckBox(master=checkbox_frame, text="Lower Case", variable=self.lower_bool_var,onvalue=True,offvalue=False,
                                           command=lambda: ver.verify_lower_checkbox())
        grid_1.grid(padx=10, pady=10, row=1)
        grid_2 = customtkinter.CTkCheckBox(master=checkbox_frame, text="Upper Case", variable=self.upper_bool_var,onvalue=True,offvalue=False,
                                           command=lambda: ver.verify_upper_checkbox())
        grid_2.grid(padx=10, pady=10, row=2)
        grid_3 = customtkinter.CTkCheckBox(master=checkbox_frame, text="Symbols", variable=self.symbol_bool_var,onvalue=True,offvalue=False,
                                           command=lambda: ver.verify_symbols_checkbox())
        grid_3.grid(padx=10, pady=10, row=3)
        grid_4 = customtkinter.CTkCheckBox(master=checkbox_frame, text="Numbers", variable=self.digits_bool_var,onvalue=True,offvalue=False,
                                           command=lambda: ver.verify_digits_checkbox())
        grid_4.grid(padx=10, pady=10, row=4)

        # frame/grid config for EntryBox
        entrybox_frame = customtkinter.CTkFrame(master=self)
        entrybox_frame.grid(row=2, padx=30, sticky="w")

        digits_entry = customtkinter.CTkEntry(master=entrybox_frame, textvariable=self.convert_var, placeholder_text="Password Length")
        digits_entry.grid(padx=10, pady=5, row=0, column=0, sticky="w")
    

        # password TextBox
        password_frame = customtkinter.CTkFrame(master=self, width=400, height=200)
        password_frame.grid(padx=100, pady=70, row=3, sticky="nsew")

        password_textbox = customtkinter.CTkEntry(master=password_frame, width=400, height=40,textvariable=self.text_strvar,state="disabled")
        password_textbox.grid(row=0)
        generate_button = customtkinter.CTkButton(password_frame,text="Generate Password", command=lambda: gen.generator())
        generate_button.grid(row=4, pady=10)
        

    def exception():
        password_excep = customtkinter.CTkLabel(app.password_frame, text="batata")
        password_excep.grid()



class Verify():
    def verify_characters(self):
        return app.characters_bool_var.get()

    def verify_lower_checkbox(self):
        return app.lower_bool_var.get()

    def verify_upper_checkbox(self):
        return app.upper_bool_var.get()

    def verify_digits_checkbox(self):
        return app.digits_bool_var.get()

    def verify_symbols_checkbox(self):
        return app.symbol_bool_var.get()
    
    def convert_digits(self):
        try:
            return int(app.convert_var.get()) 
        except(ValueError,TypeError):
              pass
            

class Generator():

    def generator(self):
        ver = Verify()

        characters = ""
        letters = string.ascii_letters
        special = string.punctuation
        digits = string.digits
        

        characters_bolvar = ver.verify_characters()
        lower_bolvar = ver.verify_lower_checkbox()
        upper_bolvar = ver.verify_upper_checkbox()
        symbols_bolvar = ver.verify_symbols_checkbox()
        digits_bolvar = ver.verify_digits_checkbox()
        
        if characters_bolvar:
            characters = letters
        if lower_bolvar:
            characters = characters.lower()
        if upper_bolvar:
            characters = characters.upper()
        if digits_bolvar:
            characters += digits
        if symbols_bolvar:
            characters += special

        pwd = ""
        letters = ver.convert_digits()

        try:
            while letters >= 1:
                rand_char = secrets.choice(characters)
                pwd += rand_char
                letters -= 1
        except (ValueError,TypeError):
            app.exception()
           
        
        app.text_strvar.set(pwd)


if __name__ == "__main__":
    app = App()
    app.mainloop()
