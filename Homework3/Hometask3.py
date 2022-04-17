y = int(input("Please, input a year: \n"))

# if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#     print("YES")
# else:
#     print("NO")

#Ternary Operator
# print("YES") if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else print("NO")

print("YES" if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else "NO")
