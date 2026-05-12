def merge_the_tools(string, k):
    i = 0
    while i < len(string):
        t = string[i:i+k]
        result = []
        for ch in t:
            if ch not in result:
                result.append(ch)
        print(''.join(result))
        i += k
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)