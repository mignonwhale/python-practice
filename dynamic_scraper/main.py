from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

# page.goto("https://www.wanted.co.kr/")
# time.sleep(2)
# # page.screenshot(path="screenshot.png")

# page.click("button[aria-label='검색']")
# time.sleep(2)

# page.fill("input[type='search']", "python")
# # page.get_by_placeholder('검색어를 입력해 주세요.').fill('python')
# time.sleep(2)

# page.keyboard.down('Enter')
# time.sleep(2)


# page.click("a#search_tab_position")
# # page.click("a[id='search_tab_position']")
# time.sleep(2)

# 위 로직은 아래처럼 url로 바로 연결해도 됨
page.goto("https://www.wanted.co.kr/search?query=react&tab=position")

for x in range(5):
  time.sleep(5)
  page.keyboard.down('End')

content = page.content()

p.stop()


# html에서 정보 추출
soup = BeautifulSoup(content, "html.parser")
jobs = soup.find("div", id="search_tabpanel_position").find('div', class_='JobList_container__Hf1rb JobList_container--variant-card-grid__HyAWe JobList_container--item-sm-2__4F80w JobList_container--item-md-2__wnQDc JobList_container--item-lg-4__v7c0Y').find_all('div', class_='JobCard_container__zQcZs JobCard_container--variant-card___dlv1')

all_jobs = []
for job in jobs:
  link = f"https://www.wanted.co.kr{job.find("a")["href"]}"
  content = job.find("div", class_="JobCard_content__5Y_uq")
  title = content.find('strong').text
  company = content.find_all("span")[0]
  xp = content.find_all("span")[1]

  job_data = {
    "title": title,
    "company": company.text,
    "xp": xp.text,
    "link": link,
  }

  all_jobs.append(job_data)

print(all_jobs)
print("total_count:::", len(all_jobs))

# csv 만들기
file = open("jobs.csv", "w", encoding="utf-8")
writter = csv.writer(file)
writter.writerow(["title", "company", "xp", "link"])

for job in all_jobs:
  writter.writerow(job.values())