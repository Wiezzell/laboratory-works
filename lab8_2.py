import random

n: int = int(input('input N: '))
a: int = int(input('input a: '))
b: int = int(input('input b: '))

numbers = []
numbers3degree = []

for i in range(n):
    numbers.append(random.randrange(a - 1, b + 1))
    numbers3degree.append(3**i)

res = numbers + numbers3degree
list.sort(res)
print(res)