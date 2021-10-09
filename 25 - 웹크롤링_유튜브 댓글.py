from selenium import webdriver
import time
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys

cp = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(cp)
browser.get("https://www.youtube.com/watch?v=V324pRQbB3I")
time.sleep(5)
# 스크롤 내려서 첫 댓글 생성시키기
browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN) # 스크롤 살짝 내리기 / Keys.END : 스크롤 한번에 끝까지 내리기
time.sleep(5)
comments = browser.find_elements_by_css_selector("#content-text")
idx = 0
while True:
    try:
        print(comments[idx].text)
    except:
        print("-------- 크롤링 끝 ----------")
        break
    idx += 1
    if idx % 20 == 0: # idx 가 20의 배수라면?
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(4)
        comments = browser.find_elements_by_css_selector("#content-text")