import json

data = {
    "name": "Rajnish",
    "course": "Python"
}

# Write JSON
with open("data.json", "w") as file:
    json.dump(data, file)

# Read JSON
with open("data.json", "r") as file:
    content = json.load(file)

print(content)