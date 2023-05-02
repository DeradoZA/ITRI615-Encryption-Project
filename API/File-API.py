import os
import sys
from flask_cors import CORS
from flask_restful import Api, Resource
from flask import Flask

sys.path.append(os.path.join(os.path.dirname(__file__), '../Algorithms'))
from VernamMethods import VernamMethods as vm
from TranspositionMethods import TranspositionMethods as tm

app = Flask(__name__)
api = Api(app)

CORS(app)


class TextEncrypt(Resource):
    def get(self, text, encKey, encMethod):
        
        if (encMethod == "Vernam"):
            vernamEncryptor = vm(text)

            cipherText, vernamKey = vernamEncryptor.textEncrypt(text)

            return {"plaintext": text, "ciphertext": cipherText}
        elif (encMethod == "Transposition"):
            encKeyValue = int(encKey)
            TranspositionEncryptor = tm(encKeyValue,text)
            
            cipherText, textMatrix, paddingValue = TranspositionEncryptor.TextEncrypt(text, encKeyValue)
            
            return {"plaintext" : text, "ciphertext" : cipherText}


api.add_resource(
    TextEncrypt, "/TextEncrypt/<string:text>/<string:encKey>/<string:encMethod>")

if __name__ == "__main__":
    app.run(debug=True)
