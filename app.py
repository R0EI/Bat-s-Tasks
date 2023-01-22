from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import socket

app = Flask(__name__)

def get_db():
    client = MongoClient(host='mongodbhost',
                         port=27017,
                         user='root',
                         password='password',
                         authSource='admin')
    db = client["tasks"]
    return db


@app.route("/")
def index():  
    db = get_db()
    mycol = db["all_tasks"]

    message=""
    for x in mycol.find():
        message += f"{x}\n"
    
    return jsonify(
        message
    )


@app.route("/tasks")
def get_all_tasks():
    db = get_db()
    tasks = db.task.find()
    data = []
    for task in tasks:
        item = {
            "id": str(task["_id"]),
            "task": task["task"]
        }
        data.append(item)
    return jsonify(
        data=data
    )


@app.route("/task", methods=["POST"])
def create_task():
    db = get_db()
    data = request.get_json(force=True)
    db.task.insert_one({"task": data["task"]})
    return jsonify(
        message="Task saved successfully!"
    )


@app.route("/task/<id>", methods=["PUT"])
def update_task(id):
    db = get_db()
    data = request.get_json(force=True)["task"]
    response = db.task.update_one({"_id": ObjectId(id)}, {"$set": {"task": data}})
    if response.matched_count:
        message = "Task updated successfully!"
    else:
        message = "No Task found!"
    return jsonify(
        message=message
    )


@app.route("/task/<id>", methods=["DELETE"])
def delete_task(id):
    db = get_db()
    response = db.task.delete_one({"_id": ObjectId(id)})
    if response.deleted_count:
        message = "Task deleted successfully!"
    else:
        message = "No Task found!"
    return jsonify(
        message=message
    )


@app.route("/tasks/delete", methods=["POST"])
def delete_all_tasks():
    db = get_db()
    db.task.remove()
    return jsonify(
        message="All Tasks deleted!"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)





