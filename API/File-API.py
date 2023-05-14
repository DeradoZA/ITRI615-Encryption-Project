import os
import sys
from flask_cors import CORS
from flask_restful import Api, Resource
from flask import Flask, request, send_file, make_response, jsonify
import base64
from io import BytesIO

sys.path.append(os.path.join(os.path.dirname(__file__), '../Algorithms'))
from VernamMethods import VernamMethods as vm
from TranspositionMethods import TranspositionMethods as tm
from CustomAlgoMethods import CustomAlgoMethods as cam
from Vigenere import Vigenere as vig

app = Flask(__name__)
api = Api(app)

CORS(app)


class TextEncrypt(Resource):
    def get(self, text, encKey, encMethod):
        
        if (encMethod == "Vernam"):
            vernamEncryptor = vm(text)

            cipherText, vernamKey = vernamEncryptor.textEncrypt(text)

            return {"plaintext": text, "ciphertext": cipherText, "Vernam" : vernamKey}
        elif (encMethod == "Transposition"):
            encKeyValue = int(encKey)
            TranspositionEncryptor = tm(text)
            
            cipherText = TranspositionEncryptor.TextEncrypt(text, encKeyValue)
            
            return {"plaintext" : text, "ciphertext" : cipherText}
        
        elif(encMethod == "Custom"):
            CustomEncryptor = cam(text)
            cipherText, encryptedBytes, rawEncryptedDecs, customDecKey = CustomEncryptor.TextEncrypt(text)

            return {"plaintext" : text, "ciphertext" : cipherText, "rawEncryptedDecs" : rawEncryptedDecs, "CustomDecKey" : customDecKey}  
        
        elif(encMethod == "Vigenere"):
            VigenereEncryptor = vig()

            cipherText = vig.textEncrypt(text, encKey)

            return {"plaintext" : text, "ciphertext" : cipherText}
        
class TextDecrypt(Resource):
    def get(self, cipherText, encKey, encMethod):
        if (encMethod == "Vernam"):
            vernamDecryptor = vm(cipherText)

            plainText = vernamDecryptor.textDecrypt(cipherText, encKey)

            return {"ciphertext" : cipherText, "plaintext" : plainText}
        elif (encMethod == "Transposition"):
            encKeyValue = int(encKey)
            TranspositionDecryptor = tm(cipherText)
            plainText = TranspositionDecryptor.TextDecrypt(cipherText, encKeyValue)
            
            return {"ciphertext" : cipherText, "plaintext" : plainText}
        elif (encMethod == "Vigenere"):
            VigenereDecryptor = vig()
            plainText = vig.textDecrypt(cipherText, encKey)

            return {"ciphertext" : cipherText, "plaintext" : plainText}
            
class TextCustomDecrypt(Resource):
    def get(self, cipherText, encKey, rawEncDecs):
        
        encKeyValues = encKey.split(",")
        rawEncDecValues = rawEncDecs.split(",")
        encKeyValues = [int(i) for i in encKeyValues]
        rawEncDecValues = [int(i) for i in rawEncDecValues]
        CustomDecryptor = cam(cipherText)
        plainText = CustomDecryptor.TextDecrypt(rawEncDecValues, encKeyValues)
        
        return {"ciphertext" : cipherText, "plaintext" : plainText}
    
class FileEncrypt(Resource):
    def post(self):
        file = request.files['file']
        file_contents = file.read()
        file_name = file.filename
        encKey = request.form.get('encryptionkey')
        encMethod = request.form.get('encryptionMethod')

        if encMethod == 'Vernam':
            vernamEncryptor = vm(file_contents)
            cipherBytes, vernamKey = vernamEncryptor.fileEncrypt(file_contents)
            vernamKeyDecoded = ''

            vernamKey_b64 = base64.b64encode(vernamKey).decode('utf-8')

            vernamKey_bytes = base64.b64decode(vernamKey_b64)


            encryptedFileData = BytesIO()
            encryptedFileData.write(cipherBytes)
            encryptedFileData.seek(0)

            fileInfo = os.path.splitext(file_name)
            encryptedFileName = fileInfo[0] + " - E" + fileInfo[1]

            response_data = {
                'file': {
                    'data': base64.b64encode(encryptedFileData.getvalue()).decode('utf-8'),
                    'name': encryptedFileName,
                    'mime_type': 'application/octet-stream'
                },
                'vernam': vernamKey_b64
            }

            return jsonify(response_data)
        
        if encMethod == 'Transposition':
            transEncryptor = tm(file_contents)
            cipherBytes = transEncryptor.FileEncrypt(file_contents, int(encKey))

            encryptedFileData = BytesIO()
            encryptedFileData.write(cipherBytes)
            encryptedFileData.seek(0)

            fileInfo = os.path.splitext(file_name)
            encryptedFileName = fileInfo[0] + " - E" + fileInfo[1]

            response_data = {
                'file': {
                    'data': base64.b64encode(encryptedFileData.getvalue()).decode('utf-8'),
                    'name': encryptedFileName,
                    'mime_type': 'application/octet-stream'
                }
            }

            return jsonify(response_data)

        if encMethod == 'Vigenere':
            pass

        if encMethod == 'Custom':
            customEncryptor = cam(file_contents)
            cipherBytes, rawEncDecs, CustomKey = customEncryptor.FileEncrypt(file_contents)

            encryptedFileData = BytesIO()
            encryptedFileData.write(cipherBytes)
            encryptedFileData.seek(0)

            fileInfo = os.path.splitext(file_name)
            encryptedFileName = fileInfo[0] + " - E" + fileInfo[1]


            response_data = {
                'file': {
                    'data': base64.b64encode(encryptedFileData.getvalue()).decode('utf-8'),
                    'name': encryptedFileName,
                    'mime_type': 'application/octet-stream'
                },
                'rawEncDecs' : rawEncDecs,
                'CustomKey' : CustomKey
            }

            return jsonify(response_data)
        
class FileDecrypt(Resource):
    def post(self):
        file = request.files['file']
        file_contents = file.read()
        file_name = file.filename
        encKey = request.form.get('encryptionkey')
        encMethod = request.form.get('encryptionMethod')
        vernamKey = request.form.get('vernamKey')
        rawEncDecs = request.form.get('rawEncDecs')
        customDecKey = request.form.get('customDecKey')


        if encMethod == 'Vernam':
            vernamDecryptor = vm(file_contents)
            vernamKey_bytes = base64.b64decode(vernamKey)
            plainBytes = vernamDecryptor.fileDecrypt(file_contents, vernamKey_bytes)

            decryptedFileData = BytesIO()
            decryptedFileData.write(plainBytes)
            decryptedFileData.seek(0)

            fileInfo = os.path.splitext(file_name)
            decryptedFileName = fileInfo[0] + " - D" + fileInfo[1]

            response_data = {
                'file': {
                    'data': base64.b64encode(decryptedFileData.getvalue()).decode('utf-8'),
                    'name': decryptedFileName,
                    'mime_type': 'application/octet-stream'
                },
            }

            return jsonify(response_data)
        
        if encMethod == 'Transposition':
            transDecryptor = tm(file_contents)
            plainBytes = transDecryptor.FileDecrypt(file_contents, int(encKey))

            decryptedFileData = BytesIO()
            decryptedFileData.write(plainBytes)
            decryptedFileData.seek(0)

            fileInfo = os.path.splitext(file_name)
            decryptedFileName = fileInfo[0] + " - D" + fileInfo[1]

            response_data = {
                'file': {
                    'data': base64.b64encode(decryptedFileData.getvalue()).decode('utf-8'),
                    'name': decryptedFileName,
                    'mime_type': 'application/octet-stream'
                }
            }

            return jsonify(response_data)

        if encMethod == 'Vigenere':
            pass

        if encMethod == 'Custom':
            encKeyValues = customDecKey.split(",")
            rawEncDecValues = rawEncDecs.split(",")
            encKeyValues = [int(i) for i in encKeyValues]
            rawEncDecValues = [int(i) for i in rawEncDecValues]

            customDecryptor = cam(file_contents)
            plainBytes = customDecryptor.FileDecrypt(rawEncDecValues, encKeyValues)

            decryptedFileData = BytesIO()
            decryptedFileData.write(plainBytes)
            decryptedFileData.seek(0)

            fileInfo = os.path.splitext(file_name)
            decryptedFileName = fileInfo[0] + " - D" + fileInfo[1]

            response_data = {
                'file': {
                    'data': base64.b64encode(decryptedFileData.getvalue()).decode('utf-8'),
                    'name': decryptedFileName,
                    'mime_type': 'application/octet-stream'
                }
            }

            return jsonify(response_data)
        
api.add_resource(TextEncrypt, "/TextEncrypt/<string:text>/<string:encKey>/<string:encMethod>")
api.add_resource(TextDecrypt, "/TextDecrypt/<string:cipherText>/<string:encKey>/<string:encMethod>")
api.add_resource(TextCustomDecrypt, "/TextCustomDecrypt/<string:cipherText>/<string:encKey>/<string:rawEncDecs>")
api.add_resource(FileEncrypt, "/EncryptFileUpload")
api.add_resource(FileDecrypt, "/DecryptFileUpload")

if __name__ == "__main__":
    app.run(debug=True)

