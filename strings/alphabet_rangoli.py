import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4 * size - 3

    rows = []

    for i in range(size):
        left = alpha[i:size]
        
        s = '-'.join(left[::-1] + left[1:])
        
        rows.append(s.center(width, '-'))

    print('\n'.join(rows[::-1] + rows[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)