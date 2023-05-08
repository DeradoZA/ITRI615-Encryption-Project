import os
import sys
from flask_cors import CORS
from flask_restful import Api, Resource
from flask import Flask

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
    def post(self, cipherText, encKey, rawEncDecs):
        
        encKeyValues = encKey.split(",")
        rawEncDecValues = rawEncDecs.split(",")
        encKeyValues = [int(i) for i in encKeyValues]
        rawEncDecValues = [int(i) for i in rawEncDecValues]
        CustomDecryptor = cam(cipherText)
        plainText = CustomDecryptor.TextDecrypt(rawEncDecValues, encKeyValues)
        
        return {"ciphertext" : cipherText, "plaintext" : plainText}
    
class FileDecrypt(Resource):
    def get(self, file, encKey, encMethod):
        pass

api.add_resource(TextEncrypt, "/TextEncrypt/<string:text>/<string:encKey>/<string:encMethod>")
api.add_resource(TextDecrypt, "/TextDecrypt/<string:cipherText>/<string:encKey>/<string:encMethod>")
api.add_resource(TextCustomDecrypt, "/TextCustomDecrypt/<string:cipherText>/<string:encKey>/<string:rawEncDecs>")
api.add_resource(FileDecrypt, "/EncryptedFileUpload")

if __name__ == "__main__":
    app.run(debug=True)
