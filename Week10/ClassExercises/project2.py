class person:
    def __init__(self, name, age, address, city, state, zipcode):
        self.name = name
        self.age = age
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

class Student(person):
    def __init__(self, name, age, address, city, state, zipcode, studentID, GPA):
        super().__init__(name, age, address, city, state, zipcode)
        self.studentID = studentID
        self.GPA = GPA

class Teacher(person):
    def __init__(self, name, age, address, city, state, zipcode, teacherID, className):
        super().__init__(name, age, address, city, state, zipcode)
        self.teacherID = teacherID
        self.className = className

student = Student('Kevin Munoz', 25, 'Mountain View', 'Santa Ana', 'CA', 92703, 1245, 3.81)
teacher = Teacher('Jim Brooks', 45, 'Valley View', 'Santa Ana', 'CA', 94703, 532, 'Biology')

print(f'Name: {student.name}, Age: {student.age}, Address: {student.address}, {student.state}, {student.state} {student.zipcode}, Student ID: {student.studentID}, GPA: {student.GPA}')
print(f'Name: {teacher.name}, Age: {teacher.age}, Address: {teacher.address}, {teacher.state}, {teacher.state} {teacher.zipcode}, Teacher ID: {teacher.teacherID}, Class: {teacher.className}')