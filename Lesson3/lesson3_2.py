speed = int(input("Enter speed:"))

if speed >= 80:
    print("You're riding too fast. Please, lower you speed!")
else:
    print("Have a nice day!")


if speed >= 80:
    print("You're riding too fast. Please, lower you speed!")
elif speed < 0:
    print("You are going to a wrong way!")
else:
    print("Have a nice day!")

    s = input("?:")

    if 'Hi' == s:
        print("hello!")

    print("Goodbye!")

    # ______________________

    x = float(input("Enter a number"))

    if 0 < x <= 100:
        print("Correct number: ")
    else:
        print("Incorrect number")