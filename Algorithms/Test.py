from VernamMethods import VernamMethods as vm

text = "Hello World"

VernamAlgo = vm(text)

cipherText, vernamKey = VernamAlgo.textEncrypt(text)

print("cipher text: " + cipherText + '\n' + "vernam key: " + vernamKey)

plainText = VernamAlgo.textDecrypt(cipherText, vernamKey)

print("plain text: " + plainText)