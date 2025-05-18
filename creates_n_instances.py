class Student():
    def __init__(self,Name, Age, Class, Id, Grade):
        self.Name = Name
        self.Age = Age
        self.Class = Class
        self.Id = Id
        self.Grade = Grade
    def Give_info(self):
        print(f"This the the name you have givven: {self.Name} \nthis is your Age: {self.Age}\nthis is your class: {self.Class} \nyour ID: {self.Id} \nand your: {self.Grade}")

class kid(Student):
    def is_a_kid_or_not(self):
        if self.Age < 18:
            print(f"The student {idx} Name {self.Name} is a Minor.")
        else:
            print(f"The sudent {idx} Name {self.Name} is an adult.")

Number_of_students = int(input("The number of students you wnat to enter: "))
students_list = []
for i in range(0,Number_of_students):
    print(f"Enter the details of student {i+1}")
    name = str(input("enter the name: "))
    age = int(input("enter the age: "))
    Classs = int(input("enter the class: "))
    id = int(input("enter the id: "))
    grade = str(input("enter the grade: "))
    s = kid(Name=name, Age=age, Class=Classs, Id=id, Grade=grade)
    students_list.append(s)


# print("\n--- Student Information ---")
# for item in students_list:
#     item.Give_info()
for idx, item in enumerate(students_list, start=1):
    print(f"Here are the detail of the student {idx}")
    item.Give_info()
    item.is_a_kid_or_not()

