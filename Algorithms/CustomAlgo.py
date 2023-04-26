import random
import os
import decimal


def CustomEncrypt(fileName):
    file = open(fileName, "rb")

    plainFileBytes = file.read()

    customDecKey = []
    rawEncryptedDecs = []
    encryptedBytes = b""

    for byte in plainFileBytes:
        randomKeyDec = random.randint(1, 256)
        customDecKey.append(randomKeyDec)

        encryptedRawDecimalValue = byte * randomKeyDec
        encryptedDecimalValue = encryptedRawDecimalValue % 256
        encryptedByteValue = encryptedDecimalValue.to_bytes(1, byteorder='big')
        rawEncryptedDecs.append(encryptedRawDecimalValue)

        encryptedBytes += encryptedByteValue

    file.close()
    return encryptedBytes, rawEncryptedDecs, customDecKey


def CustomDecrypt(encryptedRawDecimals, customKey):
    decryptedBytes = b""

    for index in range(0, len(encryptedRawDecimals)):
        decryptedByteDec = int(encryptedRawDecimals[index] / customKey[index])
        decryptedBytes += decryptedByteDec.to_bytes(1, byteorder='big')

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

    originalFile = input("File name or path that you would like to encrypt: ")

    encryptedBytes, rawEncryptedValues, customKey = CustomEncrypt(originalFile)

    CreateEncryptedFile(encryptedBytes, originalFile)

    decryptedBytes = CustomDecrypt(rawEncryptedValues, customKey)

    CreateDecryptedFile(decryptedBytes, originalFile)
