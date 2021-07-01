# 웹 스크래이핑(크롤링)

from urllib import request
url = "http://www.naver.com"
content = request.urlopen(url) # url 대신 주소바로 입력해도됨.
print(content.read())