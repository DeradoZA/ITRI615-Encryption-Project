import os
import sys
from flask_cors import CORS
from flask_restful import Api, Resource
from flask import Flask, Response
from urllib.parse import unquote_plus
import json
import urllib.parse

sys.path.append(os.path.join(os.path.dirname(__file__), '../Algorithms'))
from VernamMethods import VernamMethods as vm
from TranspositionMethods import TranspositionMethods as tm
from CustomAlgoMethods import CustomAlgoMethods as cam

app = Flask(__name__)
api = Api(app)

CORS(app)


class TextEncrypt(Resource):
    def get(self, text, encKey, encMethod):
        text = unquote_plus(text)
        encKey = unquote_plus(encKey)
        encMethod = unquote_plus(encMethod)

        if encMethod == "Vernam":
            vernamEncryptor = vm(text)

            cipherText, vernamKey = vernamEncryptor.textEncrypt(text)

            response = {"plaintext": text, "ciphertext": cipherText, "Vernam": vernamKey}

            return Response(json.dumps(response, ensure_ascii=False), content_type="application/json; charset=utf-8")
        elif encMethod == "Transposition":
            encKeyValue = int(encKey)
            TranspositionEncryptor = tm(encKeyValue, text)

            cipherText, textMatrix, paddingValue = TranspositionEncryptor.TextEncrypt(text, encKeyValue)

            return {"plaintext": text, "ciphertext": cipherText}

        elif encMethod == "Custom":
            CustomEncryptor = cam(text)
            cipherText, encryptedBytes, rawEncryptedDecs, customDecKey = cam.TextEncrypt(text)

            return {"plaintext": text, "ciphertext": cipherText}

class TextDecrypt(Resource):
    def get(self, cipherText, encKey, encMethod):
        cipherText = unquote_plus(cipherText)
        encKey = unquote_plus(encKey)
        encMethod = unquote_plus(encMethod)

        if encMethod == "Vernam":

            cipherText = urllib.parse.unquote(cipherText)
            encKey = urllib.parse.unquote(encKey)
            vernamDecryptor = vm(cipherText)

            plainText = vernamDecryptor.textDecrypt(cipherText, encKey)

            return {"ciphertext": cipherText, "plaintext": plainText}


api.add_resource(
    TextEncrypt, "/TextEncrypt/<path:text>/<path:encKey>/<path:encMethod>")

api.add_resource(TextDecrypt, "/TextDecrypt/<path:cipherText>/<path:encKey>/<path:encMethod>")

if __name__ == "__main__":
    app.run(debug=True)