db = db.getSiblingDB("tasks");
db.all_tasks.drop()

db.all_tasks.insertMany([
    {
        "id": 1,
        "task": "Working",
        "until": "25/06/23"
    },
    {
        "id": 2,
        "task": "Reading",
        "until": "10/02/23"
    }
]);