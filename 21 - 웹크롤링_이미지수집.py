from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par
import os

if not os.path.exists("./이미지수집"):
    os.mkdir("./이미지수집")

keyword = input("키워드 입력 >> ")
if not os.path.exists(f"./이미지수집/{keyword}"):
    os.mkdir(f"./이미지수집/{keyword}")

encoded = par.quote(keyword) # 한글 --> 특수한 문자열
code = req.urlopen(f"https://images.search.yahoo.com/search/images;_ylt=Awr9Imss6mBh3F8AdDFXNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p={encoded}&fr2=piv-web&fr=yfp-t")
soup = BeautifulSoup(code, "html.parser")
img = soup.select("a.img > img")
cnt = 1
for i in img:
    img_url = i.attrs["data-src"]
    req.urlretrieve(img_url, f"./이미지수집/{keyword}/{cnt}.png")
    print(f"{keyword} 이미지 수집 완료 {cnt}")
    cnt += 1