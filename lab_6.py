import math

def calculate_expression(x):
    return 7 - x*math.exp(2*x-1) + math.sqrt(abs(x))

result_list = []

a = int(input('Введіть a: '))
b = int(input('Введіть b: '))
h = int(input('Введіть h: '))

for i in range(a, b+1, h):
    result_list.append(calculate_expression(i))

a = int(input('Введіть a: '))
b = int(input('Введіть b: '))
h = int(input('Введіть h: '))

while a <= b:
    result_list.append(calculate_expression(a))
    a += h;

print(result_list)

set_of_results = set()
duplicated_results = []

for result in result_list:
    if result in set_of_results:
        duplicated_results.append(result)
    else:
        set_of_results.add(result)

print('Дублікати в результатах: ', duplicated_results)