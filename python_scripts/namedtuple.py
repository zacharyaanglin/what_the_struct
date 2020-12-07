from collections import namedtuple

Name = namedtuple("Name", "first last")
me = Name("Zach", "Anglin")
me_tuple = ("Zach", "Anglin")

# print(me == me_tuple)
# # True


from collections import namedtuple

Name = namedtuple("Name", "first last middle", defaults=["X"])
me = Name("Zach", "Anglin")

print(me)
# Name(first='Zach', last='Anglin', middle='X')


from collections import namedtuple

Student = namedtuple("Student", "name id age year", defaults=[10, 5])
tommy = Student("tommy", 12345)

print(tommy._asdict())
# OrderedDict([('name', 'tommy'), ('id', 12345), ('age', 10), ('year', 5)])


from collections import namedtuple

Student = namedtuple("Student", "name id age year", defaults=[10, 5])
tommy = Student("tommy", 12345)
print(tommy)
# Student(name='tommy', id=12345, age=10, year=5)

# tommy.age = 11
print(tommy)

tommy_plus_one = tommy._replace(age=11)
print(tommy_plus_one)
# Student(name='tommy', id=12345, age=11, year=5)


from typing import NamedTuple

Student = NamedTuple("Student", [("name", str), ("id", int), ("age", int), ("year", int)])
tommy = Student("tommy", 12345, 10, 5)

print(tommy)
# Student(name='tommy', id=12345, age=10, year=5)


from typing import NamedTuple

class Student(NamedTuple):
    name: str
    id: int
    age: int = 10
    year: int = 5

tommy = Student("tommy", 12345)
# tommy.age = 11


class Car(NamedTuple):
    color: str
    vin: int
    wheels: int
    tons: int

ginger = Student("ginger", id=321, age=4, year=1)
pickup = Car("ginger", vin=321, wheels=4, tons=1)

print(ginger == pickup)
# True
