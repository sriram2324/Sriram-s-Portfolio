"""Database Seeder for Retail Sales Analytics."""

import os
import sqlite3

def seed_database(db_path: str):
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executescript(schema_sql)

    # Insert Customers
    customers = [
        (1, 'Aarav Sharma', 'aarav.s@example.com', 'Bangalore', 'Consumer'),
        (2, 'Priya Patel', 'priya.p@example.com', 'Mumbai', 'Corporate'),
        (3, 'Rohan Verma', 'rohan.v@example.com', 'Delhi', 'Consumer'),
        (4, 'Ananya Iyer', 'ananya.i@example.com', 'Chennai', 'Home Office'),
        (5, 'Vikram Singh', 'vikram.s@example.com', 'Hyderabad', 'Corporate'),
        (6, 'Neha Gupta', 'neha.g@example.com', 'Pune', 'Consumer'),
    ]
    cur.executemany("INSERT OR IGNORE INTO customers VALUES (?, ?, ?, ?, ?)", customers)

    # Insert Products
    products = [
        (101, 'Ergonomic Desk Chair', 'Furniture', 8500.0, 5200.0),
        (102, 'Wireless Mechanical Keyboard', 'Technology', 4200.0, 2400.0),
        (103, 'Noise-Cancelling Headphones', 'Technology', 9500.0, 6000.0),
        (104, 'Standing Desk Converter', 'Furniture', 12000.0, 8000.0),
        (105, 'Organic Cotton Notebook Pack', 'Office Supplies', 650.0, 300.0),
        (106, 'Gel Ink Pen Set (12-pack)', 'Office Supplies', 450.0, 180.0),
    ]
    cur.executemany("INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?, ?)", products)

    # Insert Orders
    orders = [
        (1001, 1, '2026-01-10', 'Delivered'),
        (1002, 2, '2026-01-15', 'Delivered'),
        (1003, 3, '2026-01-22', 'Delivered'),
        (1004, 1, '2026-02-05', 'Delivered'),
        (1005, 4, '2026-02-12', 'Delivered'),
        (1006, 5, '2026-02-18', 'Delivered'),
        (1007, 2, '2026-03-02', 'Delivered'),
        (1008, 6, '2026-03-14', 'Delivered'),
        (1009, 3, '2026-03-20', 'Delivered'),
    ]
    cur.executemany("INSERT OR IGNORE INTO orders VALUES (?, ?, ?, ?)", orders)

    # Insert Order Items
    order_items = [
        (1, 1001, 102, 2, 4200.0), # Keyboard x2 = 8400
        (2, 1001, 106, 3, 450.0),  # Pen x3 = 1350
        (3, 1002, 101, 1, 8500.0), # Chair x1 = 8500
        (4, 1003, 103, 1, 9500.0), # Headphones = 9500
        (5, 1004, 105, 4, 650.0),  # Notebook x4 = 2600
        (6, 1005, 104, 1, 12000.0),# Standing Desk = 12000
        (7, 1006, 102, 1, 4200.0), # Keyboard = 4200
        (8, 1006, 103, 1, 9500.0), # Headphones = 9500
        (9, 1007, 104, 1, 12000.0),# Standing Desk = 12000
        (10, 1008, 101, 1, 8500.0),# Chair = 8500
        (11, 1009, 103, 1, 9500.0),# Headphones = 9500
    ]
    cur.executemany("INSERT OR IGNORE INTO order_items VALUES (?, ?, ?, ?, ?)", order_items)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_file = os.path.join(os.path.dirname(__file__), "retail.db")
    seed_database(db_file)
    print(f"Database seeded at {db_file}")
