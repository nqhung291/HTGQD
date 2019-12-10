import datetime
from flask import Flask, Response
from flask_cors import CORS
from flask.json import JSONEncoder
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


class MongoEngineJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return JSONEncoder.default(self, o)


class JsonResponse(Response):
    default_mimetype = 'application/json'


# create the flask app
app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = 'mongodb://root:pass123@ds253418.mlab.com:53418/htgqd?retryWrites=false'
mongo = PyMongo(app)
app.json_decoder = MongoEngineJSONEncoder
app.response_class = JsonResponse
from app.controller import *
