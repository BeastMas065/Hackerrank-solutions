if __name__ == '__main__':
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])

    low = float('inf')
    low2 = float('inf')

    for i in range(len(scores)):
        s = scores[i][1]

        if s < low:
            low2 = low
            low = s

        elif s < low2 and s != low:
            low2 = s
    
    names = []

    for i in range(len(scores)):
        if scores[i][1] == low2:
            names.append(scores[i][0])

    for name in sorted(names):
        print(name)