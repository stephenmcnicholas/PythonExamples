#fib

proceed = False
while(not proceed):
    digits = input("Type how many digits in the Fibonacci sequence you would like to see: ")
    if(not digits.isdigit()):
        print("Please enter a positive integer")
    else:
        digits = int(digits)
        if(digits>100):
            print("Choose a number 100 or less")
        else:
            proceed = True



print("There are the first ", digits, " numbers in the Fibonacci sequence: ")

fibs = [0,1]

for i in range(digits-2):
    latest = fibs[-1] + fibs[-2]
    fibs.append(latest)
for i in range(len(fibs)):
    print(fibs[i],end=',')
