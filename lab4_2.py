import math

x = float(input("Введіть x: "))
y = (math.cos(math.fabs(x**3-4))+math.log(x))/math.pow(x-8+x**2,3)
print("Відповідть:",y)