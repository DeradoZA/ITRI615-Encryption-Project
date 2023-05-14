from VernamMethods import VernamMethods
from TranspositionMethods import TranspositionMethods
from CustomAlgoMethods import CustomAlgoMethods
from Vigenere import Vigenere

file = open('CMPG_311_DATACRAFTERS_PHASE2_DATABASE_DESIGN.pdf', "rb")
file_contents = file.read()

encKey = input("Enter the key: ")

cipherBytes = Vigenere.fileEncrypt(file_contents, encKey)

plainBytes = Vigenere.fileDecrypt(cipherBytes, encKey)

Vigenere.createEncryptedFile(cipherBytes, 'CMPG_311_DATACRAFTERS_PHASE2_DATABASE_DESIGN.pdf')
Vigenere.createDecryptedFile(plainBytes, 'CMPG_311_DATACRAFTERS_PHASE2_DATABASE_DESIGN.pdf')