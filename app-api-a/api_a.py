from flask import Flask, jsonify
from flask_restx import Api, Resource
import requests

API_B_URL = 'http://api-b:80'

app = Flask(__name__)
api = Api(app)

@api.route('/call-api-b')
class CallAPIB(Resource):
    def get(self):
        """Call API B and return its response"""
        response = requests.get(f'{API_B_URL}/hello')
        return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)