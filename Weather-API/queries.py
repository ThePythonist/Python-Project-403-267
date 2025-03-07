import sqlite3

conn = sqlite3.connect("weather_data.db")
cur = conn.cursor()


def create(data):
    query1 = f"CREATE TABLE IF NOT EXISTS {data['city']} (dt,temp,humidity,wind_speed);"
    cur.execute(query1)

    query2 = f"INSERT INTO {data['city']} VALUES {(data['dt'], data['temp'], data['humidity'], data['wind_speed'])};"
    cur.execute(query2)
    conn.commit()
    conn.close()


def read(city):
    try:
        query = f"SELECT * FROM {city};"
        cur.execute(query)
        records = cur.fetchall()
    except sqlite3.OperationalError:
        print("No data available for this city")
        return

    if len(records) > 0:
        for i in records:
            print(i)
    else:
        print("No data available for this city")
