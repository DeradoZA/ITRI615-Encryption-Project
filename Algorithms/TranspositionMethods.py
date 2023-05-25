import os

class TranspositionMethods:
    def __init__(self, text = None, file = None):
        self.file = file
        self.text = text
        
        
    def TextEncrypt(self, text, rowLength):
        textMatrix = []
        Row = []
        cipherText = ""

        for character in text:
            Row.append(character)
            if len(Row) == rowLength:
                textMatrix.append(Row)
                Row = []
                
        if len(Row) == rowLength:
            textMatrix.append(Row)
        elif len(Row) == 0:
            pass
        else:
            paddingValue = rowLength - len(Row)
            for _ in range(paddingValue):
                Row.append(" ")
            textMatrix.append(Row)
            
        for index in range(rowLength):
            for row in textMatrix:
                cipherText += row[index]
                
        return cipherText
            
            
    def TextDecrypt(self, cipherText, rowLength):
        textMatrix = []
        Row = []
        plainText = ""

        for character in cipherText:
            Row.append(character)
            if len(Row) == len(cipherText) // rowLength + (1 if len(cipherText) % rowLength > 0 else 0):
                textMatrix.append(Row)
                Row = []

        for index in range(len(textMatrix[0])):
            for row in textMatrix:
                if index < len(row):
                    plainText += row[index]

        return plainText
        
        
    def FileEncrypt(self, fileBytes, rowLength):
        byteMatrix = []
        Row = []
        cipherBytes = b""

        for byte in fileBytes:
            Row.append(byte)
            if len(Row) == rowLength:
                byteMatrix.append(Row)
                Row = []
                
        if len(Row) == rowLength:
            byteMatrix.append(Row)
        elif len(Row) == 0:
            pass
        else:
            paddingValue = rowLength - len(Row)
            for _ in range(paddingValue):
                Row.append(0)
            byteMatrix.append(Row)
            
        for index in range(rowLength):
            for row in byteMatrix:
                cipherBytes += bytes([row[index]])
                
        return cipherBytes
    
    def FileDecrypt(self, cipherBytes, rowLength):
        byteMatrix = []
        Row = []
        plainBytes = b""

        for byte in cipherBytes:
            Row.append(byte)
            if len(Row) == len(cipherBytes) // rowLength + (1 if len(cipherBytes) % rowLength > 0 else 0):
                byteMatrix.append(Row)
                Row = []

        for index in range(len(byteMatrix[0])):
            for row in byteMatrix:
                if index < len(row):
                    plainBytes += bytes([row[index]])

        return plainBytes
    
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