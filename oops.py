#OOPs Object Oriented Programming
#use Object classes 
#Object with thier methods and behaviours/attributes

#Class blueprint for creating objects class has methods and attributes
#Object instance of a class
#Inheritence mechanism copy methods from parent class to child class
#Polymorphism same method different way 
#Encapsulation boundry methods 
#Abstraction hiding internal details
#method overidding same method different argument
#composition combine simpler object

#base class
class School:
    def __init__(self, name, address, schoolID):
        #construct school attributes
        self.name = name
        self.addr = address
        self.sch_id = schoolID
    #Method to display school info
    def dis_sch_info(self):
        return f"School Name: {self.name}, Address: {self.addr}, Schoold ID:{self.sch_id} "
    
#create object from class 
school_muhammad = School("Iqra", "T block", 301)
school_osama = School("Queen", "Clifton", 302)
school_ali = School("sadiq", "bahawalpur", 303)

#print(school_ali.dis_sch_info())


#inheritence
#parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name}, and I am {self.age} years old"

#child class 
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) #inherit
        self.stu_id = student_id

    def dis_stud_info(self):
        return f"{self.introduce()}, Student ID: {self.stu_id}"
    
stu_Muh = Student("Muhammad", 30, "iq8765")
print(stu_Muh.dis_stud_info())