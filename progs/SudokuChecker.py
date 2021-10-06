row = ' '
lst = []
valid = True
while(len(row)>0):
    #print(lst)
    row = input("Enter a row of nine digitsm then ENTER (or just ENTER to finish): ")
    if(row.isdigit()):
        lst.append(row)

if(len(lst)<9):
    valid = False
else:
    for elem in lst:
        for i in range(1,10):
            if(elem.find(str(i))==-1):
                valid = False
                break
if(valid):
    print("valid sudoku")
else:
    print("Invalid sudoku")