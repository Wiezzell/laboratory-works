import math


def isFullSquareNumber(number: float) -> bool:
    if number < 0:
        return False
    if math.sqrt(number) != 0:
        return False
    return True


n = float(input('input n: '))

print(isFullSquareNumber(n))
if not isFullSquareNumber(n):
    n = (int(math.sqrt(n)) + 1) ** 2

matrix = []
iter: int = 1
for i in range(int(math.sqrt(n))):
    subMatrix = []
    for j in range(int(math.sqrt(n))):
        subMatrix.append(iter)
        iter += 1
    matrix.append(subMatrix)

print(matrix)