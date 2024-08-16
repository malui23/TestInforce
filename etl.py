import pandas as pd
import psycopg2
import os

def ETL(file_name):
    # Читання даних з CSV
    data = pd.read_csv(file_name)
    data.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

    # Обробка дат і доменів
    data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%Y')
    data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')
    data['Domain'] = data['Email'].str.extract(r'(@[\w.-]+)')

    # Підключення до бази даних PostgreSQL
    conn = psycopg2.connect(
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT']
    )
    cursor = conn.cursor()

    # Створення запиту для вставки даних
    columns = ', '.join(data.columns)  # Список всіх стовпців
    placeholders = ', '.join(['%s'] * len(data.columns))  # Місця для параметрів
    insert_query = f"""
        INSERT INTO sample_data ({columns})
        VALUES ({placeholders})
    """

    # Вставка даних у таблицю
    for _, row in data.iterrows():
        cursor.execute(insert_query, tuple(row))

    # Фіксація змін
    conn.commit()

    # Закриття курсора та з'єднання
    cursor.close()
    conn.close()


if __name__ == '__main__':
    ETL('sample_data.csv')
