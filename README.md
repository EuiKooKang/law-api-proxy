
# 국가법령정보 프록시 API

이 프로젝트는 open.law.go.kr의 XML 기반 API를 GPTs 및 사용자에게 JSON으로 변환해주는 프록시 서버입니다.

## 주요 경로

- `/getLawName?query=민법` → 법령명 검색
- `/getLawDetail?law_id=JO2020154` → 조문 상세 검색

## 실행

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 10000
```

## 배포 예시

Render.com에서 Web Service로 등록:
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`
