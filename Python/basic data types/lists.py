if __name__ == '__main__':
    N = int(input())
    listf = []
    for i in range(N):
        query = input()
        query = query.split()
        match query[0]:
            case 'insert':
                listf.insert(int(query[1]),int(query[2]))
            case 'remove':
                listf.remove(int(query[1]))
            case 'append':
                listf.append(int(query[1]))
            case 'sort':
                listf.sort()
            case 'pop':
                listf.pop()
            case 'reverse':
                listf.reverse()
            case 'print':
                print(listf)