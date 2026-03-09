from flask import Flask, render_template_string, request
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Đọc file HTML trực tiếp từ cùng thư mục với file Python
def load_template(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    user_data = None
    all_data = []

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db()
        cursor = conn.cursor()

        # Kiểm tra username/password
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            message = f"Đăng nhập thành công: {username}"
            # Lấy thông tin user
            cursor.execute("SELECT * FROM info WHERE username=?", (username,))
            user_data = cursor.fetchone()
        else:
            message = "Đăng nhập thất bại"

        # Lấy tất cả dữ liệu info để hiển thị bên dưới
        cursor.execute("SELECT * FROM info")
        all_data = cursor.fetchall()

        conn.close()

    # Load template từ file index.html ngoài thư mục templates
    template_str = load_template('index.html')
    return render_template_string(template_str, message=message, user_data=user_data, all_data=all_data)

if __name__ == '__main__':
    app.run(debug=True)