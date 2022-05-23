n = input("Enter smth: ")
m = input("Enter another smth: ")
try:
    n, m = float(n), float(m)
    print(n+m)
except (TypeError, ValueError):
    print(n+m)