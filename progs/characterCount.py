mydict = {}
myfile = input("enter file name to be read :")
try:
    poem = open(myfile, 'rt')
    for line in poem:
        #line.lower()
        for elem in line.lower():
            if elem in mydict.keys():
                mydict[elem] +=1
            else:
                mydict[elem] = 1
    poem.close()
except IOError as e:
    print("I/O error :", str(e.errno), ", ", e)

#sorteddict = sorted(mydict.items(), key=lambda n: [1], reverse=True)

for k, v in sorted(mydict.items(), key=lambda n: n[1], reverse=True):
    if k.isalpha():
        print(k, " -> ", v)
