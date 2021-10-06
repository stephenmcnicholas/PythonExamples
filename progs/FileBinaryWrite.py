from os import strerror

#create binary stream to write data
somedata = bytearray(10)

for i in range(len(somedata)):
    somedata[i] = 10 + i

try:
    bf = open('file.bin', 'ab')
    bf.write(somedata)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# read data from binary stream
moredata = bytearray(10)
try:
    bf = open('file.bin', 'rb')
    bf.readinto(moredata)
    bf.close()

    for b in moredata:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
