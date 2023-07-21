class Student:
    name=""
    address=""

    def __init__(self, student_id):
        print("object is created!")

    def print_name(self):
        print(self.name)

    def print_address(self):
        print(self.address)

    def study(self, study):
        self.study = study
        print(self.study)
    
    def plays_sport(self,sport):
        self.sport = sport
    
    def __del__(self):
        print("Object is destroyed!")

student1 = Student(1902) #create an object
print(id(student1))

student1.name="Mahesh"
student1.address="Delhi"
student1.print_name()
student1.print_address()
student1.study("CSE")




