# pip install requests && beautifulsoup


import requests
from bs4 import BeautifulSoup

url = 'https://www.innak.kr/bbs/board.php?bo_table=D02_2022'
detailUrl = 'https://www.innak.kr/bbs/board.php?bo_table=D02_2022'

response = requests.get(url)
detailResponse = requests.get(detailUrl)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.list-body')
    
    # 제목
    titles = ul.select("#list-body > .list-item div.wr-subject > a")
    for title in titles:
        print(title.get_text())
    # 업체명
    userNames = ul.select("#list-body > .list-item:not(.bg-light) div.wr-subject a .member")
    for userName in userNames:
        print(userName.get_text())
    # 주소
    subjects = ul.select("#list-body > .list-item:not(.bg-light) div.wr-subject a.item-subject")
    for subject in subjects:
        print(subject.attrs['href'])
    # 게시일
    uploadAts = ul.select("#list-body > .list-item:not(.bg-light) div.wr-date")
    for uploadAt in uploadAts:
        print(uploadAt.get_text())
    # 유저 아이디
    userIds = ul.select("#list-body > .list-item:not(.bg-light) div.wr-name a")
   
    for userId in userIds:
        print(userId.attrs["onclick"].split(', ')[1].strip().strip("'"))
        
    descs = ul.select("#")
    for desc in descs:
        print(desc.get_text())
        
        
        
        
else : 
    print(response.status_code)
    
    
