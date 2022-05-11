# class MyClass(object): #object is not necessary
#     def __init__(self):
#         self.search = 'result'
#
#     def my_method(self, add=''):
#         print(self.search + add)
#
# obj = MyClass()
# obj.my_method()
# obj.my_method(add='!')
# print(obj.search)

class User:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):
        return "{} {}".format(self.name, self.surname)

    def get_older(self, years):
        self.age += years



user = User("John", "Dou", 25)

if __name__ == '__main__':
    print(user.full_name())
    user.get_older(3)
    print(user.age)
# def __str__(self):
#     return "User object with name {}, surname {}.".format(self.name, self.surname)
#
# def set_name(self, x):
#     self.name = x
#
def print_self(self):
    print(self)
#
# def say_hello(self):
#     print("Hello! I'm {}".format(self.name))


# user = User("John", "Dou", 25)
# print(user.title)
# print(user.name, user.surname)
# print(user)
# # print(user)
# # user.set_name("John")
# # print(user.name)
# print(user.print_self())
# user.say_hello()
#
# user2 = User()
# print(user2.title)
# user2.set_name("Jane")
# print(user2.name)
# user2.say_hello()
#
