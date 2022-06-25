res = [x**(1/2) for x in range(1, 26, 2) ]
print(res)


names = ["John", "jane", "2314124", "OLALA", "oLena"]
names = [name.title() for name in names if name.isalfa() ]
print(names)