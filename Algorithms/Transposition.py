if __name__ == "__main__":
    plainText = input(
        "Input the plaintext you would like to encrypt using transposition cipher: ")

    rowLength = int(input("Input the row length you would like to use: "))

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

    print(letterMatrix)
    print(cipherText)
