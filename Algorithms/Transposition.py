def TranspositionEncrypt(rowLength, plainText):
    letterMatrix = []
    Row = []
    cipherText = ""

    for char in plainText:
        if len(Row) == rowLength:
            letterMatrix.append(Row)
            Row = []

        Row.append(char)

    if Row:
        if len(Row) < 4:
            lengthDiff = rowLength - len(Row)
            for filler in range(lengthDiff):
                Row.append(" ")

            letterMatrix.append(Row)

    for index in range(rowLength):
        for row in letterMatrix:
            cipherText = cipherText + row[index]
            
    return cipherText, letterMatrix, lengthDiff

def TranspositionDecrypt(letterMatrix, paddingValue, rowLength):
    plainText = ""

    letterMatrixFinalRow = len(letterMatrix)
    
    for _ in range(paddingValue):
        letterMatrix[-1].pop()
        
    for row in letterMatrix:
        for letter in row:
            plainText = plainText + letter
            
    return plainText, letterMatrix

if __name__ == "__main__":
    plainText = input(
        "Input the plaintext you would like to encrypt using transposition cipher: ")

    rowLength = int(input("Input the row length you would like to use: "))
    
    cipherText, letterMatrix, paddingValue = TranspositionEncrypt(rowLength, plainText)
    
    print("This is the encrypted text: " + cipherText)
    
    decryptedText, letterMatrix2 = TranspositionDecrypt(letterMatrix, paddingValue, rowLength)
    
    print("This is the decrypted text: " + decryptedText)

    
