def calculate_levels(entry_price, side):

    sl_percent = 0.01
    tp_percent = 0.02

    if side == "BUY":

        stop_loss = entry_price * (1 - sl_percent)
        take_profit = entry_price * (1 + tp_percent)

    else:

        stop_loss = entry_price * (1 + sl_percent)
        take_profit = entry_price * (1 - tp_percent)

    return stop_loss, take_profit