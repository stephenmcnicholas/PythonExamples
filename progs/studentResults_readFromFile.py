#studentFileData

# An exception for an empty file.
class FileEmpty(Exception):
    def __init__(self):
        super().__init__(self)

mydict = {}
file = input("please input file name to process: ")

try:
    results = open(file, 'rt')
    lines = results.readlines()
    results.close()
    if len(lines) == 0:
        raise FileEmpty()
    for line in lines:
        fname, sname, score = line.split(" ")
        name = fname+" "+sname
        score = float(score)
        if name in mydict.keys():
            mydict[name] += score
        else:
            mydict[name] = score
    results.close()
    
except IOError as e:
    print("I/O error :", str(e.errno), ", ", e)
except FileEmpty:
    print("source file empty")

fo = open("scores.txt", 'wt')

for name, score in mydict.items():
    line = name + "\t" + str(score) + "\n"
    fo.write(line)
fo.close()
        
    


                
            

