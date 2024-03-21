from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/home')
class HomePage(Resource):
    def get(self):
        return "This is the home page"


if __name__ == "__main__":
    app.run()
