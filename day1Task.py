class Student:
    def __init__(self,name,age,grade,section,marks):
        self.name = name
        self.age = age
        self.grade = grade
        self.section = section
        self.marks = marks

    def display_report_card(self):
        print("___Report Card___")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)
        print("Section:", self.section)
        print("Marks:", self.marks)

    def update_grade(self, new_grade):
    
        self.grade = new_grade

s1 = Student("raj", 15, 10, "A", {"maths": 85, "science": 90, "english": 80})
s2 = Student("sita", 14, 9, "B", {"maths": 78, "science": 82, "english": 88})
s3 = Student("gita", 16, 11, "A", {"maths": 92, "science": 95, "english": 89})
s1.display_report_card()
s2.display_report_card()
s3.display_report_card()



s1.update_grade(11)
print("Updated Grade:", s1.grade)
