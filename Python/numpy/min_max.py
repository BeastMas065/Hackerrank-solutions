import numpy
n,m = map(int,input().split())
a = numpy.array([list(map(int,input().split())) for _ in range(n)])
a = numpy.min(a,axis = 1)
print(numpy.max(a))