import numb_word

numb_word.task_header(3)


def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


print(is_year_leap(numb_word.numb()))

numb_word.task_header(4)


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


print(is_triangle(2, 3, 4))

numb_word.task_header(5)


def kind_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Such triangle exists!")
        if a == b or a == c or c == b:
            print("Isosceles triangle")
        elif a == b == c:
            print("Equilateral triangle")
        else:
            print("Versatile triangle ")
    else:
        print("Such triangle does not exist")


kind_triangle(2, 3, 4)

numb_word.task_header(6)


def distance(x1, y1, x2, y2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return d


print(distance(3, 4, 0, 0))

numb_word.task_header(7)


def dell_numbers(s):
    for i in s:
        if not i.isalpha():
            res = s.replace(i, "")
            s = res
        else:
            "Something went wrong! Check your function! "
    return res


print(dell_numbers('12dggf656 uygu'))
