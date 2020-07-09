### example 2
# class Student:
#     def __init__(self, name):
#         self.name = name

# class Graduate(Student):
#     def __init__(self, name, graduation_date):
#         # looks up to the Student parent class and Graduate child class inherits it
#         super().__init__(name)
#         self.graduation_date = graduation_date

### example 1
# class Bicycle:
#     def exclaim(self):
#         print("I'm a bicycle!")

# class Specialized(Bicycle):
#     def jump(self):
#         print("I'm jumping!")

# a_bicycle = Bicycle()
# a_specialized = Specialized()