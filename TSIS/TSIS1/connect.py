import psycopg2
from datetime import datetime
from config import DB_CONFIG   # импортируем словарь с параметрами подключения

def connect():
    try:
        conn = psycopg2.connect(**DB_CONFIG)  # используем словарь напрямую
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def parse_date(date_str):
    if not date_str or not isinstance(date_str, str):
        return None
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        print(f"Invalid date format: {date_str}. Expected YYYY-MM-DD.")
        return None
