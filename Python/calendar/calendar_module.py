import calendar
m, d, y = map(int,input().split())
'''
initial method
c = calendar.TextCalendar(calendar.SUNDAY)
x = c.monthdayscalendar(y,m)
for i in x:
    for j in range(7):
        if i[j] == d:
            print(days[j])
            break
'''
c = calendar.weekday(y,m,d)
days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print(days[c])