from datetime import datetime
def time_delta(p, q):
    format = "%a %d %b %Y %H:%M:%S %z"
    d1 = datetime.strptime(p, format)
    d2 = datetime.strptime(q, format)
    diff = abs(int((d1 - d2).total_seconds()))
    print(diff)
t = int(input())
for t_itr in range(t):
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)