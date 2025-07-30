from flask import Flask, render_template, request, redirect, send_file
from extractors.wanted import extract_wanted_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def search():
  # print(request.args) #ImmutableMultiDict([('keyword', 'python')])
  # 쿼리스크링값 가져오기
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")

  if keyword in db:
    jobs = db[keyword]
  else:
    # job scrapper 호출
    jobs = extract_wanted_jobs(keyword)
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv")

app.run(debug=True) #자동 새로고침
#app.run("0.0.0.0") #서버종료