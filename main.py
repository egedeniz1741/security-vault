import os
import sqlite3
from fastapi import FastAPI

app = FastAPI()


AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "default_unsafe_key")


def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INT, username TEXT, role TEXT)")
    c.execute("DELETE FROM users")
    c.execute("INSERT INTO users VALUES (1, 'josh', 'user')")
    c.execute("INSERT INTO users VALUES (2, 'root_admin', 'superadmin')")
    conn.commit()
    conn.close()


init_db()


@app.get("/")
def home():
    return {"status": "online", "message": "Security-Vault API is running!"}


@app.get("/user")
def get_user(username: str):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    
    query = "SELECT * FROM users WHERE username = ?"
    c.execute(query, (username,))
    result = c.fetchall()
    conn.close()

    return {"searched_user": username, "data": result}