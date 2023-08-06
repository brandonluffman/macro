import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from fastapi import FastAPI, Depends, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import mysql.connector
import mysql.connector.pooling
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
import os
import json
import yfinance as yf
from yahooquery import Ticker
import openai


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