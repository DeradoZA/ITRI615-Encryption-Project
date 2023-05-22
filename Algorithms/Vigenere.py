import os
import base64

class Vigenere:
    def __init__(self):
        self.letters = bytes(range(256))

    def vigenere(self, plaintext, key, encrypt=True):
        ciphertext = bytearray()

        for i in range(len(plaintext)):
            letter_index = self.letters.index(plaintext[i])
            key_index = self.letters.index(key[i % len(key)])

            if encrypt:
                plaintext_value = (letter_index + key_index) % len(self.letters)
            if not encrypt:
                plaintext_value = (letter_index - key_index) % len(self.letters)

            ciphertext.append(self.letters[plaintext_value])

        return bytes(ciphertext)
    
    def textEncrypt(self, plaintext, key):
        plaintext_bytes = plaintext.encode('utf-8') 
        key_bytes = key.encode('utf-8')
        cipher_bytes = self.vigenere(plaintext_bytes, key_bytes, True)
    
        return base64.b64encode(cipher_bytes).decode('utf-8')

    def textDecrypt(self, ciphertext, key):
        key_bytes = key.encode('utf-8')
        
        ciphertext_bytes = base64.b64decode(ciphertext.encode('utf-8'))
        plain_bytes = self.vigenere(ciphertext_bytes, key_bytes, False)
        return plain_bytes.decode('utf-8')

    def createEncryptedFile(self, file, key):
        fileInfo = os.path.splitext(file)
        newFileName = fileInfo[0] + 'Encrypted' + fileInfo[1]
        key_bytes = key.encode()

        readFile = open(file, 'rb')
        file_bytes = readFile.read()
        readFile.close()

        cipher_bytes = self.vigenere(file_bytes, key_bytes, True)

        newFile = open(newFileName, 'wb')
        newFile.write(cipher_bytes)
        newFile.close()

    def createDecryptedFile(self, file, key):
        fileInfo = os.path.splitext(file)
        newFileName = fileInfo[0] + 'Decrypted' + fileInfo[1]
        key_bytes = key.encode()

        readFile = open(file, 'rb')
        file_bytes = readFile.read()
        readFile.close()

        plain_bytes = self.vigenere(file_bytes, key_bytes, False)

        newFile = open(newFileName, 'wb')
        newFile.write(plain_bytes)
        newFile.close()
        
def main():
    vig = Vigenere()

    # Test on text
    print("Text encryption/decryption")
    plaintext = "Hello, World!"
    key = "lock"
    
    encrypted_text = vig.textEncrypt(plaintext, key)
    print("Encrypted Text:", encrypted_text)
    decrypted_text = vig.textDecrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)

    # Test on file
    print("File encryption/decryption")
    file = 'Test3.pptx'

    file_name, file_extension = os.path.splitext(file)

    encrypted_file_name = file_name + "Encrypted" + file_extension

    vig.createEncryptedFile(file, key)
    vig.createDecryptedFile(encrypted_file_name, key)

if __name__ == "__main__":
    main()
