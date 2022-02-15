from sqlalchemy import create_engine
import pandas as pd
df = pd.read_csv('data.csv')
print(df)
# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="pw",
                               db="darabase name"))
# Insert whole DataFrame into MySQL
df.to_sql('data_set2', con=engine, if_exists='append', chunksize=100000, index=False)
print(df.to_sql)