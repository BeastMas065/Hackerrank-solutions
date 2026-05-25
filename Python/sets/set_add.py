# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
stamps = set()
for i in range(n):
    stamps.add(input())
    
print(len(stamps))