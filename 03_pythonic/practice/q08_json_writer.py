import json

data = {
    "student": "Rajnish",
    "marks": 95
}

with open("student.json", "w") as file:
    json.dump(data, file)

print("JSON written successfully.")