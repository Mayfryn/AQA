s = input("Please, input a string: \n")

# print(s[2], s[-2], s[:5], s[:-2], s[::2], s[1::2], s[::-1], s[-2::-2], s[-2:0:-1], len(s), sep='\n')

l = [s[2], s[-2], s[:5], s[:-2], s[::2], s[1::2], s[::-1], s[-1::-2], s[-2::-2], s[-2:0:-1], len(s)]

for i in range(len(l)):
    print(i + 1, ": ", l[i], sep="")
