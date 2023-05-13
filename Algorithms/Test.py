from VernamMethods import VernamMethods

vm = VernamMethods('lmao')

file = open('CMPG_311_DATACRAFTERS_PHASE2_DATABASE_DESIGN.pdf', "rb")
file_contents = file.read()

cipherBytes, vernamKey = vm.fileEncrypt(file_contents)

plainBytes = vm.fileDecrypt(cipherBytes, vernamKey)

vm.createEncryptedFile(cipherBytes, 'CMPG_311_DATACRAFTERS_PHASE2_DATABASE_DESIGN.pdf')
vm.createDecryptedFile(plainBytes, 'CMPG_311_DATACRAFTERS_PHASE2_DATABASE_DESIGN.pdf')