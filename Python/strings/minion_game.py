def minion_game(string):
    l = len(string)
    v = 'AEIOU'    
    k = 0
    s = 0
    for i in range(l):
        if string[i] in v:
            k += l - i
        else:
            s += l - i
    if k > s:
        print("Kevin", k)
    elif k < s:
        print("Stuart", s)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)