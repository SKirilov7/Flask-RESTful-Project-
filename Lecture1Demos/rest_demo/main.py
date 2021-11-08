from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class BookModel:
    _pk = 1

    def __init__(self, title, author):
        self.id = BookModel._pk
        self.title = title
        self.author = author
        BookModel._pk += 1

    def serialize(self):
        return self.__dict__


books = [BookModel(f"Book number: {i}", f"Author number: {i}") for i in range(10)]


class Books(Resource):
    def get(self):
        return {"Books available": [b.serialize() for b in books]}

    def post(self):
        new_book = BookModel('New book', 'New author')
        books.append(new_book)
        return new_book.serialize(), 201


class Book(Resource):
    def get(self):
        try:
            book_searched = [b for b in books][0]
            return book_searched.serialize()
        except IndexError:
            return {"error": "Not Found"}, 404

    def put(self):
        try:
            searched_book = [b for b in books][0]
            searched_book.title = "Harry Potter"
            searched_book.author = 'Slavi Kirilov'
            return searched_book.serialize(), 201
        except IndexError:
            return {"error": "Not Found"}, 404

    def delete(self):
        try:
            searched_book = [b for b in books][0]
            books.remove(searched_book)
            return 204
        except IndexError:
            return {"error": "Not Found"}, 404


api.add_resource(Book, "/pk")
api.add_resource(Books, "/")

if __name__ == '__main__':
    app.run()
