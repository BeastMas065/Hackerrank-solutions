from html.parser import HTMLParser
class pp(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print("->",i[0],">",i[1])
        
    def handle_endtag(self, tag):
        print("End   :", tag)
        
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print("->",i[0],">",i[1])
    
    def handle_comment(self, data):
        return()
        
p = pp()
h = ''
for _ in range(int(input())):
    h += input() + '\n'
p.feed(h)