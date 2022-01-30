import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pyEX as p

df = pd.read_csv('csv loaction')
print(df)
df = df[['close']]
df.reset_index(level=0, inplace=True)
df.columns = ['ds', 'y']
print(df)

#ploting madc

plt.plot(df.ds, df.y, label='Infy_close')
exp1 = df.y.ewm(span=12, adjust=False).mean()
exp2 = df.y.ewm(span=26, adjust=False).mean()
macd = exp1 - exp2
exp3 = macd.ewm(span=9, adjust=False).mean()
print(exp3)
plt.plot(df.ds, macd, label='MACD_LINE', color='#EBD2BE')
plt.plot(df.ds, exp3, label='Signal_Line', color='#E5A4CB')
plt.legend(loc='center right')
plt.show()
