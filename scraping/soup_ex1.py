# BeautifulSoup 모듈 사용하기
from bs4 import BeautifulSoup

html_str="""
<html>
<body>
    <ul class ="item">
        <li>인공지능</li>
        <li>빅데이터</li>
        <li>로봇</li>
    </ul>
    <ul class ="lang">
        <li>영어</li>
        <li>중국어</li>
        <li>과학</li>
    </ul>
</body>
</html>
"""

contents = BeautifulSoup(html_str, "html.parser")
ul = contents.find('ul', {'class':'lang'})

# print(ul)
# li = ul.find('li')
# print(li) # 맨위 리스트만 검색
# 중국어 검색 방법1
lis = ul.find_all('li')
print(lis)
print(lis[1].text)
