import sqlite3

conn = sqlite3.connect('database.db')  # File database SQLite thật
c = conn.cursor()

# Tạo bảng users
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
''')

# Tạo bảng info
c.execute('''
CREATE TABLE IF NOT EXISTS info (
    username TEXT PRIMARY KEY,
    pet TEXT,
    salary REAL,
    FOREIGN KEY (username) REFERENCES users(username)
)
''')

# Thêm dữ liệu demo
c.execute("INSERT OR IGNORE INTO users VALUES ('alice', '1234')")
c.execute("INSERT OR IGNORE INTO users VALUES ('bob', 'abcd')")

c.execute("INSERT OR IGNORE INTO info VALUES ('alice', 'Chó', 5000)")
c.execute("INSERT OR IGNORE INTO info VALUES ('bob', 'Mèo', 7000)")

conn.commit()
conn.close()

print("Database đã được tạo thành công")