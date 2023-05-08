from CustomAlgoMethods import CustomAlgoMethods as cam

text = input("text: ")

customDec = cam(text)

cipherText, encryptedBytes, rawEncryptedDecs, customDecKey = customDec.TextEncrypt(text)

plainText = customDec.TextDecrypt(rawEncryptedDecs, customDecKey)

print(cipherText)
print("Decrypting")

print(plainText)