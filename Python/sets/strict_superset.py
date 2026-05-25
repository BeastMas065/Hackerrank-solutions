a = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    subset = True

    b = set(map(int, input().split()))

    for i in b:
        if i not in a:
            subset = False
            break

    if not subset or a == b:
        result = False
        break

print(result)