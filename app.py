from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import socket

app = Flask(__name__)

def get_db():
    client = MongoClient(host='mongodb://root:password@mymongodb:27017/tasks',
                         port=27017,
                         username='root',
                         password='password',
                         authSource='admin')
    db = client["tasks"]
    return db


@app.route("/")
def index():  
    return render_template("index.html")
  


@app.route("/tasks")
def get_all_tasks():
    db = get_db()
    mycol = db["all_tasks"]
    tasks = mycol.find()
    msg = ""

    for task in tasks:
        item = {
            "id": str(task["_id"]),
            "task": task["task"],
            "Expiration": task["until"]
        }
        msg += f"{item}"
    return jsonify(
        tasks=msg
    )


@app.route("/task", methods=["POST"])
def create_task():
    db = get_db()
    mycol = db["all_tasks"]
    
    tasks = mycol.find()
    s=0
    for task in tasks:
        s+=1
    s+=1

    data = request.get_json(force=True)
    mycol.insert_one({"id":str(s),
                        "task": data["task"],
                        "until": data["until"]})
    return jsonify(
        message="Task saved successfully!"
    )


@app.route("/task/<id>", methods=["PUT"])
def update_task(id):
    db = get_db()
    mycol = db["all_tasks"]
    data = request.get_json(force=True)["task"]
    response = mycol.update_one({"_id": ObjectId(id)}, {"$set": {"task": data}})
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
    mycol = db["all_tasks"]
    response = mycol.delete_one({"_id": ObjectId(id)})
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
    mycol = db["all_tasks"]
    mycol.delete_all_tasks
   
    return jsonify(
        message="All Tasks deleted!"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)





