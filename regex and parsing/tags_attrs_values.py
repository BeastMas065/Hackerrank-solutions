from html.parser import HTMLParser

class pp(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for k,v in attrs:
            print("->", k,">", v)
            
html = ''
h = pp()
for _ in range(int(input())):
    html += input() + '\n'
h.feed(html)