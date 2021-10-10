from selenium import webdriver
import time
import chromedriver_autoinstaller

chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
id = browser.find_element_by_css_selector("#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)
browser.get("http://cafe.daum.net/talingpython")
time.sleep(3)
# 중고나라 게시판 클릭
browser.switch_to.frame("down")
browser.find_element_by_css_selector("#fldlink_rRa6_347").click()
time.sleep(3)

# 메모장에 있는 문자열들 읽어옴.
try:
    f = open("./중고나라.txt","r") #r 모드 : 읽기모드
    ref = f.readlines() # 반환값 : 리스트자료형
except:
    f = open("./중고나라.txt","w") # "w"모드로 파일을 open하면 존재하지 않는 파일 자동 생성
    ref = []


# 게시글 제목 크롤링
title = browser.find_elements_by_css_selector("a.txt_item")
new_one = 0
for i in title:
    if (i.text+"\n") not in ref: #i.text가 최신 글이라면?
        f = open("./중고나라.txt","a") # "a" 모드 : 더해서 쓰기 모드
        f.write(i.text + "\n") # write()함수 쓸때, 개행문자는 직접 더해주기
        f.close()
        if "키보드" in i.text:
            new_one += 1

print(f"키보드 관련 글이 {new_one}개 올라왔습니다.")
browser.close()

if new_one >= 1:
    from twilio.rest import Client

    account_sid = "AC9cd90e7dcc1ffa84aef9e0782eb4a15c"
    auth_token = "9b3753bd9bb7ee7503aadb37ad3b5133"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"키보드 관련 글이 {new_one}개 올라왔습니다. https://cafe.daum.net/talingpython/rRa6",
                         from_='+13526493053',
                         to='+821095518905'
                     )
