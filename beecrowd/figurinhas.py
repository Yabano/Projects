def MDC(a, b):
    if b == 0:
        return a
    else:
        return MDC(b, a % b)

nCasos = int(input())

for _ in range(nCasos):
    fig1,fig2 = map(int, input().split())
    print(MDC(fig1,fig2))