
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "tasks.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_db_connection()
    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()


@app.route("/")
def home():
    connection = get_db_connection()
    tasks = connection.execute(
        "SELECT * FROM tasks ORDER BY id DESC"
    ).fetchall()
    connection.close()

    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task", "").strip()

    if task_name:
        connection = get_db_connection()
        connection.execute(
            "INSERT INTO tasks (task) VALUES (?)",
            (task_name,)
        )
        connection.commit()
        connection.close()

    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    connection = get_db_connection()
    connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    connection.commit()
    connection.close()

    return redirect(url_for("home"))


create_table()

if __name__ == "__main__":
    app.run(debug=True)
