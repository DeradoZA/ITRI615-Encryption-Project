import random

if __name__ == "__main__":
    plainText = input("Input the plaintext you would like to encrypt: ")

    plainTextLength = len(plainText)

    cipherText = ""
    vernamKey = ""

    for index in range(plainTextLength):
        keyRandomASCIIValue = random.randint(0, 255)
        keyChar = chr(keyRandomASCIIValue)
        plainTextASCIIValue = ord(plainText[index])

        cipherTextASCIIValue = plainTextASCIIValue ^ keyRandomASCIIValue

        vernamKey = vernamKey + keyChar
        cipherText = cipherText + chr(cipherTextASCIIValue)

    print(cipherText)
    decryptedText = ""

    for index in range(plainTextLength):
        cipherTextASCIIValue = ord(cipherText[index])
        vernamKeyTextASCIIValue = ord(vernamKey[index])

        decryptedASCIIValue = cipherTextASCIIValue ^ vernamKeyTextASCIIValue

        decryptedText = decryptedText + chr(decryptedASCIIValue)

    print(decryptedText)
