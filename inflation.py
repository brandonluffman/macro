import tradingeconomics as te
te.login('Your_Key:Your_Secret')
data = te.getHistoricalData(country='United States', indicator='Inflation Rate', initDate='2015-01-01')
print(data)