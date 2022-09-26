import sys

if len(sys.argv) == 3:
    a = float(sys.argv[1])
    h = float(sys.argv[2])
    v = a * a * h / 3
    print("об'єм піраміди  = ", v)
else:
    print('wrong number of arguments')