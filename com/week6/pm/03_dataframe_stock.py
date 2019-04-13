import pandas as pd

from pandas import DataFrame

data = {'name': ['Samsung', 'SK', 'Hyundai Mortor'],
       'open': [46050, 267500, 127000],
       'high':[46850, 265500, 128000]}
stock_frame = DataFrame(data)

print(stock_frame)