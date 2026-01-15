import sqlite3
from src.config import DB_PATH

def create_prices_table():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS prices (
                city TEXT PRIMARY KEY,
                price INTEGER    
            )
    """)
        
    conn.execute("INSERT OR IGNORE INTO prices VALUES ('mumbai', 6000), ('kochi',10500),('delhi',7000)")


def get_ticket_price(city):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT price from prices where city=?", (city.lower(),))
        result=cursor.fetchone()
        return f"Ticket price to {city.title()} is Rs{result[0]}" if result else "No price data available"