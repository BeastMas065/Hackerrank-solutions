def average(array):
    a = set(array)
    avg = 0
    for x in a:
        avg += x
    avg /= len(a)
    return("{0:0.3f}".format(avg))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)