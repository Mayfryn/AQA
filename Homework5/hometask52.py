from datetime import datetime
import math


class RectanglularArea:
    def __init__(self, length=0, width=0):
        self.length = length
        assert length >= 0
        self.width = width
        assert width >= 0

    def __str__(self):
        return "This is a room with length - {} m and width - {} m.".format(self.length, self.width)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


class Student:

    def __init__(self, full_name="", profession="", start_year=0, rating=[]):
        self.full_name = full_name
        self.profession = profession
        self.start_year = start_year
        self.rating = rating

    def __str__(self):
        return f"<Student object: full_name {self.full_name} \nprofession {self.profession}\nstart_year {self.start_year}\nrating {self.rating}>"

    def update_rating(self, new_r=0):
        self.rating.append(new_r)

    def average_rating(self):
        i = 0
        for mark in self.rating:
            i += mark
        return i / len(self.rating)

    def get_time_study(self):
        return datetime.now().year - self.start_year


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<Point object: x = {self.x}  and y = {self.y}>"

    def get_distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_distance_to_point(self, px=0, py=0):
        return ((self.x - px) ** 2 + (self.y - py) ** 2) ** 0.5

    def get_polar_system(self):
        new_coord = [self.get_distance(), math.atan(self.y / self.x)]
        return new_coord


if __name__ == '__main__':
    room = RectanglularArea(5, 8)
    print(room)
    print(room.area())
    print(room.perimeter())

    student = Student("John Dou", "constructor", 2006, [100, 89, 67, 90])
    print(student)
    print(student.average_rating())
    student.update_rating(89)
    print(student.average_rating())
    print(student.get_time_study())

    point = Point(3, 4)
    print(point)
    print(point.get_distance_to_point(5, 7))
    print(point.get_polar_system())
