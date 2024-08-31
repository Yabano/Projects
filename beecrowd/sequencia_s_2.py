y=1
conta = 0

for x in range(1,39,2):
    conta += x/y
    y*=2

print(f"{conta:.2f}")