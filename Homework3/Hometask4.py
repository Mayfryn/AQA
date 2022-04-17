a = float(input("Please, input a first number: \n"))
b = float(input("Please, input a second number: \n"))
c = float(input("Please, input a third number: \n"))

# if a + b > c and a + c > b and b + c > a:
#     print("YES")
# else:
#     print("NO")

print("YES" if a + b > c and a + c > b and b + c > a else "NO")
