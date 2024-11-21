import math

def calculate_function(x):
    return 3 - math.log(abs(x - 6)) + math.cos(x)

def tabulate_with_parameter():
    a = float(input("Введіть початок діапазону a: "))
    b = float(input("Введіть кінець діапазону b: "))
    h = float(input("Введіть крок h: "))
    
    x = a
    while x <= b:
        print(f"f({x:.2f}) = {calculate_function(x):.4f}")
        x += h

tabulate_with_parameter()
