import numpy
n, m = map(int,input().split())
a = numpy.array([list(map(int,input().split())) for _ in range(n)])
a = numpy.sum(a,axis = 0)
print(numpy.prod(a))