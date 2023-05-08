from TranspositionMethods import TranspositionMethods as tm

text = input("text: ")
rowLength = int(input("row length: "))

transDec = tm(text)

cipherText, textMatrix = transDec.TextEncrypt(text, rowLength)

print(cipherText)
print(textMatrix)
print("Decrypting")

plainText = transDec.TextDecrypt(cipherText, rowLength)

print(plainText)