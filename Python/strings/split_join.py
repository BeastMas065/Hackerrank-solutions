def split_and_join(line):
    st = line.split()
    st = "-".join(st)
    return st

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)