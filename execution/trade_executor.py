# import ccxt
# from config.settings import API_KEY, SECRET_KEY, SYMBOL, TRADE_SIZE

# exchange = ccxt.delta({
#     "apiKey": API_KEY,
#     "secret": SECRET_KEY,
# })

# def place_trade(signal):

#     if signal == "BUY":

#         order = exchange.create_market_buy_order(
#             SYMBOL,
#             TRADE_SIZE
#         )

#     elif signal == "SELL":

#         order = exchange.create_market_sell_order(
#             SYMBOL,
#             TRADE_SIZE
#         )

#     else:
#         return None

#     return order
def place_trade(signal):

    if signal:
        print(f"Simulated {signal} trade executed")

    return None