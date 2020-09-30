from db.run_sql import run_sql

from models.book import Book

def save(book):
    results = None
    sql = "INSERT INTO books (title, publisher, genre, loan_status, author_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.publisher, book.genre, book.loan_status, book.author.id]
    results = run_sql(sql, values)
    if results is not None:
        book.id = results[0]['id']
    return book


def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        book = Book(row['title'], row['publisher'], row['genre'], row['id'])
        books.append(book)
    return books


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)
    
def select(id):
    book = None
    sql = "SELECT * FROM books WHERE ID = %s"
    values = [id]

    result = run_sql(sql, values)[0]
    if result is not None:
        book = Book(row['title'], row['publisher'], row['genre'], row['id'])
    return book

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(book):
    sql = "UPDATE books SET name = %s WHERE id = %s"
    values = [book.title, book.publisher, book.genre]
    run_sql(sql,values)