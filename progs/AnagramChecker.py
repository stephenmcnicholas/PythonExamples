str1 = input("enter a word: ")
str2 = input("enter another word: ")

lst1 = sorted(list(str1.upper()))
lst2 = sorted(list(str2.upper()))

ana = True


if(len(lst1)!=len(lst2)):
    ana = False
    print("different length words can't be anagrams")
if(len(lst1)==0):
    ana = False
    print("empty strings can't be anagrams")
else: 
    for i in range(len(lst1)):
        if(lst1[i]!=lst2[i]):
            ana = False
            break
if(ana):
    print("These words ARE anagrams")
else: 
    print("These words are NOT anagrams")