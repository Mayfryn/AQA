# # def func(*args):
# #     return(args)
# # print(func())
# # print(func(1,3,4,6, 'h', 'fdsg'))
def second(*x):
    x = list(x)
    x.sort()
    return x[1]
m = (1,4,7,2)
print(second(1,6,4,3,7,0))
#
#
# def second(*x):
#     x = list(x[0])
#     x.sort()
#     return x[1]
# m = (1,4,7,2)
#
# print(second(m))
#
# def f(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
# f(a=1, b=4)

