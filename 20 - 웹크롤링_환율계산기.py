from bs4 import BeautifulSoup
import urllib.request as req

print("==== 국가 선택 ====")
print("1. 미국")
print("2. 일본")
print("3. 유럽")
print("4. 중국")
menu = int(input("선택 >> "))
unit = ["달러", "엔", "유로", "위안"]
user_price = int(input("금액 입력(단위 : {}) >> ".format(unit[menu-1])))
if menu == 2:
    # user_price = user_price / 100
    user_price /= 100
code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code, "html.parser")
price = soup.select("span.value")
print("환전 결과 : {} 원".format(float(price[menu-1].string.replace(",", "")) * user_price) )