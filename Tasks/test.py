#!/usr/bin/python3

def encrypt(txt, s):
    res = ""
    for i in range(len(txt)):
        char = txt[i]
        if (char.isupper()):
            res += chr((ord(char) + s - 65) % 26 + 65)
        elif (char.islower()):
            res += chr((ord(char) + s - 97) % 26 + 97)
        else:
            res += char
    print(res)


def decrypt(txt, s):
    res = ""
    for i in range(len(txt)):
        char = txt[i]
        if (char.isupper()):
            res += chr((ord(char) - s - 65) % 26 + 65)
        elif (char.islower()):
            res += chr((ord(char) - s - 97) % 26 + 97)
        else:
            res += char
    print(res)
 
if __name__ == '__main__':
    encrypt("Hello ,", 3)
    decrypt("khoor", 3)