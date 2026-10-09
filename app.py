"""A tiny module for the CodeGuard end-to-end test."""

import sqlite3


def find_user(conn: sqlite3.Connection, email: str):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = '%s'" % email)
    return cursor.fetchone()


def add(a: int, b: int) -> int:
    return a + b
