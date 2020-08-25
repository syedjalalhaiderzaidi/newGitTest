'''
#reading json file and coverting it into python dictionary
import json

print("Started Reading JSON file")
with open("developer.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    developer = json.load(read_file)

    print("Decoded JSON Data From File")
    for key, value in developer.items():
        print(key, ":", value)
    print("Done reading json file")

# reading json file and accessing values b keys:

import json

print("Started Reading JSON file")
with open("developer.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    developer = json.load(read_file)

    print("Decoding JSON Data From File")
    print("Printing JSON values using key")
    print(developer["name"])
    print(developer["salary"])
    print(developer["skills"])
    print(developer["email"])
    print("Done reading json file")
    

# reading json response from json string and converting it into python dictionary
import json

developerJsonString = """{
    "name": "jane doe",
    "salary": 9000,
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
"""

print("Started converting JSON string document to Python dictionary")
developerDict = json.loads(developerJsonString)
for key, value in developerDict.items():
        print(key, ":", value)
print("***************************************************")
print("Printing key and value by accessing keys :")
print(developerDict["name"])
print(developerDict["salary"])
print(developerDict["skills"])
print(developerDict["email"])
print(developerDict["projects"])

print("Done converting JSON string document to a dictionary")

#Parse and Retrieve nested JSON array key-values

import json

developerInfo = """{
    "id": 23,
    "name": "jane doe",
    "salary": 9000,
    "email": "JaneDoe@pynative.com",
    "experience": {"python":5, "data Science":2},
    "projectinfo": [{"id":100, "name":"Data Mining"}]
}
"""

developerDict= json.loads(developerInfo)

print("Project name: ", developerDict["projectinfo"][0]["name"]
print("experience: ", developerDict["experience"]["python"])


#Load JSON into an OrderedDict

import json
from collections import OrderedDict

print("Ordering keys")
OrderedData = json.loads('{"John":1, "Emma": 2, "Ault": 3, "Brian": 4}', object_pairs_hook=OrderedDict)
print("Type: ", type((OrderedData)))
print(OrderedData)



#How to use parse_float and parse_int kwarg in json.load()
import json

def roundFloats(salary):
    return round(float(salary), 2)

def salaryToDeduct(leaveDays):
    #salaryPerDay = 465
    return int(leaveDays) * salaryPerDay

print("Load float and int values from JSON and manipulate it")
print("Started Reading JSON file")

with open("developerDetails.json", "r") as read_file:
    developer = json.load(read_file, parse_float=roundFloats,
                          parse_int=salartToDeduct)


    # after parse_float
    print("Salary: ", developer["salary"])

    # after parse_int
    print("Salary to deduct: ", developer["leavedays"])
    print("Done reading a JSON file")

'''
# Import JSON module
import json

# Declare a python dictionary
customerDict = {'name': 'John', 'type': 'gold', 'age': 35 }

# Load the data from dictionary to JSON object
jsonData = json.dumps(customerDict)

# Print the JSON object
print(jsonData)


