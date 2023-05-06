import random
import os


class VernamMethods:
    def __init__(self, text=None, file=None):
        self.text = text
        self.file = file

    def textEncrypt(self, text):
        vernamKey = ""
        cipherText = ""
        
        for letter in text:
            keyByteValue = random.randint(0,255)
            keyChar = chr(keyByteValue)
            vernamKey = vernamKey + keyChar
            
            cipherText += chr(ord(letter) ^ keyByteValue)

        return cipherText, vernamKey

    def textDecrypt(self, text, vernamKey):
        decryptedText = ""
        
        for textLetter, vernamLetter in zip(text, vernamKey):
            decryptedByte = ord(textLetter) ^ ord(vernamLetter)

            decryptedText += chr(decryptedByte)

        return decryptedText

    def fileEncrypt(self, fileBytes):

        plainTextLength = len(fileBytes)
        cipherBytes = b""
        vernamKeyBytes = b""

        for index in range(plainTextLength):
            keyByte = bytes([random.randint(0, 255)])
            plainFileByte = fileBytes[index]

            vernamKeyBytes = vernamKeyBytes + keyByte
            cipherBytes = cipherBytes + bytes([plainFileByte ^ keyByte[index]])

        return cipherBytes, vernamKeyBytes

    def fileDecrypt(self, fileBytes, vernamKey):
        cipherTextLength = len(fileBytes)
        decryptedBytes = b""

        for index in range(cipherTextLength):
            cipherByte = fileBytes[index]
            vernamKeyByte = vernamKey[index]

            decryptedByte = cipherByte ^ vernamKeyByte

            decryptedBytes = decryptedBytes + bytes([decryptedByte])

        return decryptedBytes

    def createEncryptedFile(self, cipherBytes, file):
        fileInfo = os.path.splitext(file)
        encryptedFileName = "Encrypted" + fileInfo[1]
        encryptedFile = open(encryptedFileName, "wb")
        encryptedFile.write(cipherBytes)

        encryptedFile.close()

    def createDecryptedFile(self, plainBytes, file):
        fileInfo = os.path.splitext(file)
        decryptedFileName = "Decrypted" + fileInfo[1]
        decryptedFile = open(decryptedFileName, "wb")
        decryptedFile.write(plainBytes)

        decryptedFile.close()
