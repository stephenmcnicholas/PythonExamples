# Caesar cipher.
text = input("Enter your message: ")
shift = int(input("How many characters do you want to shift? "))
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    if char.isupper():
        code = ord(char) + shift
        if code > ord('Z'):
            code = ord(char)+shift-26
    if char.islower():
        code = ord(char) + shift
        if code > ord('z'):
            code = ord(char)+shift-26
    cipher += chr(code)

print(cipher)
