s = input("Enter a number: ")
i = 0


try:
    s = int(s) / i
except ValueError as e:
    print(e)
    s = 100
except ZeroDivisionError:
    s = 0

print(s)

try:
    1 / 0
except Exception as e:
    print(e)
    print(type(e))


# try:
# блок 1 # интерпретатор пытается выполнить блок1 except (name1,name2):
# блок 2 # выполняется, если в блоке try возникло исключение name1 # или name2
# except name3:
# блок 3 # выполняется, если в блоке try возникло исключение name3
# except:
# блок 4 # выполняется для всех остальных возникших исключений
# else:
# блок 5 # выполняется, если в блоке try не возникло исключения
# finally:
# блок 6 # выполнится всегда

try:
    s = int(s) / i
except (ValueError, ZeroDivisionError) as e:
    print(e)
    s = 100
finally:
    print("the end")
