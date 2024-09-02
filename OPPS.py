# CLASS => BLUEPRINT of OBJECT
# OBJECT => INSTANCE OF THAT CLASS

# Creating a Class
class Teacher():
    sub = "Python" #Class Attribute
    Salary = 12000
    name = "Akash"


# Creating a object 
Arsh = Teacher()
Arsh.name = "Arsh" #Object Attribute/Instance
# print(Arsh.name,Arsh.sub, Arsh.Salary)
# OBJECT ATTRIBUTE WILL TAKE PRECIDENCE

Akhi = Teacher()
Akhi.name = "Akhi"
# print(Akhi.name,Akhi.sub,Akhi.Salary)



class Student():
    name = "Akhi"
    Year = 2024
    RollNo = 418

    # Functions inside Classes are Known as METHODS
    def getInfo(self):
        print(f"My name is {self.name}.\nCurrent year = {self.Year}.\nRoll No. = {self.RollNo}")

    @staticmethod
    def greet():
        print("Hello" " Akhi")

Puchku = Student()

# Puchku.getInfo()
# |
# | Converts to this call
# v
# Student.getInfo(Puchku)
Puchku.name = "Puchku"
# Puchku.getInfo()
# Puchku.greet()


""" 
CONSTRUCTOR -> A FUNCTION WHICH IS AUTOMATICALLY
               CALLED WHEN AN OBJECT IS CREATED
"""

class Employee: 
    language = "Python" 
    salary = 1200000

    # Constructor
    def __init__(self,name,language,Salary): # dunder method which is automatically called
        self.name = name
        self.language = language
        self.salary = Salary
        print(f"Name = {name}\nLanguage = {language}\nSalary = {Salary}")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


# Akash = Employee()
# Akash.getInfo()

Akash = Employee("Akash","C++",1200000000000)
