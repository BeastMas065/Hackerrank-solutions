import textwrap

def wrap(string, max_width):
    str = list(string)
    for i in range(len(string),1,-1):
        if i%max_width==0:
            str.insert(i,"\n")
    return "".join(str)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)