def fatorar(num):
    conta = num
    
    for x in range(1,num):
        conta *= x
    print(conta)


teste = int(input())

fatorar(teste)