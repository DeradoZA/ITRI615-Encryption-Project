from VernamMethods import VernamMethods
from TranspositionMethods import TranspositionMethods
from CustomAlgoMethods import CustomAlgoMethods
from Vigenere import Vigenere
import base64

file = open('CMPG_311_DATACRAFTERS_PHASE2_DATABASE_DESIGN.pdf', "rb")
file_contents = file.read()
file_decoded_contents = base64.b64encode(file_contents).decode('utf-8')

encKey = input("Enter the key: ")

cipherBytes = Vigenere.fileEncrypt(file_decoded_contents, encKey)

cipherBytes_encoded = cipherBytes.encode('utf-8')
plainBytes = Vigenere.fileDecrypt(cipherBytes, encKey)
plainBytes_encoded = plainBytes.encode('utf-8')

Vigenere.createEncryptedFile(cipherBytes_encoded, 'CMPG_311_DATACRAFTERS_PHASE2_DATABASE_DESIGN.pdf')
Vigenere.createDecryptedFile(plainBytes_encoded, 'CMPG_311_DATACRAFTERS_PHASE2_DATABASE_DESIGN.pdf')