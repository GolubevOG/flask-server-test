from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)
counter_file = "visits.txt"

def get_visit_count():
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f:
            f.write("0")
    with open(counter_file, "r") as f:
        return int(f.read())

def increment_visit_count():
    count = get_visit_count() + 1
    with open(counter_file, "w") as f:
        f.write(str(count))
    return count

@app.route('/')
def index():
    visit_num = increment_visit_count()
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    user_agent = request.headers.get('User-Agent', 'Неизвестно')
    accept_language = request.headers.get('Accept-Language', '—')
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <h1>👋 Привет, незнакомец!</h1>
    <p><b>Твой IP:</b> {ip}</p>
    <p><b>Браузер:</b> {user_agent}</p>
    <p><b>Язык:</b> {accept_language}</p>
    <p><b>🕒 Сейчас на сервере:</b> {server_time}</p>
    <p><b>🔢 Ты — {visit_num}-й посетитель этого сайта!</b></p>
    """
