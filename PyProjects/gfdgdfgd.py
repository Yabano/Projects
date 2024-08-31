numbers = [int(numbers) for numbers in input().split()]

while True:
    if numbers[1] <= 0:
        numbers.pop(1)
    else: break

a = numbers[0]
n = numbers[1]

def soma_consecutiva(num):
    soma = 0
    for i in range(0, num):
        soma += (a+i)
    return soma

print(soma_consecutiva(n))