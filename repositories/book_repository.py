from models.book import Book
import repositories.library_repository as library_repository
from db.run_sql import run_sql


def save(book):
    sql = """
        INSERT INTO books (title, author, library_id)
        VALUES (%s, %s, %s)
        RETURNING id
    """
    values = [book.title, book.author, book.library.id]
    results = run_sql(sql, values)

    id = results[0]["id"]
    book.id = id


def select(id):
    sql = """
        SELECT * FROM books
        WHERE id = %s
    """
    values = [id]
    result = run_sql(sql, values)[0]

    title = result["title"]
    author = result["author"]
    library_id = result["library_id"]
    library = library_repository.select(library_id)
    id = result["id"]
    book = Book(title, author, library, id)

    return book


def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for result in results:
        title = result["title"]
        author = result["author"]
        library_id = result["library_id"]
        library = library_repository.select(library_id)
        id = result["id"]
        book = Book(title, author, library, id)
        books.append(book)

    return books


def update(book):
    sql = """
        UPDATE books
        SET (title, author, library_id) = (%s, %s, %s)
        WHERE id = %s
    """
    values = [book.title, book.author, book.library.id, book.id]
    run_sql(sql, values)


def delete(book):
    sql = """
        DELETE FROM books
        WHERE id = %s
    """
    values = [book.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)


def select_by_library(library):
    books = []
    sql = """
        SELECT * FROM books
        WHERE library_id = %s
    """
    values = [library.id]
    results = run_sql(sql, values)

    for result in results:
        title = result["title"]
        author = result["author"]
        id = result["id"]
        book = Book(title, author, library, id)
        books.append(book)

    return books
