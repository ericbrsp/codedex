#An object is an "instance" of a class
#A class is simply a template for creating objects

class Student:
  student_id = 0
  name = ''
  year = 0
  gpa = 0.0
  enrolled = False

wednesday = Student()

wednesday.student_id = 1113
wednesday.name = 'Wednesday Addams'
wednesday.year = 11
wednesday.gpa = 4.0
wednesday.enrolled = True

print(vars(wednesday))
