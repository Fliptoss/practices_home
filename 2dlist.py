students = [
    {"name": "Hermionie", "house": "Gryffindor", "patronus":"otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus":"stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus":"Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},  
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=', ')