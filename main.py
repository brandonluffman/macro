import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
import yfinance as yf

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/current_price/{ticker}")
async def get_current_price(ticker: str):
    try:
        stock_data = yf.Ticker(ticker)
        current_price = stock_data.info["currentPrice"]
        open_price = stock_data.info['open']
        daily_change = current_price-open_price
        percent_change = (daily_change/open_price) * 100
        return current_price,daily_change, percent_change
    except Exception as e:
        print(f"Error: {e}")
        return None


@app.get("/current_price/{ticker}")
async def get_current_price(ticker: str):
    try:
        stock_data = yf.Ticker(ticker)
        current_price = stock_data.info["currentPrice"]
        return current_price
    except Exception as e:
        print(f"Error: {e}")
        return None