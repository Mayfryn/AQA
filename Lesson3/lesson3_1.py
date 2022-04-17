# # inp = input("Hi! Please, input some text here:")
# # print(len(inp))
#
# m = int(input("Please, input some number:"))
# n = int(input("Please, input another number:"))
# print(n + m)
#
# print(n + m, n, m, sep=", ")
# print(n + m, n, m, sep="\n")
# print(n + m, n, m, sep="")

s = "Hi there!"
l = [1, 3.14, "Hello", [5, 7, 8]]
print(s[1:5])
print(s[0:4])
print(l[1:3])
print(s[:7])
print(l[2:])
print(l[:])
print(s[0:-3:2])
print(l[::-1])
print(s[1::3])
print(s[2:8:-1])
print(s[8:2:-1])

l1 = [1, 3.14, "Hello", [5, 7, 'people']]
l1[1:3] = [1, 2, 3, 4, 5, 6, 7, 8]
l1[2:2] = ["eggs", "Spam"]
print(l1)