f2 = open("read_write.txt", "w")

# f2.write("Hi! My name is...")
print("fsdf;hf rew ","rewfgwrsg",sep="", file=f2)

f2.close()

with open("new.txt", 'a') as f :
    f.write("#Some comment")

