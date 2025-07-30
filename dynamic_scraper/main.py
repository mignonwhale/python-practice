from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv

# 이벤트로 페이지 내 정보 추출
def scrap_jobs_by_event(keyword):
  p = sync_playwright().start()
  browser = p.chromium.launch(headless=False)
  page = browser.new_page()

  page.goto("https://www.wanted.co.kr/")
  time.sleep(2)
  # page.screenshot(path="screenshot.png")

  page.click("button[aria-label='검색']")
  time.sleep(2)

  page.fill("input[type='search']", keyword)
  # page.get_by_placeholder('검색어를 입력해 주세요.').fill('python')
  time.sleep(2)

  page.keyboard.down('Enter')
  time.sleep(2)


  page.click("a#search_tab_position")
  # page.click("a[id='search_tab_position']")
  time.sleep(2)

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

# url로 페이지 내 정보 추출
def scrap_jobs_by_url(keyword):
  p = sync_playwright().start()
  browser = p.chromium.launch(headless=False)
  page = browser.new_page()
  page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")

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
    position = content.find('strong').text
    company = content.find_all("span")[0].text
    xp = content.find_all("span")[1].text

    job_data = {
      "position": position,
      "company": company,
      "xp": xp,
      "link": link,
    }
    all_jobs.append(job_data)

  print(all_jobs)
  print("total_count:::", len(all_jobs))

  return all_jobs

# csv 만들기
def save_job_file(file_name, jobs):
  file = open(file_name, "w", encoding="utf-8")
  writter = csv.writer(file)
  writter.writerow(["title", "company", "xp", "link"])

  for job in jobs:
    writter.writerow(job.values())

  file.close()

jobs = scrap_jobs_by_url("react")
save_job_file("jobs.csv", jobs)

