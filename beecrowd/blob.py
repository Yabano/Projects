import math

num = int(input())

for x in range(num):
    f = float(input())
    
    print(f"{math.ceil(math.log2(f))} dias")