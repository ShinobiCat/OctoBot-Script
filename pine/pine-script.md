The provided Pine Script code is organized by grouping related code, logic, and TradingView inputs under the following sections:

CONFIGURATION
- Example: `//@version=6`
- Example: `indicator("My Script", overlay=true)`
- Example: `input int length = 14`

INDICATORS
- Momentum-based: RSI, MACD, Stochastic, etc.
  - Example: `rsi = ta.rsi(close, length)`
  - Example: `macd = ta.macd(close, 12, 26, 9)`
  - Example: `stoch = ta.stoch(close, high, low, length)`

- Volume-based: Order Flow, OBV, VWAP deviations.
  - Example: `obv = ta.obv(close, volume)`
  - Example: `vwap = ta.vwap(close, volume)`
  - Example: `orderFlow = ta.cum(close * volume)`

- Trend confirmation: Moving Averages, ADX, Supertrend.
  - Example: `ma = ta.sma(close, length)`
  - Example: `adx = ta.adx(length)`
  - Example: `supertrend = ta.supertrend(close, length)`

- Noise reduction: ATR filter, Bollinger Bands compression.
  - Example: `atr = ta.atr(length)`
  - Example: `bb = ta.bbands(close, length, 2)`
  - Example: `atrFilter = ta.atr(close, length)`

- Time filters: Trading hours, volatility windows.
  - Example: `tradingHours = (hour >= 9 and hour <= 16)`
  - Example: `volatilityWindow = ta.volatility(close, length)`
  - Example: `timeFilter = (hour >= 9 and hour <= 16)`

LIQUIDITY & SPREAD ANALYSIS
- Example: `spread = ask - bid`
- Example: `liquidity = volume / spread`
- Example: `avgSpread = ta.sma(spread, length)`

ENTRY CONDITIONS
- Example: `longCondition = crossover(sma, ema)`
- Example: `shortCondition = crossunder(sma, ema)`
- Example: `buySignal = ta.crossover(rsi, 30)`

EXIT CONDITIONS
- Example: `exitLong = crossunder(sma, ema)`
- Example: `exitShort = crossover(sma, ema)`
- Example: `sellSignal = ta.crossunder(rsi, 70)`

EXECUTION & ALERTS
- Example: `strategy.entry("Long", strategy.long, when=longCondition)`
- Example: `strategy.close("Long", when=exitLong)`
- Example: `alert("Buy Signal", alert.freq_once_per_bar_close)`

PLOTTING
- Example: `plot(sma, color=color.blue)`
- Example: `plot(ema, color=color.red)`
- Example: `plotshape(series=buySignal, location=location.belowbar, color=color.green)`