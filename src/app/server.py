from fastapi import FastAPI
from acquisition.news_acquisition_service import acquisition_news

app = FastAPI()


@app.get("/news_acquisition/latest_news")
def get_latest_news():
    news = acquisition_news.get_latest_hydrogen_news()
    return news
