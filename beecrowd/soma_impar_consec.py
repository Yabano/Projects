num_casos = int(input())

for _ in range(num_casos):
    x,y = [int(x) for x in input().strip().split(' ')]
    
    conta = 0

    if x % 2 == 0: x+=1
        
    for i in range(y):
        conta += x
        x+=2
    print(conta)
