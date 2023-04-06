import random
from PIL import Image
import PIL


def VernamEncrypt(plainFileBytes):
    plainTextLength = len(plainFileBytes)
    cipherBytes = b""
    vernamKeyBytes = b""

    for index in range(plainTextLength):
        keyByte = bytes([random.randint(0, 255)])
        plainFileByte = plainFileBytes[index]

        vernamKeyBytes = vernamKeyBytes + keyByte
        cipherBytes = cipherBytes + bytes([plainFileByte ^ keyByte[0]])

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


if __name__ == "__main__":

    file = open("../Testingfiles/Test8.png", "rb")

    fileBytes = file.read()

    cipherBytes, vernamKeyBytes = VernamEncrypt(fileBytes)

    decryptedBytes = VernamDecrypt(cipherBytes, vernamKeyBytes)
