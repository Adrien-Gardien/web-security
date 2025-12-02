import os
import subprocess
import sqlite3

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def sql_injection(user_input):
    conn = sqlite3.connect('database.db')
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    conn.execute(query)
    conn.close()

def path_traversal(filename):
    file_path = "/data/" + filename
    with open(file_path, 'r') as f:
        return f.read()

def command_injection(user_input):
    os.system("ls " + user_input)

if __name__ == "__main__":
    print(add(1, 2))
    print(subtract(1, 2))
    print(multiply(1, 2))
    print(divide(1, 2))