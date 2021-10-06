mynumber = int(input("what's your number? "))

print("All the prime numbers up to ", mynumber, " are: ")



def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(2,mynumber):
    if is_prime(num):
        print(num)


