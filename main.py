# pip install requests && beautifulsoup
import requests
import time
import asyncio
import re
import pymysql
from bs4 import BeautifulSoup
from urllib.parse import urljoin


connection = pymysql.connect(
    host='192.168.0.37',  
    port=3306,  
    user='localDB',
    password='flatcebo',
    db='crawling',  
    charset='utf8'
)

cur = connection.cursor()



def crawl_list(url) :

    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('.maincontents')
    # urls = []

    # 제목
    arr = []
    titles = ul.select(".contents-wrapper tbody td.subject a")
    for title in titles:
        title.get_text()
    # 업체명
    userNames = ul.select(".contents-wrapper tbody td.writer.member span")
    for userName in userNames:
        userName.get_text()
    # 주소
    subjects = ul.select(".contents-wrapper table tbody td.subject a")
    for subject in subjects:
        subject.attrs['href']
        # urls.append(subject.attrs['href'])
    # 게시일
    uploadAts = ul.select(".contents-wrapper tbody td.date")
    for uploadAt in uploadAts:
        uploadAt.get_text()
    # 유저 아이디
    userIds = ul.select(".contents-wrapper tbody td.writer.member span")
    for userId in userIds:
        userId.attrs["onclick"].split(', ')[3].strip().strip("'")
    # 지역
    regions = ul.select(".contents-wrapper tbody td.region span")
    for region in regions:
        region.get_text()
    # 글번호
    listNumbs = ul.select(".contents-wrapper tbody td.no")
    for listNumb in listNumbs:
        listNumb.get_text()
    # 타입
    types = ul.select(".contents-wrapper tbody td.type .typeicon")
    for type in types:
        type.get_text()

    for i in range(len(subjects)):
        arr.append({
            "title":titles[i].get_text(),
            "userName": userNames[i].get_text(),
            "subject": subjects[i].attrs['href'],
            "uploadAt": uploadAts[i].get_text(),
            "userId":userIds[i].attrs["onclick"].split(', ')[3].strip().strip("'"),
            "region": regions[i].get_text(),
            "listNumb":listNumbs[i].get_text(),
            "type": types[i].get_text()
        })

    return arr

def crawl_next(url) :
    # global visited_urls
    # visited_urls = set()

    # if url in visited_urls:
    #     return

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('.contents')
    count = 0
    links = soup.select("td.subject a", href=True)
    for link in links:
        if count == 1:
            break
        next_url = urljoin(print("joinUrl ===>",url),print("link =>",link['href']))
        count += 1


        # 상세글
        detailDescs = ul
        for detailDesc in detailDescs : 
            detailDesc

        # 상세 이미지
        detailImgs = ul.select('img')
        for detailImg in detailImgs :
            detailImg.attrs['src']
        
        # 상세 번호
        detailNumbs = ul
        for detailNumb in detailNumbs :
            regexNumb = detailNumb.get_text()
            pattern = re.compile(r'(?=.)(?:010)[^0-9]*[0-9]{3,4}[^0-9]*[0-9]{4}')
            results = pattern.findall(regexNumb)

            for result in results:
                print(result)
try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO users (username) VALUES (%s)"
        data = ('dd')
        cursor.execute(sql, data)
    connection.commit()
finally:
    connection.close()



if __name__ == "__main__":
    url = "http://jowhang.dinak.co.kr/%EC%A0%90%EC%A3%BC%EC%84%A0%EC%9E%A5%EC%A1%B0%ED%99%A9/list?sYear=2020&tmp=1"
    page = 1
    totalPages = 2
    delayInMilliseconds = 3
    arr = []
    while True:
        if page >= totalPages:
            print("break")
            break
       
        print("페이지 번호 =>", page)
        pages = f"&page={page}"
        arr += crawl_list(url + pages)

        page += 1

        time.sleep(delayInMilliseconds)

    for item in arr:
        crawl_next(item["subject"])