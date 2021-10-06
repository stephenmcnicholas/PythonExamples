# fibonacci sequence: prints first N fibonacci numbers, where N is specified by user

count = int(input("How many numbers in the sequence do you want: "))
num1 = 0
num2 = 1
print(num1)
print(num2)

for i in range(0, count-2):
    fibnum = num1 + num2
    num1, num2 = num2, fibnum
    print(fibnum)

print("end")
