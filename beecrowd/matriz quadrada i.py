
def min(a,b):
    if a < b:
        return a
    else:
        return b

while True:
    num = int(input())

    for i in range(num):
        
        print("1"*3)

        for j in range(num):
            
            print(f"{min(min(i, num - i  - 1),min(j, num - j - 1)) + 1}"*4)
        print()
    print()
