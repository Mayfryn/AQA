while True:
    print("Type 'quit' to exit")
    phrase = input("Your message: ")
    if phrase == "quit":
        break
    elif phrase == "Hello" or phrase == "Hi":
        print("Hi! How's it going?")
    elif phrase == "What is your name?":
        print("I don't have name :(")
    else:
        print("I don't understand you")

# for letter in 'Python':  # First Example
#     if letter == 'h':
#         break
#     print
#     'Current Letter :', letter
#
# var = 10  # Second Example
# while var > 0:
#     print
#     'Current variable value :', var
#     var = var - 1
#     if var == 5:
#         break
#
# print
# "Good bye!"