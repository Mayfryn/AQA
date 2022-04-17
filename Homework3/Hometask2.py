s = input("Please, input a string: \n")

# if len(s) % 2 == 0:
#     new_s = s[int(len(s)/2):] + s[:int(len(s)/2)]
# else:
#     new_s = s[int(len(s)/2)+1:] + s[:int(len(s)/2)+1]

i = round((len(s) + 0.01) / 2) #if two multiples are equally close, rounding is done toward the even choice

new_s = s[i:] + s[:i]

print(new_s)
