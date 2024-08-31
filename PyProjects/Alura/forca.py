import secrets
import string

string = string.ascii_letters + string.digits

pwd = secrets.choice(string)
numero = int(input("numero de letras"))

whi