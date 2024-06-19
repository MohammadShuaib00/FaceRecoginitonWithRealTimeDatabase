import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://realfacedetectionsystem-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

# Data to be added to the database
data = {
    "321654": {
        "name": "Mohammad Hassan",
        "major": "Robotics",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2024-05-30 00:54:34"
    },
    "335696": {
        "name": "Mohammad Shuaib",
        "major": "Web Developer",
        "starting_year": 2020,
        "total_attendance": 1,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2024-05-30 00:54:34"
    },
    "852741": {
        "name": "Emly Blunt",
        "major": "Economics",
        "starting_year": 2020,
        "total_attendance": 1,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2024-05-30 00:54:34"
    },
    "963852": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2020,
        "total_attendance": 1,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2024-05-30 00:54:34"
    },
    "787878": {
        "name": "Umar Sir",
        "major": "HOD",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year":2,
        "last_attendance_time": "2024-05-30 00:54:34"
    },
    "969696": {
        "name": "Viaan Sharma",
        "major": "Web Developer",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year":2,
        "last_attendance_time": "2024-05-30 00:54:34"
    },
    "123456": {
        "name": "Abhay Singh",
        "major": "Software Engineer",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year":2,
        "last_attendance_time": "2024-05-30 00:54:34"
    },
    "212121": {
        "name": "Shadab Alam",
        "major": "Cyber Security",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year":2,
        "last_attendance_time": "2024-05-30 00:54:34"
    },
    "858585": {
        "name": "Shakir",
        "major": "Sell man",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year":2,
        "last_attendance_time": "2024-05-30 00:54:34"
    }
}

# Adding data to the database
for key, value in data.items():
    ref.child(key).set(value)
