date = input("please input your DOB [as YYYYMMDD]: ")
lst = list(date)
while(len(lst)>1):
    digit = 0
    for i in range(len(lst)):
        digit += int(lst[i])
    lst = list(str(digit))
print(digit)