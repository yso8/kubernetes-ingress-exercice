from flask import Flask, jsonify
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

hello_response = api.model('HelloResponse', {
    'message': fields.String(required=True, description='The greeting message')
})

@api.route('/hello')
class HelloWorld(Resource):
    @api.marshal_with(hello_response)
    def get(self):
        """Return a simple greeting message"""
        return {'message': 'Hello from API B'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)