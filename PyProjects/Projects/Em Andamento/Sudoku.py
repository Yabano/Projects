import random

COL = 3
ROW = 3
MATRIX = 3

def geraLista():
    for i in range(MATRIX):
        lista = []
        numList = [1,2,3,4,5,6,7,8,9]
        for i in range(COL):
            cols = []
            for i in range(ROW):
                rand = random.choice(numList)
                numList.remove(rand)
                cols.append(rand)
            lista.append(cols)
        printLista(lista)
    

def printLista(lista):
    for row in range(len(lista[0])):
        for i, cols in enumerate(lista):
            if i != len(lista) -1:
               print(cols[row], end =" | ")
            else:
               print(cols[row], end =" | ") 
        print()
    print("---------")   

geraLista()