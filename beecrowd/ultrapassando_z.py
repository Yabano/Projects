x1 = int(input())
x2 = int(input())
conta = 0

while x2 <= x1:
    x2 = int(input())

conta += x1
contador = 1

while conta < x2:
    conta+= (x1+1)
    x1+=1
    contador+=1

print(contador)
