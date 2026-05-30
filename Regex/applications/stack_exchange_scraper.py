import re

html = ''
while True:
    try:
        html += input() + '\n'
    except EOFError:
        break

pattern = re.compile(
    r'question-summary-(\d+).*?'
    r'class="question-hyperlink">(.*?)</a>.*?'
    r'class="relativetime">(.*?)</span>',
    re.DOTALL
)

for qid, title, time in pattern.findall(html):
    print(f'{qid};{title};{time}')