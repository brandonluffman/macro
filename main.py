import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
import yfinance as yf

app = FastAPI()
origins = ["*"]

port = int(os.environ.get("PORT", 5000))


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
        return current_price
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