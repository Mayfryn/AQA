def numb():
    while True:
        n = input("Enter any number: ")
        try:
            n = float(n)
        except ValueError:
            print("Dummy head! That is not a number!")
        else:
            break
    return n



def word():
    while True:
        print("Type a word to exit")
        w = input("Try it: ")
        if " " not in w.strip(' '):
            break
        else:
            print("That is a phrase")
    return w

def task_header(task_number):
    print(" #{0} ".format(task_number).center(100, '='))

if __name__ == '__main__':
    numb()
    word()