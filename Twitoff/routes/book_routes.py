# Web_App/Twitoff/routes/book_routes.py

from flask import Blueprint, jsonify, render_template

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    print('requested the books in json format')
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]  # todo: get from the database
    return jsonify(books)

@book_routes.route("/books")
def books():
    print('visited the books page')
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]  # todo: get from the database
    return render_template("books.html")