from PIL import Image
import PIL


def TranspositionEncrypt(rowLength, fileBytes):
    byteMatrix = []
    Row = []
    cipherBytes = b""

    for byte in fileBytes:
        if len(Row) == rowLength:
            byteMatrix.append(Row)
            Row = []

        Row.append(bytes([byte]))

    if Row:
        if len(Row) < rowLength:
            paddingValue = rowLength - len(Row)
            for filler in range(paddingValue):
                Row.append(b" ")

            byteMatrix.append(Row)

    for index in range(rowLength):
        for row in byteMatrix:
            cipherBytes += row[index]

    return cipherBytes, byteMatrix, paddingValue


def TranspositionDecrypt(byteMatrix, paddingValue):
    plainBytes = b""

    letterMatrixFinalRow = len(byteMatrix)

    for _ in range(paddingValue):
        byteMatrix[-1].pop()

    for row in byteMatrix:
        for byte in row:
            plainBytes = plainBytes + byte

    return plainBytes, byteMatrix


if __name__ == "__main__":
    file = open("../Testingfiles/Test8.png", "rb")

    fileBytes = file.read()

    rowLength = int(input("Input the row length you would like to use: "))

    cipherBytes, byteMatrix, paddingValue = TranspositionEncrypt(
        rowLength, fileBytes)

    plainBytes, byteMatrix = TranspositionDecrypt(byteMatrix, paddingValue)
