import ccxt
import pandas as pd
from config.settings import API_KEY, SECRET_KEY, SYMBOL, TIMEFRAME

exchange = ccxt.delta({
    "apiKey": API_KEY,
    "secret": SECRET_KEY,
    "enableRateLimit": True
})

def get_candles(limit=100):

    candles = exchange.fetch_ohlcv(
        SYMBOL,
        timeframe=TIMEFRAME,
        limit=limit
    )

    df = pd.DataFrame(
        candles,
        columns=["time","open","high","low","close","volume"]
    )

    return df