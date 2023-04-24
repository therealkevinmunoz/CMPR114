class Teacher:
    def __init__(self, name, class_room, course):
        self.name = name
        self.class_room = class_room
        self.course = course
    def get_information(self):
        print(f'Teacher\'s name is {self.name}')
        print(f'Teacher\'s class room is {self.class_room}')
        print(f'Teacher\'s course is {self.course}')

Teacher2 = Teacher('Kevin Munoz', '600', 'Intro to Comp Sci')
Teacher2.get_information()