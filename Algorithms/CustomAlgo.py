import random
import os
import decimal


def CustomEncrypt(fileName):
    file = open(fileName, "rb")

    plainFileBytes = file.read()

    customDecKey = []
    encryptedBytes = b""

    for byte in plainFileBytes:
        randomKeyDec = random.randint(0, 255)
        customDecKey.append(randomKeyDec)

        encryptedDecimalValue = (byte ** randomKeyDec) % 256
        encryptedByteValue = encryptedDecimalValue.to_bytes(1, byteorder='big')

        encryptedBytes += encryptedByteValue

    file.close()
    return encryptedBytes, customDecKey


def CustomDecrypt(encryptedBytes, customKey):
    decryptedBytes = b""
    customKeyPointer = 0

    for byte in encryptedBytes:
        byteDecValue = int.from_bytes(byte, byteorder='big')
        for plainDec in range(256):
            if (plainDec ** customKey[customKeyPointer] % 256) == byte:
                decryptedBytes += plainDec.to_bytes(1, byteorder='big')
                break

        customKeyPointer += 1

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

    encryptedBytes, customKey = CustomEncrypt(originalFile)

    CreateEncryptedFile(encryptedBytes, originalFile)

    decryptedBytes = CustomDecrypt(encryptedBytes, customKey)

    CreateDecryptedFile(decryptedBytes, originalFile)
