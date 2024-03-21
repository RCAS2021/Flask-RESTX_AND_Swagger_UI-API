from flask import Flask
from flask_restx import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', help='Specify your name')
upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage)

@api.route('/home/')
class HomePage(Resource):
    @api.doc(parser=parser)
    def get(self):
        args = parser.parse_args()
        name = args['name']
        return f"This is the home page, this is your name: {name}"

@api.route('/upload/')
@api.expect(upload_parser)
class UploadDemo(Resource):
    def post(self):
        args = upload_parser.parse_args()
        file = args.get('file')
        print(file.filename)
        return f"The uploaded file name is: {file.filename}"

if __name__ == "__main__":
    app.run()
