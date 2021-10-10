from selenium import webdriver
import chromedriver_autoinstaller
import time

hash_tag = input("해시태그 입력 >> ")
cp = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(cp)
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
# 로그인 하기
id = browser.find_element_by_name("username")
id.send_keys("tutor_pyson") # 본인 계정 써주세요
pw = browser.find_element_by_name("password")
pw.send_keys("q1w2e3r4!@#$") # 본인 계정 써주세요
button = browser.find_element_by_css_selector("div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB")
button.click()
time.sleep(5)
# 해시태그 검색
url = "https://www.instagram.com/explore/tags/" + hash_tag
browser.get(url)
time.sleep(5)
# 첫번째 사진 클릭
first_photo = browser.find_element_by_css_selector("div._9AhH0")
first_photo.click()
time.sleep(4)
while True:
    like = browser.find_element_by_css_selector("section.ltpMr.Slqrh svg._8-yf5")
    value = like.get_attribute("aria-label")
    next = browser.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow")
    if value == "좋아요": # 좋아요가 안눌려있다면?
        like.click()
        time.sleep(30)
        next.click()
        time.sleep(30)
    elif value == "좋아요 취소": # 좋아요가 눌려있다면?
        next.click()
        time.sleep(30)