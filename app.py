from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Library Management</h1>';


@app.route('/books/<int:book_id>')
def get_book(book_id=''):
    if book_id == '':
        return '<h1>Book not informed</h1>';
    return f'<h1>Book ID: {escape(book_id)}</h1>';