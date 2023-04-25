import random
import os

def VernamEncrypt(fileName):

    file = open(fileName, "rb")

    plainFileBytes = file.read()

    plainTextLength = len(plainFileBytes)
    cipherBytes = b""
    vernamKeyBytes = b""

    for index in range(plainTextLength):
        keyByte = bytes([random.randint(0, 255)])
        plainFileByte = plainFileBytes[index]

        vernamKeyBytes = vernamKeyBytes + keyByte
        cipherBytes = cipherBytes + bytes([plainFileByte ^ keyByte[0]])

    file.close()
    return cipherBytes, vernamKeyBytes


def VernamDecrypt(cipherText, vernamKey):
    cipherTextLength = len(cipherText)
    decryptedBytes = b""

    for index in range(cipherTextLength):
        cipherByte = cipherText[index]
        vernamKeyByte = vernamKey[index]

        decryptedByte = cipherByte ^ vernamKeyByte

        decryptedBytes = decryptedBytes + bytes([decryptedByte])

    return decryptedBytes


def CreateEncryptedFile(cipherBytes, originalFile):
    
    fileInfo = os.path.splitext(originalFile)
    encryptedFileName = "Encrypted" + fileInfo[1]
    encryptedFile = open(encryptedFileName, "wb")
    encryptedFile.write(cipherBytes)

    encryptedFile.close()


def CreateDecryptedFile(plainBytes, originalFile):
    
    fileInfo = os.path.splitext(originalFile)
    decryptedFileName = "Decrypted" + fileInfo[1]
    decryptedFile = open(decryptedFileName, "wb")
    decryptedFile.write(plainBytes)

    decryptedFile.close()


if __name__ == "__main__":

    originalFile = input("File name or path to file name:")

    cipherBytes, vernamKeyBytes = VernamEncrypt(originalFile)

    decryptedBytes = VernamDecrypt(cipherBytes, vernamKeyBytes)

    CreateEncryptedFile(cipherBytes, originalFile)
    CreateDecryptedFile(decryptedBytes, originalFile)
