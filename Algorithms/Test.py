from Vigenere import Vigenere as vig

text = input("text: ")
key = input("key: ")

cipherText = vig.textEncrypt(text, key)

plainText = vig.textDecrypt(text, key)

print(cipherText)
print("Decrypting")

print(plainText)