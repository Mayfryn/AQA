a = int(input("Please, input a first number: \n"))
b = int(input("Please, input a second number: \n"))
c = int(input("Please, input a third number: \n"))

if a == b == c:
    print(3)
elif a != b and a != c and b != c:
    print(0)
else:
    print(2)
