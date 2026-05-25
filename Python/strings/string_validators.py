if __name__ == '__main__':
    s = input()
    key1 = False
    key2 = False
    key3 = False
    key4 = False
    key5 = False
    for char in s:
        if char.isalnum():
            key1 = True
            break
    for char in s:
        if char.isalpha():
            key2 = True
            break
    for char in s:
        if char.isdigit():
            key3 = True
            break
    for char in s:
        if char.islower():
            key4 = True
            break
    for char in s:
        if char.isupper():
            key5 = True
            break
    print(key1)
    print(key2)
    print(key3)
    print(key4)
    print(key5)
