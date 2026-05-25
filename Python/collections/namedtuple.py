from collections import *

n = int(input())

Data = namedtuple('Data', input().split())

total = 0

for _ in range(n):
    student = Data(*input().split())
    total += int(student.MARKS)

print(f'{total/n:.2f}')
