import random
import os
import base64


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
        cipherBytes = b""
        vernamKeyBytes = b""

        for byte in fileBytes:
            keyByteValue = random.randint(0, 255)
            keyByte = bytes([keyByteValue])

            vernamKeyBytes = vernamKeyBytes + keyByte
            cipherBytes = cipherBytes + bytes([byte ^ keyByteValue])

        return cipherBytes, vernamKeyBytes

    def fileDecrypt(self, fileBytes, vernamKey):
    
        decryptedBytes = b""

        print(len(fileBytes))

        for byte, vernamByte in zip(fileBytes, vernamKey):

            decryptedByte = byte ^ vernamByte

            decryptedBytes = decryptedBytes + bytes([decryptedByte])

        return decryptedBytes

    def createEncryptedFile(self, cipherBytes, file):
        fileInfo = os.path.splitext(file)
        encryptedFileName = fileInfo[0] + " - E" + fileInfo[1]
        encryptedFile = open(encryptedFileName, "wb")
        encryptedFile.write(cipherBytes)

        encryptedFile.close()

    def createDecryptedFile(self, plainBytes, file):
        fileInfo = os.path.splitext(file)
        decryptedFileName = fileInfo[0] + " - D" + fileInfo[1]
        decryptedFile = open(decryptedFileName, "wb")
        decryptedFile.write(plainBytes)

        decryptedFile.close()
