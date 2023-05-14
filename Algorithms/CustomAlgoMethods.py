import os
import random

class CustomAlgoMethods:
    def __init__(self, text=None, file=None):
        self.text = text
        self.file = file

    def TextEncrypt(self, text):
        customDecKey = []
        rawEncryptedDecs = []
        encryptedBytes = b""
        textToBytes = text.encode('ascii')

        for byte in textToBytes:
            randomKeyDec = random.randint(1, 256)
            customDecKey.append(randomKeyDec)

            encryptedRawDecimalValue = byte * randomKeyDec
            encryptedDecimalValue = encryptedRawDecimalValue % 128
            encryptedByteValue = encryptedDecimalValue.to_bytes(1, byteorder='big')
            rawEncryptedDecs.append(encryptedRawDecimalValue)

            encryptedBytes += encryptedByteValue

        cipherText = encryptedBytes.decode('ascii')

        return cipherText, encryptedBytes, rawEncryptedDecs, customDecKey

    def TextDecrypt(self, encryptedRawDecs, customDecKey):
        decryptedBytes = b""

        for index in range(0, len(encryptedRawDecs)):
            decryptedByteDec = int(encryptedRawDecs[index] / customDecKey[index])
            decryptedBytes += decryptedByteDec.to_bytes(1, byteorder='big')

        plainText = decryptedBytes.decode('ascii')

        return plainText

    def FileEncrypt(self, fileBytes):

        customDecKey = []
        rawEncryptedDecs = []
        cipherBytes = b""

        for byte in fileBytes:
            randomKeyDec = random.randint(1, 256)
            customDecKey.append(randomKeyDec)

            encryptedRawDecimalValue = byte * randomKeyDec
            encryptedDecimalValue = encryptedRawDecimalValue % 256
            encryptedByteValue = encryptedDecimalValue.to_bytes(1, byteorder='big')
            rawEncryptedDecs.append(encryptedRawDecimalValue)

            cipherBytes += encryptedByteValue
        
        return cipherBytes, rawEncryptedDecs, customDecKey

    def FileDecrypt(self, rawEncryptedDecs, customKey):
        decryptedBytes = b""

        for index in range(0, len(rawEncryptedDecs)):
            decryptedByteDec = int(rawEncryptedDecs[index] / customKey[index])
            decryptedBytes += decryptedByteDec.to_bytes(1, byteorder='big')

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