import random

widowmaker = [
    "COTE D'AZUR",
    "PALE SERPENT",
    "ANGE DE LA MORT",
    "CYBERDEVIL",
    "MEDUSA",
    "WINTER",
    "ROSE"

]

cassidy = [
    "MYSTERY MAN",
    "INVISBLE MAN",
    "SPACE RAIDER",
    "FOREST RANGER"

]

ashe = [
    "POOLSIDE",
    "WARLOCK",
    "SOCIALITE"

]

pharah = [
    "SECURITY CHIEF",
    "HADES",
    "SKY CENTURION"

]

soldier = [
    "STRIKE COMMANDER MORRISON",
    "BUG HERO",
    "SPACE RAIDER",
    "VENOM"

]



def random_skin():
#escolher personagem
    print("escolha um personagem: widowmaker , cassidy, ashe, phara, soldier")
    escolha = input()

#escolher skin
    if escolha == "widowmaker" or escolha == "widow":
        skin = random.choice(widowmaker)
        print("sua skin é: "+skin)

    if escolha == "cassidy" or escolha == "cass":
       skin = random.choice(cassidy)
       print("sua skin é: " +skin)

    if escolha == "ashe":
       skin = random.choice(ashe)
       print("sua skin é: " +skin)

    if escolha == "phara":
       skin = random.choice(pharah)
       print("sua skin é: " +skin)

    if escolha == "soldier" or escolha == "sold":
       skin = random.choice(soldier)
       print("sua skin é: " +skin)




random_skin()