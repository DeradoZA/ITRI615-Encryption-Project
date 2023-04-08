from PIL import Image
import PIL


def TranspositionEncrypt(rowLength, originalFile):
    byteMatrix = []
    Row = []
    cipherBytes = b""

    file = open(originalFile, "rb")

    fileBytes = file.read()

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


def CreateEncryptedFile(cipherBytes):
    encryptedFileName = "Encrypted.png"
    encryptedFile = open(encryptedFileName, "wb")
    encryptedFile.write(cipherBytes)

    encryptedFile.close()


def CreateDecryptedFile(plainBytes):
    decryptedFileName = "Decrypted.png"
    decryptedFile = open(decryptedFileName, "wb")
    decryptedFile.write(plainBytes)

    decryptedFile.close()


if __name__ == "__main__":
    originalFile = input("File name or path to file name:")

    rowLength = int(input("Input the row length you would like to use: "))

    cipherBytes, byteMatrix, paddingValue = TranspositionEncrypt(
        rowLength, originalFile)

    plainBytes, byteMatrix = TranspositionDecrypt(byteMatrix, paddingValue)

    CreateEncryptedFile(cipherBytes)
    CreateDecryptedFile(plainBytes)
