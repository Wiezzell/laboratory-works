import random

m: int = int(input('input m: '))
n: int = int(input('input n: '))

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

result = ''
for i in range(0, m):
    word = ''
    for j in range(0, n):
        randomAlphabetPosition = random.randrange(len(alphabet) - 1)
        word += alphabet[randomAlphabetPosition]
    result += word + ' '
