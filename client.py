from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv("bot/.env")

def get_binance_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise Exception("API keys not loaded from .env")

    client = Client(
        api_key=api_key,
        api_secret=api_secret,
        testnet=True
    )

    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client
