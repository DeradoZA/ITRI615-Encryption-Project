import os

class TranspositionMethods:
    def __init__(self, rowLength, text = None, file = None):
        self.rowLength = rowLength
        self.file = file
        self.text = text
        
        
    def TextEncrypt(self, text, rowLength):
        textMatrix = []
        Row = []
        cipherText = ""

        for character in text:
            if len(Row) == rowLength:
                textMatrix.append(Row)
                Row = []

            Row.append(character)

        if Row:
            if len(Row) < rowLength:
                paddingValue = rowLength - len(Row)
                for filler in range(paddingValue):
                    Row.append(" ")

                textMatrix.append(Row)

        for index in range(rowLength):
            for row in textMatrix:
                cipherText += row[index]

        return cipherText, textMatrix, paddingValue
    
    def TextDecrypt(self, textMatrix, paddingValue):
        plainText = ""

        letterMatrixFinalRow = len(textMatrix)

        for _ in range(paddingValue):
            textMatrix[-1].pop()

        for row in textMatrix:
            for character in row:
                plainBytes = plainBytes + character

        return plainBytes
    
    def FileEncrypt(self):
        pass
    
    def FileDecrypt(self):
        pass
    
    def CreateEncryptFile(self):
        pass
    
    def CreateDecryptFile(self):
        pass