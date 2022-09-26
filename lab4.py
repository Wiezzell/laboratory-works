import math

def func(x0, x1, x2):
    Z = (x0**3 + x1) * (x2 - math.log(x2) - math.sin(x1)) + math.pow(x**3 + x2, 3)
    return (Z)

x = float(input("Введіть x: "))
a = float(input("Введіть a: "))
y = float(input("Введіть y: "))
S = func(x, a, y)
print(S)