n = int(input())
arr = list(map(int,input().split()))
a = set(arr)
print(int((sum(a)*n-sum(arr))/(n-1)))
