# input_file = open('read_write.txt', 'r', )
#
# print(input_file.read())
#
#
# s = input_file.read(10)
# s2 = input_file.read(10)
#
#
# print(s)
# print(s2)
#
# input_file.close()
#
# f2 = open("read_write.txt", 'w')
# f2.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin tempus urna ante, commodo gravida nibh lacinia a. In interdum laoreet diam, eu congue sem blandit in. Donec placerat leo sed ante rutrum, a facilisis dui mattis. Donec ut odio gravida, pretium tortor mattis, imperdiet tellus. Vivamus facilisis neque sed rutrum pellentesque. Maecenas nec efficitur eros, sit amet ultrices justo. Mauris vitae lorem vel eros condimentum pharetra. Praesent eget arcu sed eros venenatis laoreet. Proin mauris augue, elementum at cursus eu, faucibus in enim. Aenean euismod, arcu at lacinia congue, metus sem porta leo, et laoreet massa nisi dictum mi. Quisque eleifend dui a tellus finibus rhoncus. Duis facilisis finibus ipsum, eu rhoncus dui fermentum ac.")
# f2.writelines()
#
# f2.close()

input_file = open('read_write.txt', 'r', )
i = 0
for line in input_file.readlines():
    print(f"{i}", line)
    i += 1

input_file.close()