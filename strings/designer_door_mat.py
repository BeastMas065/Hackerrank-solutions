# Enter your code here. Read input from STDIN. Print output to STDOUT
c = '.|.'
height, width = input().split()
height = int(height)
width = int(width)
for i in range(height//2):
    print((c*(2*i+1)).center(width,'-'))
print(("WELCOME").center(width,'-'))
for i in range(height//2):
    print((c*(2*((height//2-1)-i)+1)).center(width,'-'))
