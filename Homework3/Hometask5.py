a = float(input("Please, input a first number: \n"))
b = float(input("Please, input a second number: \n"))
c = float(input("Please, input a third number: \n"))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print("a:", a, "b:", b, "c:", c)