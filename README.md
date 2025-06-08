# 🔐 Password Manager — Flask + SQLite

Hi! This is my tutorial project — a simple password manager I wrote from scratch in Python Flask. The main idea is to store encrypted passwords in a database and decrypt them manually via XOR.

📌 Encryption is implemented without using external libraries — only standard Python.

---

## ⚙️ What the application can do:

- Add records with a website, login and password
- Encrypt passwords using XOR + Base64
- Save encrypted data in SQLite
- Decrypt records using the entered master password
- Display all records via the HTML interface

---

## 📁 Project structure

```
├── app.py # Flask application
├── passwords.db # Database (created at startup)
├── index.html # Main form (adding a password)
├── view.html # Table with encrypted passwords
├── static/ # CSS, styles
└── README.md
```

---

## 🚀 How to run the project:

1. Install Flask and SQLAlchemy:

```bash
pip install flask flask_sqlalchemy
```

2. Run the server:

```bash
python app.py
```

3. Go to the address in the browser:

http://127.0.0.1:5000

---

## 🔐 How encryption works

I implemented a simple symmetric XOR algorithm:

- Each character of the password is compared with the ASCII character of the master password
- The XOR (exclusive OR) operation is used
- The result is encoded in base64 for easy storage

Example:

```python
ord('p') = 112, ord('1') = 49
112 ^ 49 = 65 → chr(65) = 'A'
```

---

## 📋 How to decrypt

- On the /view page, copy the encrypted string
- Enter the same master password as when encrypting
- Get the original password

Without the correct key, you won't be able to decrypt - checked :)

---

## 🗂 Database

SQLite is used. Each record stores:

- website
- login
- encrypted password

The database is created automatically upon startup (file passwords.db).

---

## 💡 Why did I do this?

I wanted to better understand how symmetric ciphers, Flask web applications, and working with databases work. This project is the result of my training and practice.

---

## 📎 Link to GitHub

The project is available at the link:
https://github.com/yourusername/password-manager

If you have any ideas or comments, write, I will be glad to receive feedback!

---

🧑‍💻 Author: Nurshat
🌐 LinkedIn: https://www.linkedin.com/in/%D0%BD%D1%83%D1%80%D1%88%D0%B0%D1%82-%D1%88%D0%B8%D1%80%D0%BC%D1%83%D1%85%D0%B0%D0%BC%D0%B5%D1%82%D0%BE%D0%B2-772138363/
