from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

CORS(app)

class TextEncrypt(Resource):
    def get(self, text):
        return {"Output": text}
        
        
api.add_resource(TextEncrypt, "/TextEncrypt/<string:text>")    

if __name__ == "__main__":
    app.run(debug=True)