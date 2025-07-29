# python
```
choco install python3
```

# uv

## 1. uv 설치
- 전역으로 설치하면 최초 1회만 설치하면 된다.

```
choco install uv
```

## 2. uv 프로젝트 만들기
- 아래 기본 파일이 생성된다. 
  - .python-version: 파이썬 버전
  - main.py: 실행파일
  - pyproject.toml: 프로젝트 정보 + 라이브러리 정보
  - README.md

```
uv init
```

## 3. 라이브러리 설치
- Update the project's environment
- .venv폴더, uv.lock 생성
- 레파지토리를 로컬에 클론해 새로 설치 할때 여기서부터 시작
- 기존 레파지토리라면 pyproject.toml의 dependencies 정보를 참조해 라이브러리를 로컬에 설치한다. 

```
uv sync
```

### 4. 라이브러리(의존성) 추가하기
- 추가가 필요한 경우
- pyproject.toml의 dependencies에 정보가 추가된다. 

```
uv add packagename
```


## 파일 실행
```
uv run main.py
```
