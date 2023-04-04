import random

def VernamEncrypt(plainText):
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

    return cipherText, vernamKey

def VernamDecrypt(cipherText, vernamKey):
    plainTextLength = len(cipherText)
    decryptedText = ""
    
    for index in range(plainTextLength):
        cipherTextASCIIValue = ord(cipherText[index])
        vernamKeyTextASCIIValue = ord(vernamKey[index])

        decryptedASCIIValue = cipherTextASCIIValue ^ vernamKeyTextASCIIValue

        decryptedText = decryptedText + chr(decryptedASCIIValue)
        
    return decryptedText

if __name__ == "__main__":
    plainText = input(
        "Input the plaintext you would like to encrypt with vernam cipher: ")
    
    cipherText, vernamKey = VernamEncrypt(plainText)
    
    print(cipherText)
    
    decryptedText = VernamDecrypt(cipherText, vernamKey)
    
    print(decryptedText)


    
