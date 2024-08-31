
import math

#First line of code
#print("hello world")

#Variables
#first_name = "joao"
#last_name = "bastos"
#print(first_name +" "+ last_name)
#print(type(last_name))

#age = 23
#age += 1
#print("your age is: "+str(age))
#print(type(age))

#height = 250.5
#print("your height is: "+str(height)+"cm")
#print(type(height))

#human = True
#print("are you a human: "+str(human))
#print(type(human))

#Multiple Assignments

#name, age, attraticve = "marquin", 19, False

#print(name)
#print(age)
#print(attraticve)

#Tio_Patinhas = 30
#Bruninho = 30
#Junin_Menor = 30

#could be done as

#Tio_Patinhas = Bruninho = Junin_Menor = 30

#print(Tio_Patinhas)
#print(Junin_Menor)
#print(Bruninho)

#Useful String Methods

#name = "marcos"

#print(len(name))  Retuns the length of the string
#print(name.find("a"))  Will fing the first index of the character you choose (it'll start counting from 0, not 1)
#print(name.capitalize())  Will capitalize the first letter of the string, won't capitalize the first letter after spaces
#print(name.upper())  Will change all letters of the string to upper cases
#print(name.lower())  Will change all letters of the string to lower cases
#print(name.isdigit())  Will return true or false if it's a digit or not
#print(name.isalpha())  It verifies if the string is only aplhabetical letters, if there is a space/number, it'll return false
#print(name.count("o"))  Will count the number of times the character is displayed
#print(name.replace("a","o"))  Will change all (a) letters with (o)
#print(name*3)  Will display (*) times the string

#Type Casting

#x = 1 #int
#y = 2.0 #float
#z = "3" #str

#x = str(x)
#y = str(y)
#z = str(z)

#print(x)
#print(y)
#print(z*3)

#x = int(x)
#y = int(y)
#z = int(z)

#print(x)
#print(y)
#print(z*3)

#x = float(x)
#y = float(y)
#z = float(z)

#print(x)
#print(y)
#print(z*3)

#User input

#name = input("what's your name?: ")
#age = int(input("how old are you?: "))

#age = age+1

#print(name)
#print("you are "+str(age)+" years old")

#LET HIM COOK

#pp= 920.4

#x= 1
#y= 2
#z= 3

#print(round(pp))
#print(math.ceil(pp))
#print(math.floor(pp))
#print(abs(pp))
#print(max(x,y,z))
#print(min(x,y,z))

#FATIA OS CARA

#slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

#name = "marcos mantoani"

#irst_name = name[:6]
#rint(first_name)
#ast_name = name[7:]
#print(last_name)
#reversed_name = name[5::-1].replace("m","M")
#print(reversed_name)
#funky_name = name[::2]
#print(funky_name)


#slice = slice(7,-4)

#website1 = "http://google.com"
#website2 = "http:/wikipedia.com"

#print(website1[slice])
#print(website2[slice])

#If Statemants = a block of code that will execute if it's condition is true

#age = int(input("how old are you?"))

#if age >= 18:
#    print("you are an adult!")
#elif age < 0:
#    print("you're not born yet!")




