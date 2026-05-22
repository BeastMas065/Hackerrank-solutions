def wrapper(f):
    func = []
    def fun(l):
        for i in l:
            if len(i) == 10:
                func.append(' '.join(["+91",i[:5],i[5:]]))
            elif len(i) == 11:
                func.append(' '.join(["+91",i[1:6],i[6:]]))
            elif len(i) == 12:
                func.append(' '.join(["+91",i[2:7],i[7:]]))
            else:
                func.append(' '.join(["+91",i[3:8],i[8:]]))
        f(func)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


