from flask import Flask, request, jsonify, send_file, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import base64

app = Flask(
    __name__,
    static_folder='static',
    template_folder='.'
)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class PasswordEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(100))
    login = db.Column(db.String(100))
    encrypted_password = db.Column(db.Text)

 
def xor_encrypt(plain_text, key):
    result = []
    for i in range(len(plain_text)):
        result.append(chr(ord(plain_text[i]) ^ ord(key[i % len(key)])))
    return base64.urlsafe_b64encode("".join(result).encode()).decode()

def xor_decrypt(cipher_text, key):
    try:
        decoded = base64.urlsafe_b64decode(cipher_text.encode()).decode()
        result = []
        for i in range(len(decoded)):
            result.append(chr(ord(decoded[i]) ^ ord(key[i % len(key)])))
        return "".join(result)
    except Exception:
        return None

@app.route('/')
def index():
    return send_file('index.html')


@app.route('/add', methods=['POST'])
def add_password():
    data = request.json
    encrypted_password = xor_encrypt(data['password'], data['master'])

    new_entry = PasswordEntry(
        site=data['site'],
        login=data['login'],
        encrypted_password=encrypted_password
    )
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({'encrypted': encrypted_password})


@app.route('/decrypt', methods=['POST'])
def decrypt_password():
    data = request.json
    decrypted = xor_decrypt(data['encrypted'], data['master'])

    if decrypted is not None:
        return jsonify({'decrypted': decrypted})
    else:
        return jsonify({'error': 'Ошибка расшифровки'}), 400


@app.route('/view')
def view_passwords():
    entries = PasswordEntry.query.all()
    return render_template('view.html', entries=entries)


@app.route('/api/entries')
def api_entries():
    entries = PasswordEntry.query.all()
    return jsonify([
        {
            'site': e.site,
            'login': e.login,
            'encrypted': e.encrypted_password
        }
        for e in entries
    ])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
