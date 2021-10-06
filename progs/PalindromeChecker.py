text = input("enter your word: ")
text = list(text.replace(" ", "").upper())


palindrome = True
for i in range(len(text) // 2):
    if(text[i]==text[-(i+1)]):
        continue
    else:
        palindrome = False
if(palindrome):
    print("It's a palindrome")
else:
    print("It's NOT a palindrome")