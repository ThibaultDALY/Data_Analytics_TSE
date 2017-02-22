# Python work friday 23/02/2017
import pandas

data_returns = pandas.read_pickle('Returns.pkl')
print(data_returns)

data_sectors = pandas.read_pickle("Sector.pkl")
data_SPX = pandas.read_pickle("SPX.pkl")
data_strategy = pandas.read_pickle("Strategy.pkl")
