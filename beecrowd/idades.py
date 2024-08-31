lista = []

while True:
    inp = int(input())
    if inp > 0:
        lista.append(inp)
    else: break

conta = 0

for x in range(len(lista)):
    conta += lista[x]

print("{:.2f}".format(conta/len(lista)))