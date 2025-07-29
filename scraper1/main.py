import cloudscraper
from bs4 import BeautifulSoup

all_jobs = []
scraper = cloudscraper.create_scraper()
url = "https://www.jobkorea.co.kr/Search?duty=1000230%2C1000231&tabType=recruit&Page_No=1&local=I000"


def scrap_jobs(url):
  response = scraper.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find("main", id="main").find_all(
      "div",
      class_=
      "Flex_display_flex__i0l0hl2 Flex_gap_space24__i0l0hlp styles_py_space28__dk46ts8f styles_px_space20__dk46ts2k"
  )

  for job in jobs:
    link = job.find("a")["href"]
    company = job.find("span",
                       class_="Typography_variant_size16__344nw26").text
    title = job.find("span", class_="Typography_variant_size18__344nw25").text
    etc = job.find(
        "div",
        class_=
        "Flex_display_flex__i0l0hl2 Flex_gap_space16__i0l0hlj Flex_direction_row__i0l0hl3"
    )

    area = etc.find_all(
        "span", class_="Typography_variant_size14__344nw27")[-2]
    deadLine = etc.find_all(
        "span", class_="Typography_variant_size14__344nw27")[-1]

    job_data = {
        "title": title,
        "company": company,
        "deadLine": deadLine.text,
        "area": area.text,
        "link": link
    }

    all_jobs.append(job_data)
    # print(all_jobs)


def get_pages(url):
  response = scraper.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  page_no = len(
      soup.find("nav").find_all(
          "li",
          class_=
          "Flex_display_flex__i0l0hl2 Flex_align_center__i0l0hl8 Flex_justify_center__i0l0hld"
      ))

  # Next 버튼이 있으면
  return page_no


total_pages = get_pages(url)

for x in range(total_pages):
  url = f"https://www.jobkorea.co.kr/Search?duty=1000230%2C1000231&tabType=recruit&Page_No={x+1}&local=I000"
  print(f"Scraping jobs...{x}/{total_pages}")
  print(f"url...{url}")
  scrap_jobs(url)

print(len(all_jobs))
