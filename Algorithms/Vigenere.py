class Vigenere:
    def fileToBytes(file):
        readFile = open(file, 'rb')
        file_bytes = readFile.read()
        readFile.close()

        return file_bytes

    '''
    def bytesToFile(file):
        writeFile = open(file, 'wb')
        encryptedFile =  writeFile.write('')
        return encryptedFile
    '''

    def vigenere(
        plaintext,
        key,
        letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+/*[]{}\\|;:\'\",./<>? ',
        encrypt=True
    ):

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

    def encrypt(plaintext, key):
        return Vigenere.vigenere(plaintext=plaintext,
                        key=key,
                        encrypt=True)

    def decrypt(plaintext, key):
        return Vigenere.vigenere(plaintext=plaintext,
                        key=key,
                        encrypt=False)


def main():
    choice = 0
    plaintext = ''
    key = ''
    choice = int(input('Would you like to encrypt a file (1) or text (2)?: '))
    vig = Vigenere()
    
    if choice == 1:
        file = input('Enter name of file to encrypt: ')
        plaintext = str(vig.fileToBytes(file))
        key = input('Enter a key for the plaintext: ')

    if choice == 2:
        plaintext = input('Enter plaintext: ')
        key = input('Enter a key for the plaintext: ')

    ciphertext = vig.encrypt(plaintext, key)

    print('\nEncryption:\n', ciphertext)
    print('\nDecryption:\n', vig.decrypt(ciphertext, key))


if __name__ == '__main__':
    main()
