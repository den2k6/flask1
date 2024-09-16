""" flask test """

import sqlite3
from flask import render_template, request, redirect, url_for
from flaskr import app


DATABASE = "database.db"


@app.route("/")
def index():
    """index"""
    con = sqlite3.connect(DATABASE)
    db_todos = con.execute("SELECT * FROM todos").fetchall()
    con.close()

    todos = []
    for row in db_todos:
        todos.append(
            {"todo_id": row[0], "status": row[1], "event": row[2], "limits": row[3]}
        )
    return render_template("index.html", todos=todos)


@app.route("/form")
def form():
    """form"""
    return render_template("form.html")


@app.route("/register", methods=["POST"])
def register():
    """register"""
    todo_id = request.form["todo_id"]
    status = request.form["status"]
    event = request.form["event"]
    limits = request.form["limits"]

    con = sqlite3.connect(DATABASE)
    con.execute(
        "INSERT INTO todos VALUES(?, ?, ?, ?)", [todo_id, status, event, limits]
    )
    con.commit()
    con.close()
    return redirect(url_for("index"))


@app.route("/delete/<todo_id>", methods=["POST"])
def delete(todo_id):
    """delete"""
    con = sqlite3.connect(DATABASE)
    con.execute("DELETE FROM todos WHERE todo_id=?", [todo_id])
    con.commit()
    con.close()
    return redirect(url_for("index"))
