import sqlite3
import os
from random import randrange
from hashlib import sha256

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users")
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("DROP TABLE IF EXISTS userItems")

cur.execute("""CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    balance REAL NOT NULL
);
""")
cur.execute("""CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL
);
""")
            
cur.execute("""CREATE TABLE userItems (
    user_id INTEGER,
    item_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);
""")
            
cur.execute(f"INSERT INTO items (name,description,price) VALUES('Mug','Mugs are the best!',10)")
cur.execute(f"INSERT INTO items (name,description,price) VALUES('Flag','sunctf{{uNLimited_moNey_iS_so_C00l}}',100)")     
          
conn.commit()
conn.close()
