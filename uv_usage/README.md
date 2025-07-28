# python
```
choco install python3
```

# uv

## uv 설치

```
choco install uv
```

## 라이브러리 설치
- Update the project's environment
```
uv sync
```

## 실행
```
uv run main.py
```


## 참고
### uv 프로젝트 새로 만들기
- pyproject.toml가 생성된다. 
```
uv init
```

### 의존선 추가하기
```
uv add packagename
```