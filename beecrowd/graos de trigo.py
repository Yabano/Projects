
def potencia(base,expoente):
    if expoente == 1:
        return base
    if expoente % 2:
        return base * potencia(base, expoente - 1)
    
    p = potencia(base, expoente//2)
    
    return p*p

def soma(a0,q,n):
    return a0 * (potencia(q,n-1) - 1) / (q - 1)

N = int(input())

for _ in range(N):
    X = int(input())
    
    print(f"{soma(1, 2, X)//12000:.0f} kg")