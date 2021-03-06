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
        <li>수학</li>
        <li>국어</li>
        <li>영어</li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html_str,'html.parser')
# print(soup)
ul = soup.find('ul') # find() 는 맨 처음 나오는 태그만 검색
# print(ul)
# print(soup.find('li'))
print(ul.text) # ul에서 추출 ,태그를 빼고 검색
