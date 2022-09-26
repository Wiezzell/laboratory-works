import math

r1: int = int(input('Введіть r1: '))
r2: int = int(input('Введіть r2: '))
x: int = int(input('Введіть Х точки:'))
y: int = int(input('Введіть У точки:'))

if (x + y <= r1 and x + y >= r2) or (x + y <= r2 and x + y >= r1):
    print('Dot belongs to ring')
else:
    print('Точка не належить кільцю')