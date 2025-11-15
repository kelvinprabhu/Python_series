import json
person = {
    "name": "John",
    "age": 30,
    "children": ["Anna", "Ella"],
    "city": "New York",
}
# print(type(person)) -- <class 'dict'>
# Convert Python object to JSON string
person_json = json.dumps(person,indent=4)

# print(type(person_json)) -- <class 'str'>
# Convert JSON string back to Python object

person_dict = json.loads(person_json)
# print(person_dict)

sorted_person = json.dumps(person_dict, indent=4, sort_keys=True)
# print(sorted_person)
# saving json to a file
with open("p.json", "w")as f:
    json.dump(person, f, indent=4)
# reading json from a file
with open("p.json", "r") as f: # read mode - default mode
    data = json.load(f)
# print(data)
# class type of data
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = student("Alice", 22)
print(student1.__dict__)
def encode_student(obj):
    if isinstance(obj, student):
        return {"name": obj.name, "age": obj.age, "class": "student"}
    else:
        raise TypeError("Object of type student expected")
student_json = json.dumps(student1, default=encode_student, indent=4)


from json import JSONEncoder
  