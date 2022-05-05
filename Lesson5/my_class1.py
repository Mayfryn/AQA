class MyClass(object): #object is not necessary
    def __init__(self):
        self.search = 'result'

    def my_method(self, add=''):
        print(self.search + add)

obj = MyClass()
obj.my_method()
obj.my_method(add='!')
print(obj.search)

class User:
    pass

ob = User()
ob2 = User()
print(ob)
print(ob2)