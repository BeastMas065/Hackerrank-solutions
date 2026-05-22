import numpy as np

e = list(map(int,input().split()))
a = np.array(e)
a.shape = (3,3)
print(a)