word = list(input("Enter a word: ").lower())
text = input("Enter a long string to search for the word: ").lower()
hidden = True
pos = 0
for letter in word:
    pos = text.find(letter, pos)
    if(pos==-1):
        hidden = False
        print(letter, "not found")
        hidden = False
        break

if(hidden):
    print("Yes")
else: 
    print("No")


    

