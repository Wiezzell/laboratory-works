a = input("Введіть слова: ")
v = a.split()
f = len((max(v, key=len)))
b = len((min(v, key=len)))
print("Довжина найбільшого слова: ", f)
print("Довжина найменшого слова: ", b)