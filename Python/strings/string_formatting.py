def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        print("{:{w}d} {:>{w}o} {:>{w}X} {:>{w}b}".format(i, i, i, i, w=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)