texto = input()
conta = 0.0
contador = 0

for i in range(12):
    for j in range(12):
        val = float(input())
        if((j < 5) and ((i < 6 and j < i) or (i > 5 and j < 11 - i))):
            conta += val
            contador+=1

if(texto == 'S'):
     print(f"{conta:.1f}")
else:
     print(f"{conta/contador:.1f}")