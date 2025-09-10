#Definde alphabet
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Æ', 'Ø', 'Å'
]

#Define key and convert to numbers
key = 'sukkertoppen'
keyLength = len(key)
decryptKey = []
for i in key:
    decryptKey.append(alphabet.index((i)))

#Ask for message and convert to numbers
msg = input("Enter message: ")
msgNumber = []
for i in msg:
    msgNumber.append(alphabet.index(i))


def Encrypt():
    encryptedMsg = []
    for i in range(len(msgNumber)):
        encryptedMsg.append((msgNumber[i] + decryptKey[i % keyLength]) % len(alphabet))
    return encryptedMsg

#Debug prints
print(msgNumber)
print(keyLength)
print(decryptKey)
print(Encrypt())