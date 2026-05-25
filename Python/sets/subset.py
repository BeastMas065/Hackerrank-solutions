# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    buzzer = True
    m = int(input())
    a = list(map(int,input().split()))
    n = int(input())
    b = list(map(int,input().split()))
    for i in a:
        if i not in b:
            buzzer = False
            break
    print(buzzer)
    print(b)
