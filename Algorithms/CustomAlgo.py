import random
import os
import decimal


def CustomEncrypt(fileName):
    file = open(fileName, "rb")

    plainFileBytes = file.read()

    customDecKey = []
    encryptedBytes = b""

    for byte in plainFileBytes:
        vernamRandom = random.randint(0, 255)
        customDecKey.append(vernamRandom)

        encryptedDecimalValue = (byte ** vernamRandom) % 256
        encryptedByteValue = encryptedDecimalValue.to_bytes(1, byteorder='big')

        encryptedBytes += encryptedByteValue

    return encryptedBytes, customDecKey


def CustomDecrypt(encryptedBytes, customKey):
    decryptedBytes = b""

    for byte in encryptedBytes:
        pass


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

    originalFile = input("File name or path that you would like to encrypt: ")

    encryptedBytes, customKey = CustomEncrypt(originalFile)

    print(encryptedBytes)

    CreateEncryptedFile(encryptedBytes, originalFile)
