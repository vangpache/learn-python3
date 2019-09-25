from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


users = [
    {
        "name": "Nicolas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doc"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class User(Resource):
#def get
        def get(self, name):
            for user in users:
                if(name == user["name"]):
                    return user, 200
            return "User not found", 404
# def post(self, name):
        def post(self, name):
            parser = reqparse.RequestParser()
            parser.add_argument("age")
            parser.add_argument("occupation")
            args = parser.parse_args()

            for user in users:
                    if(name == user["name"]):
                        return "User with name {} already exists".format(name), 400

            user = {
                "name": name,
                "age": args["age"],
                "occupation": args["occupation"]
            }
            users.append(user)
            return user, 201
        # def post(self, name):

        # def put(self, name):

        # def delete(self, name):

api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
