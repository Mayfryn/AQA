# 1) Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
# если год високосный, и False иначе.
# 2) Функция принимает три числа a, b, c. Функция должна определить, существует ли
# треугольник с такими сторонами. Если треугольник существует, вернёт True, иначе False.

def task_header(task_number):
    print(" #{0} ".format(task_number).center(100, '='))


task_header(1)


def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


print(is_year_leap(1988))

task_header(2)


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


print(is_triangle(2, 3, 4))
