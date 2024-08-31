def fibo(num):
    lista_fibo = [0,1]
    
    for i in range(2, num):
        lista_fibo.append(lista_fibo[i-1] + lista_fibo[i-2])
    
    return lista_fibo[:num]

num_loop = int(input())
if 0 <num_loop < 46:
    fibo(num_loop)