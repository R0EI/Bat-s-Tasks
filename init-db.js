db = db.getSiblingDB("tasks");
db.all_tasks.drop()

db.all_tasks.insertMany([
    {
        "id": 1,
        "task": "Working"
    },
    {
        "id": 2,
        "task": "Sleeping"
    }
]);