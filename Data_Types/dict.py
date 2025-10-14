person = {"name": "Alice", "age": 25, "city": "Chennai"}
person["email"] = "alice@example.com"
person["age"] = 26
print(person)

for i in person:
    print(f"{i}: {person[i]}")
print("----------")
students = {
    "Alice": {"age": 25, "city": "Chennai"},
    "Bob": {"age": 27, "city": "Mumbai"}
}

for student, details in students.items():
    print(student)
    for key, value in details.items():
        print("  ", key, ":", value)
