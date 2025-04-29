#polymorphism

#parent class
class Staff:
    def role(self):
        pass

#child class
class Teacher(Staff):
    def role(self):
        return "I teach students"

#another child class
class Admin(Staff):
    def role(self):
        return "I manage School"
    
#polymorphism
def show_role(personnel):
    print(personnel.role())

#Objects
teacher = Teacher()
admin = Admin()

show_role(teacher)
show_role(admin)


#Encpsulation
#Public attributes (accessible from anywhare classes or subclasses)
#self.name = name
#Protected attributes (accessible within the class and subclas but discourage outside )
#self._name = name
#Private attributes (only within the class)
#self.__name = name 

class School:
    def __init__(self, name, location):
        self.name = name #public
        self._location = location #protected
        self.__funds = 100000 #private (abstraction)

    def dis_info(self):
        return f"School name: {self.name}, Location: {self._location}"
    
    def get_fund(self):
        return f"School funds: PKR {self.__funds}"
    
    def add_funds(self, amount):
        self.__funds += amount


aliSchool = School("sadiq", "Bahawalpur")

#print(aliSchool.name)

#print(aliSchool._location)


aliSchool.add_funds(20000)
#print(aliSchool.get_fund())


#overridding

#parent class
class Person:
    def __init__(self):
        self.name = "Ali"
        self.age = 30
    
    def introduce(self):
        return f"My name is {self.name}, and I am {self.age} years old"

#child class 
class Student(Person):
    def __init__(self):
        super().__init__() #inherit

    def introduce(self): #overriding
        return f"My name is Muhammad, and I am 30 years old"


person = Person()
student = Student()

print(person.introduce())
print(student.introduce())

