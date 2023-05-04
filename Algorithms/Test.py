from VernamMethods import VernamMethods as vm

VernamAlgo = vm("Hello World")

cipherText, vernamKey = VernamAlgo.textEncrypt(VernamAlgo.text)

print(cipherText + '\n' + vernamKey)

plainText = VernamAlgo.textDecrypt(cipherText, vernamKey)

print(plainText)