# def repeat(s, exclaim):
#     results = s * 3
#     if exclaim:
#         results = results + '!!!'
#     return results
#
#
# r = repeat('wow', True)
# print(r)


def hypo(a, b):
    h = (a ** 2 + b ** 2) ** 0.5
    return h


print(hypo(3, 4))
print(hypo(4, 4))
print(hypo(1, 2))

