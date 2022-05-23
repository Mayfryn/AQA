from datetime import datetime


class Person:
    """
    Person (два свойства: 1. теперь full_name пусть будет свойством, а не функцией (одно
поле, мы ожидаем - тип строка и состоит из двух слов «имя фамилия»), а свойств name и
surname нету, 2. год рождения).
Реализовать методы, которые:
1. выделяет только имя из full_name
2. выделяет только фамилию из full_name;
3. вычисляет сколько лет было/есть/исполнится в году, который передаётся
параметром (obj.age_in(year)); если не передавать параметр, по умолчанию,
сколько лет в этом году;
* (дополнительное) Можете в конструкторе проверить, что в full_name передаётся
строка, состоящая из двух слов, если нет, вызывайте исключение
* (дополнительное) Можете в конструкторе проверить, что в год рождения меньше или
равно 2020 (текущий год – для продвинутых), но больше или равно 1900. Если нет,
вызывайте исключение
    """

    def __init__(self, full_name, birth_year=1900):
        self.full_name = full_name
        if len(self.full_name.split()) != 2:
            raise ValueError("Wrong name")
        self.birth_year = birth_year
        if 1900 > self.birth_year or self.birth_year > datetime.now().year:
            raise Exception("Wrong year of birth.")

    def __str__(self):
        return "This is a human with name {}. It was born at {}.".format(self.full_name, self.birth_year)

    def only_name(self):
        return self.full_name.split()[0]

    def only_surname(self):
        return self.full_name.split()[1]

    def age_in(self, year=2022):
        return year - self.birth_year


class Employee(Person):
    """
    Employee (наследуемся от Person) (добавляются свойства: должность, опыт работы,
зарплата)
* (дополнительное) Можете в конструкторе проверить, что в опыт работы и зарплата
не отрицательные
Реализовать новые методы:
1. возвращает должность с приставкой, которая зависит от опыта работы: Junior —
менее 3 лет, Middle — от 3 до 6 лет, Senior — больше 6 лет.
Т.е. метод должен вернуть позицию с приставкой Junior/Middle/Senior &lt;position&gt;.
Если, например, у вас объект имел должность “programmer” с опытом 2 года,
метод должен вернуть “Junior programmer”
2. метод, который увеличивает зарплату на сумму, которую вы передаёте
аргументом.
    """

    def __init__(self, full_name, birth_year, position="", experience=0, salary=0):
        super().__init__(full_name, birth_year)
        self.position = position
        self.experience = experience
        if self.experience < 0:
            raise Exception("Wrong value for experience.")
        self.salary = salary
        if self.salary < 0:
            raise Exception("Wrong value for salary.")

    def __str__(self):
        return "This is a human with name {}. It was born at {}. It works as a {} for a {} year(s). Its income is {} " \
               "per month".format(self.full_name, self.birth_year, self.position, self.experience, self.salary)

    def upd_position(self):
        if 0 < self.experience < 3:
            self.position = "Junior " + self.position
            return self.position
        if 3 < self.experience < 6:
            self.position = "Middle " + self.position
            return self.position
        else:
            self.position = "Senior " + self.position
            return self.position

    def increase_salary(self, delta):
        self.salary += delta


class ITEmployee(Employee):
    """
    ITEmployee (наследуемся от Employee)
1. Реализовать метод добавления одного навыка в новое свойство skills (список) новым
методом add_skill (см. презентацию).
2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список)
новым методом add_skills.
Тут можно выбрать разные подходы: или аргумент один и он список навыков, которым вы
расширяете список-свойство skill, или вы принимаете неопределённое количество
аргументов, и все их добавляете в список-свойство skill
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skill = []

    def __str__(self):
        return "{} is an IT employee.\nHe/She was born at {} and works as {} for a {} year(s).\nAnd has income as {}$ " \
               "per month.\nSkills: {}".format(
            self.full_name, self.birth_year, self.position, self.experience, self.salary, self.skill)

    def add_skill(self, skill):
        self.skill.append(skill)

    def add_some_skills(self, new_skills):
        self.skill += new_skills


if __name__ == '__main__':
    p1 = Person('Billie Bob', 1954)
    e1 = Employee('Billie Bob', 1954, "QA", 8, 500)
    ite1 = ITEmployee('Billie Bob', 1954, "QA", 8, 500)
    print(p1)
    print(p1.only_name())
    print(p1.only_surname())
    print(p1.age_in(2082))
    # p2 = Person("John Dou", 2078)
    # p3 = Person("JaneDou", 1947)
    print()
    print(e1)
    print(e1.upd_position())
    e1.increase_salary(1000)
    print(e1.salary)
    print()
    ite1.add_skill("python")
    ite1.add_skill("git")
    list1 = ["git", "python"]
    ite1.add_some_skills(list1)
    print(ite1)
