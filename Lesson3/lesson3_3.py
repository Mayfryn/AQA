# l = [1,2,3,4,5,6,7,7]
# while l:
#     print(l.pop());
# ------------------------------------
# n = int(input("enter a number: "))
# i = 0
#
# while n % 2 == 0:
#     n = n / 2
#     i += 1
#
# print(i)
# ------------------------------------
# l = [1, 2, 3, 4, 5, 6, 7, 7]
#
# for i in l:
#     if i % 2 == 0:
#         print(i)
#     else:
#         print(i+1)
#--------------------------------------
# l = [1, 2, 3, 4, 5, 6, 7, 7]
#
# for i in l:
#     if i % 2 == 0:
#         print(i)
#     else:
#         l.insert(l.index(i), i + 1)
#         l.remove(i)
#
#         print(i+1)
# print(l)
#----------------------------------------

for i in range(2, 80, 4):
    print(i)

l = list(range(0,10))
print(l)

li = [1, 2, 3, 4, 5, 6, 7, 7]
for ind in range(len(li)):
    if li[ind] % 2 != 0:
        li[ind] += 1
print(li)
