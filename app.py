from flask import Flask
from flask_restful import Resource, Api
from views import Questions, StartView


app1 = Flask(__name__)
api = Api(app1)


api.add_resource(StartView, '/')
api.add_resource(Questions, '/questions')

if __name__ == '__main__':
    app1.run()
