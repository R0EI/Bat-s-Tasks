from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient

from bson.objectid import ObjectId
import socket

client = MongoClient(host='localhost',
                         port=27017,
                         user='root',
                         password='password',
                         authSource='admin')
db = client["tasks"]
mycol = db["all_tasks"]

for x in mycol.find():
    print(x)