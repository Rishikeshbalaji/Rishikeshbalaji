import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv location')
print(df)
# Calculating 30 days moving average
df['30_MA_Close'] = df.close.rolling(window=30).mean()
# calculating 20 days rolling standard devtaion
df['20_std_Close'] = df.close.rolling(window=20).std()
df['upper'] = df['30_MA_Close'] + (2 * df['20_std_Close'])
df['lower'] = df['30_MA_Close'] - (2 * df['20_std_Close'])
print(df)
df[['close', 'upper', 'lower', '30_MA_Close']].plot(figsize=(30, 30))
plt.xlabel('DATE')
plt.ylabel('Bollinger_Bands')

plt.show()
