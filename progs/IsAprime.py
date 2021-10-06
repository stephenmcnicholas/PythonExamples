number = int(input("Is your number a prime?:"))

prime = True
half = number // 2

for i in range(2, half):
    if number%i==0:
        print(number, " is a multiple of ",i)
        print(number, " is NOT a prime")
        prime = False
        break
if prime:
    print(number, " is a prime")

    
