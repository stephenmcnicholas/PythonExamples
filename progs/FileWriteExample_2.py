from os import strerror

try:
    fo = open('C:/Users/stephen.mcnicholas/py/files/newtext2.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
