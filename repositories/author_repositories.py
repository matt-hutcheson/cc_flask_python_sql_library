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


def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)
    
def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE ID = %s"
    values = [id]

    result = run_sql(sql, values)[0]
    if result is not None:
        author = Author(result["name"], result["id"])
    return author

def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(author):
    sql = "UPDATE authors SET name = %s WHERE id = %s"
    values = [author.name, author.id]
    run_sql(sql,values)

