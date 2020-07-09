### 3
# class Duck:
#     def __init__(self, name, bill_discription, tail_length, collar):
#         self.name = name
#         self.bill = Bill(bill_description)
#         self.tail = Tail(tail_length)
#         self.collar = collar

#     def about(self):
#         print(f"This duck has a {self.bill.description}, {self.tail.tail_length}, and {self.color} ")

# ### composition relationship --> dependent on other classes. One class needs to other in order to exist
# class Bill:
#     def __init__(self, description)
#         self.description = description

# class Tail:
#     def __init__(self, length)
#         self.length = length

# ### aggregate relationship --> exists independently. Added to other classes, can exist indpendently.
# class Collar:
#     def __init__(self, color):
#         self.color = color

# my_collar = Collar("red")
# duck = Duck('Quackers', 'wide orange', 'long')
# duck.about()

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