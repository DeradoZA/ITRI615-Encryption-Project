def vigenere(
        plaintext,
        key,
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ',
        encrypt = True
    ):

    ciphertext = ''

    for i in range(len(plaintext)):
        letter_index = letters.index(plaintext[i])
        key_index = letters.index(key[i % len(key)])

        if encrypt:
            plaintext_value = (letter_index + key_index) % len(letters)
        
        if not encrypt:
            plaintext_value = (letter_index - key_index) % len(letters)

        ciphertext += letters[plaintext_value]

    return ciphertext

def vig_encrypt(plaintext, key):
    return vigenere(plaintext=plaintext, key=key, encrypt = True)

def vig_decrypt(plaintext, key):
    return vigenere(plaintext=plaintext, key=key, encrypt = False)

def main():
    plaintext = str(input('Enter any plaintext: '))
    key =  str(input('Enter a key for the plaintext: '))

    ciphertext = vig_encrypt(plaintext, key)
    
    print(ciphertext)
    print(vig_decrypt(ciphertext, key))

main()
    