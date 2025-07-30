import csv

def save_to_file(file_name, jobs):

  # vscode로 받아 볼거면 encoding="utf-8" 파람 추가 필요
  # 엑셀로 볼거면 상관없음
  file = open(f"{file_name}.csv", "w") 
  writter = csv.writer(file)
  writter.writerow(["title", "company", "xp", "link"])

  for job in jobs:
    writter.writerow(job.values())

  file.close()
