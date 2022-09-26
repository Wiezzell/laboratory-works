import math

x = float(input("Введіть x: "))

if x>= 0:
    a = x+(2**x-4)-math.sqrt(x)
    print(a)
elif -7.7 < x:
    b = math.sin(2*x)+math.log10(abs(x))
    print(b)
elif x<=0:
    c = math.cos(3*x-(1/x))
    print(c)
else:
    print("Обчислення неможливе.")