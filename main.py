
from fastapi import FastAPI, Query
import requests
import xmltodict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/getLawName")
def get_law_name(query: str):
    url = "https://www.law.go.kr/DRF/lawService.do"
    params = {
        "OC": "haemer4",
        "target": "lawName",
        "query": query
    }
    res = requests.get(url, params=params)

    try:
        data = xmltodict.parse(res.content)
        items = data.get("LawList", {}).get("law", [])

        if isinstance(items, list):
            item = items[0]
        else:
            item = items

        return {
            "법령명": item.get("법령명", "알 수 없음"),
            "공포일자": item.get("공포일자", "알 수 없음"),
            "법령ID": item.get("법령ID", "없음")
        }
    except Exception as e:
        return {"error": str(e), "raw": res.text}

@app.get("/getLawDetail")
def get_law_detail(law_id: str):
    url = "https://www.law.go.kr/DRF/lawService.do"
    params = {
        "OC": "haemer4",
        "target": "lawDetail",
        "lawId": law_id
    }
    res = requests.get(url, params=params)

    try:
        data = xmltodict.parse(res.content)
        return data
    except Exception as e:
        return {"error": str(e), "raw": res.text}
