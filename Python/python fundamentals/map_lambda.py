cube = lambda x: x**3

def fibonacci(n):
    fib = []
    if n == 0:
        return fib
    for i in range(1, n+1):
        if i <= 2:
            fib.append(i-1)
        else:
            fib.append(fib[-1] + fib[-2])
    return fib
        
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))