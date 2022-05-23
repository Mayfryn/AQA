def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def kind_triangle(a, b, c):
    if not is_triangle(a, b, c):
        return "Not a triangle"
    else:
        if a == b == c:
            return "Equilateral triangle"
        elif a == b or a == c or b == c:
            return "Isosceles triangle"
        else:
            return "Versatile triangle"