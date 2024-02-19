import sqlite3
with sqlite3.connect("../db/tests.db") as conn:
    c = conn.cursor()
    for i in range(10):
