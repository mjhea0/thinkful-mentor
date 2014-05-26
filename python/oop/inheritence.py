class SchoolMember(object):

    """Represents any member of the school."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def output_details(self):
        return "Name: {}, Age: {}".format(self.name, self.age)

class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def output_details(self):
        SchoolMember.output_details(self)
        return "{} is {} years old and makes {} a year.".format(self.name,self.age,self.salary)

class Student(SchoolMember):

    def __init__(self, name, age, gpa):
        SchoolMember.__init__(self, name, age)
        self.gpa = gpa
    
    def output_details(self):
        SchoolMember.output_details(self)
        return "{} is {} years old and has a {} GPA.".format(self.name,self.age,self.gpa)

teacher = Teacher("Mr. Clark", 35, 35000)
student = Student('Michael', 22, 3.12)

print teacher.output_details()
print student.output_details()
