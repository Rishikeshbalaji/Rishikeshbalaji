import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# reading csv using pandas


df = pd.read_csv('csv Location')
print(df)


# Bollinger band


# Calculating 30 days moving average
df['30_MA_Close'] = df.close.rolling(window=30).mean()
# calculating 20 days rolling standard devtaion
df['20_std_Close'] = df.close.rolling(window=20).std()
df['upper'] = df['30_MA_Close'] + (2 * df['20_std_Close'])
df['lower'] = df['30_MA_Close'] - (2 * df['20_std_Close'])
print(df)


# plotting Bollinger bands


df[['close', 'upper', 'lower', '30_MA_Close']].plot(figsize=(30, 30))
plt.xlabel('DATE')
plt.ylabel('Bollinger_Bands')
df = df[['close']]
df.reset_index(level=0, inplace=True)
df.columns = ['ds', 'y']
print(df)

# plotting madc

# plt.plot(df.ds, df.y, label='Infy_close')
exp1 = df.y.ewm(span=12, adjust=False).mean()
exp2 = df.y.ewm(span=26, adjust=False).mean()
macd = exp1 - exp2
exp3 = macd.ewm(span=9, adjust=False).mean()
print(exp3)
plt.plot(df.ds, macd, label='MACD_LINE', color='#EBD2BE')
plt.plot(df.ds, exp3, label='Signal_Line', color='#E5A4CB')
plt.legend(loc='center right')

# showing graph

plt.show()
