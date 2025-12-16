# app.py
from fastapi import FastAPI, Query
from typing import List, Literal

from scrape_horoscope import get_horoscope, get_all_daily

app = FastAPI(title="Horoscope Scraper API")


@app.get("/")
def root():
    return {"message": "Horoscope Scraper API is running"}


@app.get("/horoscope")
def horoscope(
    sign: str = Query("aries", description="zodiac sign, e.g. aries, taurus"),
    period: Literal["daily", "weekly", "monthly"] = Query("daily")
):
    """
    Return single horoscope as JSON.
    """
    data = get_horoscope(sign, period)
    return data


@app.get("/daily-all")
def daily_all():
    """
    Return all 12 signs daily horoscope as JSON list.
    """
    return get_all_daily()
