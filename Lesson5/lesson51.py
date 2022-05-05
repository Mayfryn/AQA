# import my_package.functions as my_module
# from my_package import functions
# from my_package.functions import task_header
#
# my_module.task_header(1)

# x = input("Enter a str: ")
# assert type(x) is int, "Variable 'x' must be int"

def func(a, b, c, d):
    return (a - b) * c / d


l = [5, 4, 5, 10]
j = ["fg", 'fg', "rkdh"]
print(func(*l))
print(*j)

d = {"a": 2, "b": 6, "c": 6, "d": 4}
print(func(**d))

di = {"end": "!!!!\n", "sep": "-"}
print("Tam", "param", "pam", "pam", **di)


def print_age(name, age):
    print(name, 'is', age, 'years old')


persons = [{"name": "Jinny", "age": 15}, 
           {"name": "John", "age": 30},
           {"name": "Jane", "age": 34}]

for persons in persons:
    print_age(**persons)
