from urllib import request
from bs4 import BeautifulSoup

def getcontents():
    url = "https://finance.naver.com/item/main.nhn?code=005930"
    html = request.urlopen(url)
    content = BeautifulSoup(html, 'html.parser')

    return content

contents = getcontents()

no_today = contents.find('p',{'class':'no_today'})
print(no_today.text)

price = no_today.find('span',{'class':'blind'}) # blind는 html 웹 요소창에 표시 x
# print(price)
print("삼성 전자 주가 : {}원".format(price.text))
