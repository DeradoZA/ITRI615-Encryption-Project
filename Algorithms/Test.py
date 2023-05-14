from VernamMethods import VernamMethods
from TranspositionMethods import TranspositionMethods
from CustomAlgoMethods import CustomAlgoMethods

cam = CustomAlgoMethods('lmao')

file = open('CMPG_311_DATACRAFTERS_PHASE2_DATABASE_DESIGN.pdf', "rb")
file_contents = file.read()

cipherBytes, rawEncsDecs, CustomKey = cam.FileEncrypt(file_contents)

plainBytes = cam.FileDecrypt(rawEncsDecs, CustomKey)

cam.createEncryptedFile(cipherBytes, 'CMPG_311_DATACRAFTERS_PHASE2_DATABASE_DESIGN.pdf')
cam.createDecryptedFile(plainBytes, 'CMPG_311_DATACRAFTERS_PHASE2_DATABASE_DESIGN.pdf')