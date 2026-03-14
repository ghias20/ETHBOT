import time

from data.fetch_data import get_candles
from strategy.price_action import detect_signal
from execution.trade_executor import place_trade
from utils.logger import log
from utils.telegram import send_message

def run_bot():

    log("Bot Started")

    while True:

        df = get_candles()

        signal = detect_signal(df)

        log(f"Signal detected: {signal}")

        if signal:
            message=f"""
            Signal: {signal}
            Symbol: {df['symbol'].iloc[-1]}
            Time: {df['time'].iloc[-1]}
            Price: {df['close'].iloc[-1]}"""
            send_message(message)
            order = place_trade(signal)

            log(f"Order executed: {order}")
            send_message(f"Trade Executed: {signal}")
        time.sleep(30)

if __name__ == "__main__":
    run_bot()