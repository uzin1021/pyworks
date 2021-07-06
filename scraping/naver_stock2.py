from urllib import request
from bs4 import BeautifulSoup

# 변수지정해 여러종목 만들기
def getcontent(item_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + item_code
    html = request.urlopen(url)
    content = BeautifulSoup(html, 'html.parser')

    return content
def getprice(item_code):
    content = getcontent(item_code)
    no_today = content.find('p',{'class':'no_today'})
    price = no_today.find('span', {'class':'blind'})
    return price
# 삼성전자 - 005930, 카카오 - 035720, 네이버 - 035420
삼성전자 = getprice("005930")
카카오 = getprice("035720")
네이버 = getprice("035420")

print("삼성전자 : {}원".format(삼성전자.text))
print("카카오 : {}원".format(카카오.text))
print("네이버 : {}원".format(네이버.text))

'''
no_today = contents.find('p',{'class':'no_today'})
print(no_today.text)

price = no_today.find('span',{'class':'blind'}) # blind는 html 웹 요소창에 표시 x
# print(price)
print("삼성 전자 주가 : {}원".format(price.text))
'''