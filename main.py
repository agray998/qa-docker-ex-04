from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{getenv('DATABASE', default='default')}.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    email = db.Column(db.String(30), unique=True)

@app.route('/')
def index():
    return '<br>'.join('\t'.join([c.first_name, c.surname, c.email]) for c in Customer.query.all())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
