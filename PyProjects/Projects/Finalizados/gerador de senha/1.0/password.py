import secrets
import string

chars = string.ascii_letters + string.digits + string.punctuation

pwd = ""

letters = int(input("how many chars?"))

while letters >= 1:
    rand_char = secrets.choice(chars)
    pwd += rand_char
    letters -= 1

print(pwd)
