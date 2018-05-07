student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

all_students = [
    {"name": "Mark", "student_id": 15163},
    {"name": "Katarina", "student_id": 63112},
    {"name": "Jessica", "student_id": 30021}
]

student["name"] == "Mark"
student["last_name"] == KeyError
student.get("last_name", "Unknown") == "Unknown"
student.keys() == ["name", "student_id", "feedback"]
student.values() == ["Mark", 15163, None]
student["name"] = "James"
del student["name"]