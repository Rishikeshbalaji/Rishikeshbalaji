import pymysql
import pandas as pd


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="pw",
        db='database name',
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM databse name;")
    output = cur.fetchall()
    df = pd.DataFrame(output)
    print(df)
    # print(output)

    # To close the connection
    conn.close()


# Driver Code
if __name__ == "__main__":
    mysqlconnect()

