import numpy
c = list(map(float,input().split()))
x = float(input())
print(numpy.polyval(c,x))