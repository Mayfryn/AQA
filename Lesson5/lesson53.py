# class Person:
#
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def full_name(self):
#         return "{} {}".format(self.name, self.surname)
#
#     def get_older(self, years):
#         self.age += years
from Lesson5.my_class1 import User


class Employee(User):
    def __init__(self, name='', surname='', age=None, position="", salary=0):
        # self.name = name
        # self.surname = surname
        # self.age = age
        # User.__init__(self, name, surname, age)   #instead of copy those commented strings
        super().__init__(name, surname, age)
        self.position = position
        self.salary = salary

    def income(self, months):
        return self.salary * months

    def new_method(self):
        print(self.age)

    def __str__(self):
        return "User object with name {} and surname {}. Under age {} works as {}. And has income as {}$ per " \
               "mounth".format(
            self.name, self.surname, self.age, self.position, self.salary)

    def increase_salary(self, delta):
        self.salary += delta


e = Employee(name='Olga', surname="Rabota", age=33, position="AQA", salary=5000)
e.new_method()
print(e)
print(e.full_name())
e.get_older(3)
print(e.age)


class ITEmployee(Employee):
    """
        def __init__(self, name='', surname='', age=None, position="", salary=0):
        super().__init__(name, surname, age, position, salary)"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = []
        self.rate = 0

    def __str__(self):
        return "IT employee with name {} and surname {}. Under age {} works as {}. And has income as {}$ per " \
               "month. Has rate as {}. Skills: {}".format(
            self.name, self.surname, self.age, self.position, self.salary, self.rate, self.skills)

    def add_skill(self, skill):
        self.skills.append(skill)


ite = ITEmployee()
ite.skills.append('Python')
ite.skills.append('git')
ite.rate = 5
print(ite)
