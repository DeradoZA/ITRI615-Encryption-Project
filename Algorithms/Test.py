from VernamMethods import VernamMethods as vm

userInput = input("plaintext: ")

VernamAlgo = vm(userInput)

cipherTextBytes, vernamKeyBytes = VernamAlgo.textEncrypt(VernamAlgo.text)

plainText = VernamAlgo.textDecrypt(cipherTextBytes, vernamKeyBytes)

print("Decrypted Text: " + plainText)