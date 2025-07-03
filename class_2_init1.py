class Student:
  def __init__(self, name, year, gpa, enrolled):
    self.name = name
    self.year = year
    self.gpa = gpa
    self.enrolled = enrolled


eric = Student('Eric Gonçalves', 43, 4.9, True)
ladybird = Student('Christine McPherson', 12, 4.0, True)
kyle = Student('Kyle Scheible', 12, 3.4, True)

print(vars(eric))
print(vars(ladybird))
print(vars(kyle))

