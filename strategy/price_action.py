def detect_signal(df):

    last = df.iloc[-1]
    prev = df.iloc[-2]

    recent_high = df['high'].tail(20).max()
    recent_low = df['low'].tail(20).min()

    signal = None

    # LONG SETUP
    if last['low'] < recent_low and last['close'] > prev['high']:
        signal = "BUY"

    # SHORT SETUP
    elif last['high'] > recent_high and last['close'] < prev['low']:
        signal = "SELL"

    return signal