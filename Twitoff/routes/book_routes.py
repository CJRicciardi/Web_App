# Web_App/Twitoff/routes/book_routes.py

from flask import Blueprint, jsonify, render_template, request

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
    return render_template("books.html", books=books)

@book_routes.route("/books/new")
def new_books():
    print('visited the new books page')
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["post"])
def create_book():
    print('Form Data:', dict(request.form))
    #todo: store in database
    return jsonify({
        "message": "Book created ok (TODO)",
        "book": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")