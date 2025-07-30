# flask를 이용해 job scraper를 만들자

## flask 설치

```
uv add flask
```


### 참고 
- vscode에서 flask가 설치되지 않았다고 나온다면 아래 처리
- ctrl+P (명령어 팔렛) > `Python:Select Interpreter` > `Enter interpreter paht...` > 윈도우파일편지기에서 `.venv\Scripts\python.exe` 선택

- uv가 만든 `.venv`환경을 선택해 줘야 vscode가 똑바로 가상환경을 활성화시킨다.


## pico 설치
- css 라이브러리
- API: [https://picocss.com/docs](https://picocss.com/docs)

`<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
>`