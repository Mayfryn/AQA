def task_header(task_number):
    print(" #{0} ".format(task_number).center(100, '='))



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

