import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("DELTA_API_KEY")
SECRET_KEY = os.getenv("DELTA_SECRET_KEY")

SYMBOL = "BTC/USDT"
TIMEFRAME = "15m"

LEVERAGE = 15

RISK_PER_TRADE = 0.02
STOP_LOSS_PERCENT = 0.01
TAKE_PROFIT_PERCENT = 0.02

TRADE_SIZE = 0.001