def imprime(string,lista,numero):
    for x in range(numero):
        print(f"{string}[{x}] = {lista[x]}")

lista_impar = []
lista_par = []

for x in range(15):
    valor = int(input())

    if valor % 2 == 0:  
        lista_par.append(valor)
        if len(lista_par) == 5:
            imprime("par",lista_par,len(lista_par))
            lista_par.clear()
    else:  
        lista_impar.append(valor)
        if len(lista_impar) == 5:
            imprime("impar",lista_impar,len(lista_impar))
            lista_impar.clear()

imprime("impar",lista_impar,len(lista_impar))
imprime("par",lista_par,len(lista_par))