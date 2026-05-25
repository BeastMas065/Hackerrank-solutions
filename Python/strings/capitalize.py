'''method 1(original logic fails on single letter word and empty string)
def solve(s):
    slist = s.split(" ")
    for i in range(len(slist)):
        slist[i] = slist[i][0].upper()+slist[i][1:]
    s = " ".join(slist)
    return s
'''
#method 2
def solve(s):
    slist = s.split(" ")
    a = [x.capitalize() for x in slist]
    s = " ".join(a)
    return s

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)