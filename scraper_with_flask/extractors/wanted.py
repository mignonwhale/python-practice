from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time


def extract_wanted_jobs(keyword):
  p = sync_playwright().start()
  browser = p.chromium.launch(headless=False)
  page = browser.new_page()
  page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")

  for x in range(5):
    time.sleep(3)
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

  # print(all_jobs)
  print("total_count:::", len(all_jobs))

  return all_jobs