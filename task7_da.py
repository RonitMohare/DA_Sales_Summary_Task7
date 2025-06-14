# -*- coding: utf-8 -*-
"""Task7_DA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gkQ8M0dsd37sS4YmaxlMl4N-PhOSB_Qc
"""

import sqlite3

# Connect to database (creates the file if it doesn't exist)
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

# Insert sample data
sample_data = [
    ('Shoes', 10, 50.0),
    ('Shirts', 20, 25.0),
    ('Pants', 15, 40.0),
    ('Shoes', 5, 50.0),
    ('Shirts', 10, 25.0)
]

cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)
conn.commit()
conn.close()

import sqlite3
conn = sqlite3.connect("sales_data.db")

query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

import pandas as pd

df = pd.read_sql_query(query, conn)
print(df)

import matplotlib.pyplot as plt

df.plot(kind='bar', x='product', y='revenue', title='Revenue by Product')
plt.ylabel("Revenue (₹)")
plt.xlabel("Product")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Save image
plt.show()