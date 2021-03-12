from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
import time
import re
import random

webdriver_options = webdriver.ChromeOptions()
webdriver_options .add_argument('headless')
webdriver_options.add_argument("user-agent= Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15")
driver = '/Users/kim/Desktop/dgaja/chromedriver'
driver = webdriver.Chrome(driver, options=webdriver_options )
time.sleep(random.uniform(3,5))

#갤러리관련임------------------------------------------------------
#글넘버 스크랩
def dcin_page(a):
    gall_p = []
    driver.get(a)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(random.uniform(3,10))
    data = soup.find_all("td", {"gall_num"})
    #텍스트
    for i in data:
        gall_p.append(i.text)
    return gall_p

#갤러리 글 내용 스크랩
def news_head(link, tag, class1, option):
    text = []
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(random.uniform(3,10))
    if option == '':
        data_1 = soup.find_all(f"{tag}", {f"{class1}"})
    else:
        data_1 = soup.find(f"{tag}", {f"{class1}"}).find_all(f"{option}")
    #텍스트화
    for i in data_1:
        text.append(i.text)
    return text

#갤러리 글 내용 스크랩
def clean(list_name):
    clean_0 = []
    list_name.remove("dc official App", "")
    for i in list_name:
        text = re.sub('[^a-zA-Z]',' ',i).strip()
        if(text != ''):
            clean_0.append(text)
    return clean_0

#/n 추출하기
def clean_n(list_name):
    clean_1 = []
    for j in list_name:
        clean_1.append(j.replace("\n", "").replace("\t", "").strip())
    clean_1 = list(filter(None, clean_1))
    return clean_1


#페이지 반복 횟수 page->스타트숫자
def page_count(page, numbers):
    page_num = []
    for i in range(numbers):
        i = i + 1
        page = page + 1
        page_num.append(page)
        if i == numbers:
            break;
    return page_num

#사이트 텍스트 추출 반
def text_index(page, text_list, html_1):
    kk = []
    for h in page:
        hh='{}{}'.format(html_1, h)
        kk.append(dcin_text(hh))
        text_list = sum(kk, [])
    return text_list
#갤러리관련임------------------------------------------------------


"""
resp = requests.get("https://gall.dcinside.com/mgallery/board/view/?id=tenbagger&no=3015136")
soup_1 = BeautifulSoup(resp.text, 'html.parser')
data_1 = soup_1.find("div", {"write_div"}).all('div')  # 타이틀(제목)을 가지고 있는 클래스 명
print(data_1)
"""
"""
#스크래핑과정(해주갤)
for k in tenbagger_p[9:20]:
    resp = requests.get(f"https://gall.dcinside.com/mgallery/board/view/?id=tenbagger&no=+'{k}'")
    soup = BeautifulSoup(resp.text, 'html.parser')
    data = soup.find_all("div", {"write_div"})  # 타이틀(제목)을 가지고 있는 클래스 명
    print(data)
"""
#print("https://gall.dcinside.com/mgallery/board/view/?id=tenbagger&no="+kk[9])

