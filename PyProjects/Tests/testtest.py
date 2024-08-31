import string
import secrets


def generator(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    special = string.punctuation
    digits = string.digits

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_cryteria = False
    has_number = False
    has_special = False

    while not meets_cryteria or len(password) < min_length:
        new_char = secrets.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_cryteria = True
        if numbers:
            meets_cryteria = has_number
        if special_characters:
            meets_cryteria = meets_cryteria and has_special

    return password

min_lenght = int(input("len"))
has_number = input("num").lower() =="y"
has_spec = input("spec").lower()=="y"
pwd = generator(min_lenght, has_number, has_spec)
print(pwd)
