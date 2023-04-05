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

    with PIL.Image.open("../Testingfiles/Test8.png") as normalImage:
        normalImage.show()

    cipherBytes, byteMatrix, paddingValue = TranspositionEncrypt(
        rowLength, fileBytes)

    try:
        with open("EncryptedFile.png", "wb") as encryptedFile:
            encryptedFile.write(cipherBytes)

        with Image.open("EncryptedFile.png") as encryptedImage:
            encryptedImage.show()
    except PIL.UnidentifiedImageError:
        print("The file is encrypted and cannot be read properly.")

    plainBytes, byteMatrix = TranspositionDecrypt(byteMatrix, paddingValue)

    with open("DecryptedFile.png", "wb") as decryptedFile:
        decryptedFile.write(plainBytes)

    with Image.open("DecryptedFile.png") as decryptedImage:
        decryptedImage.show()
