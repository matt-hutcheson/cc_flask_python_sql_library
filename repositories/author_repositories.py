from db.run_sql import run_sql

from models.author import Author
# from models.book import Book

def save(author):
    results = None
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    if results is not None:
        author.id = results[0]['id']
    return author
    

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['name'], row['id'])
        authors.append(author)
    return authors


