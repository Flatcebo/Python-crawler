# pip install requests && beautifulsoup
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'http://jowhang.dinak.co.kr/%EC%A0%90%EC%A3%BC%EC%84%A0%EC%9E%A5%EC%A1%B0%ED%99%A9/list?sYear=2020&tmp=1'
detailUrl = 'http://jowhang.dinak.co.kr/%EC%A0%90%EC%A3%BC%EC%84%A0%EC%9E%A5%EC%A1%B0%ED%99%A9/list?sYear=2020&tmp=1'

response = requests.get(url)
detailResponse = requests.get(detailUrl)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
ul = soup.select_one('.maincontents')
urls = []

# 제목
# titles = ul.select(".contents-wrapper tbody td.subject a")
# for title in titles:
#     print(title.get_text())
# # 업체명
# userNames = ul.select(".contents-wrapper tbody td.writer.member span")
# for userName in userNames:
#     print(userName.get_text())
# 주소
subjects = ul.select(".contents-wrapper table tbody td.subject a")
for subject in subjects:
    print(subject.attrs['href'])
    urls.append(subject.attrs['href'])
# 게시일
# uploadAts = ul.select(".contents-wrapper tbody td.date")
# for uploadAt in uploadAts:
#     print(uploadAt.get_text())
# # 유저 아이디
# userIds = ul.select(".contents-wrapper tbody td.writer.member span")
# for userId in userIds:
#     print(userId.attrs["onclick"].split(', ')[3].strip().strip("'"))
# # 지역
# regions = ul.select(".contents-wrapper tbody td.region span")
# for region in regions:
#     print(region.get_text())
# # 글번호
# listNumbs = ul.select(".contents-wrapper tbody td.no")
# for listNumb in listNumbs:
#     print(listNumb.get_text())
# # 타입
# types = ul.select(".contents-wrapper tbody td.type .typeicon")
# for type in types:
#     print(type.get_text())

    

visited_urls = set()
# url = "http://jowhang.dinak.co.kr/%EC%A0%90%EC%A3%BC%EC%84%A0%EC%9E%A5%EC%A1%B0%ED%99%A9"
# url = "http://jowhang.dinak.co.kr/%EC%A0%90%EC%A3%BC%EC%84%A0%EC%9E%A5%EC%A1%B0%ED%99%A9"

def crawl_page(url,urls):
    global visited_urls

    if url in visited_urls:
        return

    visited_urls.add(url)

    print(f"Crawling: {url}")

    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            # 원하는 데이터 추출 또는 처리
            # 예를 들어, 해당 페이지의 제목 출력
            # title = soup.title.string
            # print(f"Page Title: {title}")
            # print(soup.select("td.subject a",href=True))

            # 페이지의 모든 링크를 가져와서 재귀적으로 크롤링
            # count = 0
            # links = soup.select("td.subject a", href=True)
            # for link in links:
            #     # count += 1
            #     next_url = urljoin(url, link['href'])
            #     urls.append(next_url)
            #     crawl_page(next_url, urls)
            # print("count =", count)

                

    except Exception as e:
        print(f"Error crawling {url}: {e}" )



        # detailPhoneNumber:
#         (detailDesc as any).text().trim().replace(/\D/g, "|") ?? "",
#  const regex: any =
#       /(?=.)(?:02|0[13-9]{1}[0-9]{1})[^0-9]*[0-9]{3,4}[^0-9]*[0-9]{4}/g;
#     let result: any = regex.exec(detailItems.detailDesc);
#     let results: any = [];
#     while (result != null) {
#       results.push(result[0]);
#       console.log("phone =>", result[0]);
#       result = regex.exec(detailItems.detailDesc);
#     }



if __name__ == "__main__":
    # start_url = urls  # 크롤링을 시작할 URL 설정
    # crawl_page(start_url)
    for url in urls:
        crawl_page(url, urls)
