class Student:
    def __init__(self,name,age,grade,section,marks):
        self.name = name
        self.age = age
        self.grade = grade
        self.section = section
        self.marks = marks

    def update_grade(self, new_grade):
        self.grade = new_grade

s1 = Student("raj", 15, 10, "A", {"maths": 85, "science": 90, "english": 80})
s2 = Student("sita", 14, 9, "B", {"maths": 78, "science": 82, "english": 88})
s3 = Student("gita", 16, 11, "A", {"maths": 92, "science": 95, "english": 89})
print("___Report Card___")
print("Name:", s1.name)
print("Age:", s1.age)
print("Grade:", s1.grade)
print("Section:", s1.section)
print("Marks:", s1.marks)

print("\n___Report Card___")
print("Name:", s2.name)
print("Age:", s2.age)
print("Grade:", s2.grade)
print("Section:", s2.section)
print("Marks:", s2.marks)   

print("\n___Report Card___")
print("Name:", s3.name)
print("Age:", s3.age)
print("Grade:", s3.grade)
print("Section:", s3.section)
print("Marks:", s3.marks)

s1.update_grade(11)
print("Updated Grade:", s1.grade)
