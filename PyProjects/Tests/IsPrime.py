def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a positive integer: "))
if is_prime(number):
    print(number, "is prime.")
else:
    print(number, "is not prime.")