from flask import Flask
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', help='Specify your name')

@api.route('/home')
class HomePage(Resource):
    @api.doc(parser=parser)
    def get(self):
        args = parser.parse_args()
        name = args['name']
        return f"This is the home page, this is your name: {name}"


if __name__ == "__main__":
    app.run()
