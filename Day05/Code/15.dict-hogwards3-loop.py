students = [
    {"name": "Hermione", "house": "Gryffindor", "petronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "petronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "petronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "petronus": None}
]
#none - special keyword that represents absence of value
for student in students:
    print(student["name"], student["house"], student["petronus"], sep=", ")
