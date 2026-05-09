n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
sum = 0
x=0
for i in student_marks[query_name]:
    sum += i
    x += 1

print("{0:.2f}".format(sum/x))