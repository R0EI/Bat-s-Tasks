# from flask import Flask, request, jsonify
# from flask_pymongo import PyMongo
from pymongo import MongoClient
# from bson.objectid import ObjectId
# import socket
#import pymongo

client = MongoClient(host='mongodb://root:password@localhost:27017/tasks',
                         port=27017,
                         username='root',
                         password='password',
                         authSource='admin')
# client = MongoClient("mongodb://@localhost:27017/tasks")

db = client["tasks"]
mycol = db["all_tasks"]

x = mycol.insert_one({
        "id": 3.0,
        "task": "Working"
    })

msg =""
for x in mycol.find():
    msg+=f"{x}\n"
print(msg)
# exit