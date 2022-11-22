import vectorbt as vbt

dados=vbt.BinanceData.download('BTCBRL',start='2022-01-01', interval='4h').get()

prices = dados['Close']

media_rapida = vbt.MA.run(prices, 8)
media_lenta = vbt.MA.run(prices, 25)

entradas=media_rapida.ma_above(media_lenta)
saídas=media_rapida.ma_below(media_lenta)

pf = vbt.Portfolio.from_signals(prices, entradas, saídas)

pf.plot().show()

pf.stats()
