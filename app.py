import base64
import os
from flask import Flask, request, jsonify, session, send_from_directory, send_file
from flask_cors import CORS
from flask_pymongo import PyMongo
import uuid
import jwt
import datetime
import random
from decimal import Decimal
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app, origins="http://localhost:*", supports_credentials=True)
app.config["MONGO_URI"] = "mongodb://localhost:27017/challegecup"
SECRET_KEY = "your_secret_key_here"
mongo = PyMongo(app)


@app.route('/swiper/img/<filename>', methods=['GET'])
def img(filename):
    return send_from_directory('./swiper', filename)


@app.route('/swiper', methods=['GET'])
def swiper():
    result = os.listdir('./swiper')
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
