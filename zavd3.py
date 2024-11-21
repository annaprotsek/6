import math

def calculate_function(x):
    return 3 - math.log(abs(x - 6)) + math.cos(x)

def save_to_list_and_display():
    a = float(input("Введіть початок діапазону a: "))
    b = float(input("Введіть кінець діапазону b: "))
    h = float(input("Введіть крок h: "))
    
    values = [] 
    x = a
    while x <= b:
        values.append(calculate_function(x))
        x += h

    print("Значення у рядок:")
    print(" ".join(f"{v:.4f}" for v in values))
    
    print("\nЗначення у стовпчик:")
    for v in values:
        print(f"{v:.4f}")

save_to_list_and_display()
