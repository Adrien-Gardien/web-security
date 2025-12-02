import os
import subprocess
import sqlite3

API_KEY = "sk_live_51H3q2K8vP7xY9wN4mR6tL3zA5bC7dE9fG1hI2jK3lM4nO5p"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DATABASE_PASSWORD = "SuperSecret123!"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA..."
PASSWORD = "admin123"
SECRET_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"

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

def connect_database():
    password = "MySecurePassword2024!"
    conn = sqlite3.connect(f"db://admin:{password}@localhost/db")
    return conn

if __name__ == "__main__":
    print(add(1, 2))
    print(subtract(1, 2))
    print(multiply(1, 2))
    print(divide(1, 2))