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
        
        
        
    
    def FileEncrypt(self):
        pass
    
    def FileDecrypt(self):
        pass
    
    def CreateEncryptFile(self):
        pass
    
    def CreateDecryptFile(self):
        pass