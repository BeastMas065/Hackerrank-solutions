n = int(input())
arr = list(map(int, input().split()))
arr.sort()
flag = True
for i in range(1,n):
    if arr[-1] == arr[i]:
        print(arr[i-1])
        flag = False
        break
if flag:
    print(arr[-2])