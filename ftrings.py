class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def __str__(self):
        return f"This is an object of student class, with student name as {self.name} and lives at {self.address}"
    def __repr__(self):
        return f"this is the name {self.name} and he is living in {self.address}"

obj = Student("Mahesh", "Delhi")

print(f"{obj}")
print(f"{obj.__repr__()}")