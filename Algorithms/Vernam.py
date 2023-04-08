import random
from PIL import Image
import PIL


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


def CreateEncryptedFile(cipherBytes):
    encryptedFileName = "Encrypted.png"
    encryptedFile = open(encryptedFileName, "wb")
    encryptedFile.write(cipherBytes)

    encryptedFile.close()


def CreateDecryptedFile(plainBytes):
    decryptedFileName = "Decrypted.png"
    decryptedFile = open(decryptedFileName, "wb")
    decryptedFile.write(plainBytes)

    decryptedFile.close()


if __name__ == "__main__":

    originalFile = input("File name or path to file name:")

    cipherBytes, vernamKeyBytes = VernamEncrypt(originalFile)

    decryptedBytes = VernamDecrypt(cipherBytes, vernamKeyBytes)

    CreateEncryptedFile(cipherBytes)
    CreateDecryptedFile(decryptedBytes)
