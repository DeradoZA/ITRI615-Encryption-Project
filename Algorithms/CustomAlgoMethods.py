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

    def FileEncrypt(self):
        pass

    def FileDecrypt(self):
        pass

    def CreateEncryptedFile(self):
        pass

    def CreateDecryptedFile(self):
        pass