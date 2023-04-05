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

    with Image.open("../Testingfiles/Test8.png") as normalImage:
        normalImage.show()

    cipherBytes, vernamKeyBytes = VernamEncrypt(fileBytes)

    try:
        with open("EncryptedFile.png", "wb") as encryptedFile:
            encryptedFile.write(cipherBytes)

        with Image.open("EncryptedFile.png") as encryptedImage:
            encryptedImage.show()
    except PIL.UnidentifiedImageError:
        print("The file is encrypted and cannot be read properly.")

    decryptedBytes = VernamDecrypt(cipherBytes, vernamKeyBytes)

    with open("DecryptedFile.png", "wb") as decryptedFile:
        decryptedFile.write(decryptedBytes)

    with Image.open("DecryptedFile.png") as decryptedImage:
        decryptedImage.show()
