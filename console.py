import pdb 
from models.author import Author
from models.book import Book

author1 = Author("Iain M Banks")
book1 = Book("Matter", "Orbit", "Sci-Fi", author1.id)
# print(author1.name)
# print(book1.title)
# print(author1.id)
# print(book1.id)



pdb.set_trace()