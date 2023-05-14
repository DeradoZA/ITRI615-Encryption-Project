import os

class Vigenere:
    def vigenere(
        plaintext,
        key,
        encrypt=True
    ):

        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+/*[]{}\\|;:\'\",./<>? '
        ciphertext = ''
        plaintext_value = 0

        for i in range(len(plaintext)):
            letter_index = letters.index(plaintext[i])
            key_index = letters.index(key[i % len(key)])

            if encrypt:
                plaintext_value = (letter_index + key_index) % len(letters)

            if not encrypt:
                plaintext_value = (letter_index - key_index) % len(letters)

            ciphertext += letters[plaintext_value]

        return ciphertext

    def textEncrypt(plaintext, key):
        return Vigenere.vigenere(plaintext, key, True)

    def textDecrypt(plaintext, key):
        return Vigenere.vigenere(plaintext, key, False)

    def fileToBytes(file):
        readFile = open(file, 'rb')
        file_bytes = readFile.read()
        readFile.close()
    
        return file_bytes

    def fileEncrypt(plaintext, key):
        ciphertext = Vigenere.vigenere(plaintext, key, True)
        return ciphertext

    def fileDecrypt(ciphertext, key):
        return Vigenere.vigenere(ciphertext, key, False)
    
    def createEncryptedFile(ciphertext, file):
        fileInfo = os.path.splitext(file)
        encryptedFileName = "Encrypted" + fileInfo[1]
        encryptedFile = open(encryptedFileName, "wb")
        encryptedFile.write(bytes(ciphertext, 'utf-8'))

        encryptedFile.close()

    def createDecryptedFile(plainBytes, file):
        fileInfo = os.path.splitext(file)
        decryptedFileName = fileInfo[0] + " - D" + fileInfo[1]
        decryptedFile = open(decryptedFileName, "wb")
        decryptedFile.write(plainBytes)

        decryptedFile.close()

        