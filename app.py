from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from random import choice
import socket
import json

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
    html_indexing = "&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;"
    msg = ""
    for task in tasks:
        temp_id = str(task["_id"])
        temp_task = task["task"]
        temp_until = task["until"]
        temp_lvl = task["urgency_lvl"]
        if temp_lvl=='A':
            msg+=f"{html_indexing}<b style='color:red;'>ID: {temp_id}</b><br>{html_indexing}Task: {temp_task}<br>{html_indexing}Expiration: {temp_until}<br><br><br>"
        elif temp_lvl=='B':
            msg+=f"{html_indexing}<b style='color:#FFC300;'>ID: {temp_id}</b><br>{html_indexing}Task: {temp_task}<br>{html_indexing}Expiration: {temp_until}<br><br><br>"
        else:
            msg+=f"{html_indexing}<b style='color:green;'>ID: {temp_id}</b><br>{html_indexing}Task: {temp_task}<br>{html_indexing}Expiration: {temp_until}<br><br><br>"
    return msg

@app.route("/task", methods=["POST"])
def create_task():
    db = get_db()
    mycol = db["all_tasks"]
    task=request.form["task"]
    until=request.form["until"]
    urgency_lvl=request.form["urgency_lvl"]
    mycol.insert_one({  "task": task,
                        "until": until,
                        "urgency_lvl": urgency_lvl})
    return redirect(url_for("get_all_tasks"))
    

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

@app.route("/sorted_tasks")
def sorted_tasks():
    db = get_db()
    mycol = db["all_tasks"]
    tasks = mycol.find()
    html_indexing = "&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;"
    msg = ""
    msgB=""
    msgC=""
    for task in tasks:
        temp_id = str(task["_id"])
        temp_task = task["task"]
        temp_until = task["until"]
        temp_lvl = task["urgency_lvl"]
        if temp_lvl=='A':
            msg+=f"{html_indexing}<b style='color:red;'>ID: {temp_id}</b><br>{html_indexing}Task: {temp_task}<br>{html_indexing}Expiration: {temp_until}<br><br><br>"
        elif temp_lvl=='B':
            msgB+=f"{html_indexing}<b style='color:#FFC300;'>ID: {temp_id}</b><br>{html_indexing}Task: {temp_task}<br>{html_indexing}Expiration: {temp_until}<br><br><br>"
        else:
            msgC+=f"{html_indexing}<b style='color:green;'>ID: {temp_id}</b><br>{html_indexing}Task: {temp_task}<br>{html_indexing}Expiration: {temp_until}<br><br><br>"  
    msg= msg + msgB + msgC
    return msg

@app.route("/id_for_testing")
def id_for_testing():  
    db = get_db()   
    mycol = db["all_tasks"]
    result = list(mycol.find({}, {"_id": 1}))
    random_id = choice(result)["_id"]
    return str(random_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)





