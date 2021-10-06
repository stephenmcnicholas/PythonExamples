# fibonacci: prints sequence of numbers up to (but not exceeding) limit input by user

num1 = 0
num2 = 1



limit = int(input("print all Fibonacci numbers lower than WHAT number?: "))

print(num1)
print(num2)
while (num1 + num2 <= limit):
    fib = num1 + num2
    print(fib)
    num1, num2 = num2, fib

print("end")
