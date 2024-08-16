ETL Project with PostgreSQL
Цей проєкт містить Python ETL-програму, яка виконує завантаження
даних з CSV-файлу до бази даних PostgreSQL. Проєкт також містить
приклади SQL-запитів для роботи з даними та Docker-конфігурацію
для контейнеризації програми та бази даних.

Запуск проєкту

Створення віртуального середовища та встановлення залежностей:
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt

Виконайте команду для побудови та запуску Docker-контейнерів:
    docker-compose up --build
Ця команда запустить два контейнери:
    db: PostgreSQL база даних.
    app: Контейнер з Python додатком, який виконує ETL процес.

Виконання SQL-запитів
    Для підключення до бази даних можна використовувати
    будь-який клієнт PostgreSQL (наприклад, pgAdmin або
    psql). Підключіться до бази даних з такими параметрами:

    Host: localhost
    Port: 5432
    Database: inforcedb
    User: postgres
    Password: Ars2004@


Деталі Python ETL-програми
Python скрипт etl.py виконує такі основні функції:
    - Читає дані з CSV-файлу (sample_data.csv).
    - Перетворює дані (опціонально) та вставляє їх у базу даних PostgreSQL.
    - Усі параметри підключення до бази даних зчитуються з середовища (environment variables).
Деталі SQL-запитів
    - Отримати всі унікальні домени електронної пошти:
        SELECT DISTINCT SUBSTRING(email FROM '@.*$') AS domain FROM sample_data;
    - Отримати користувачів, зареєстрованих за останні 7 днів:
        SELECT * FROM sample_data WHERE registration_date >= NOW() - INTERVAL '7 days';
    - Знайти користувачів із найпоширенішим доменом електронної пошти:
        WITH topDomain AS (
            SELECT SUBSTRING(email FROM '@.*$') AS domain, COUNT(*) AS dc
            FROM sample_data
            GROUP BY domain
            ORDER BY dc DESC
            LIMIT 1
        )
        SELECT * FROM sample_data
        WHERE SUBSTRING(email FROM '@.*$') = (SELECT domain FROM topDomain);

Структура проєкту
.
├── Dockerfile               # Dockerfile для створення образу Python-додатку
├── docker-compose.yml       # Файл Docker Compose для запуску контейнерів
├── requirements.txt         # Список Python-залежностей
├── etl.py                   # Головний Python скрипт для ETL процесу
└── sample_data.csv          # CSV-файл з початковими даними
