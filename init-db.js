db = db.getSiblingDB("tasks");
db.all_tasks.drop()

db.all_tasks.insertMany([
    {
        "task": "Working Out",
        "until": "25/06/23",
        "urgency_lvl": "A"
    },
    {
        "task": "Reading",
        "until": "10/02/23",
        "urgency_lvl": "B"
    },
    {
        "task": "Meditation",
        "until": "24/01/23",
        "urgency_lvl": "C"
    }
]);