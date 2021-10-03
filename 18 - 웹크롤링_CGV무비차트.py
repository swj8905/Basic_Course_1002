import urllib.request as req
from bs4 import BeautifulSoup

code = req.urlopen("http://www.cgv.co.kr/movies/")
# print(code.read())

# HTML 코드 이쁘게 정리하기
soup = BeautifulSoup(code, "html.parser")
# print(soup)

# 내가 원하는 요소 가져오게 하기
# title = soup.select_one("strong.title")
title = soup.select("div.sect-movie-chart strong.title")

# 요소 내용 출력하기
# print(title.string)
f = open("./무비차트.txt", "w") # w 모드 : 쓰기모드
for i in title:
    print(i.string)
    f.write(i.string + "\n")
f.close()
