n, x = map(int,input().split())
marks = []
for _ in range(x):
    sub = list(map(float,input().split()))
    marks.append(sub)
d = list(zip(*marks))
for i in d:
    print(sum(i)/len(i))