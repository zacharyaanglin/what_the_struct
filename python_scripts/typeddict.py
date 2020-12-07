from typing import TypedDict

class Student(TypedDict):
    name: str
    id: int
    age: int
    year: int

tommy = Student(name="tommy", id=12345, age=10, year=5)
print(tommy)
# {'name': 'tommy', 'id': 12345, 'age': 10, 'year': 5}

print(isinstance(tommy, dict))
# True
