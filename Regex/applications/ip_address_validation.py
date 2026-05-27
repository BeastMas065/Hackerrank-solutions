import re

ipv4 = r'((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'

ipv6 = r'([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}'

for _ in range(int(input())):
    s = input()

    if re.fullmatch(ipv4, s):
        print("IPv4")

    elif re.fullmatch(ipv6, s):
        print("IPv6")

    else:
        print("Neither")