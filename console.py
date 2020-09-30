import pdb 
from models.author import Author
from models.book import Book

import repositories.author_repositories as author_repositories
import repositories.book_repositories as book_repositories

book_repositories.delete_all()
author_repositories.delete_all()

author1 = Author("Iain Banks")
author_repositories.save(author1)
author2 = Author("Adrian Tchaikovsky")
author_repositories.save(author2)
book1 = Book("Matter", "Orbit", "Sci-Fi", author1)
book_repositories.save(book1)
book2 = Book("Children of Time", "Tor Books", "Sci-Fi", author2)
book_repositories.save(book2)
# print(author1.name)
# print(book1.title)
# print(author1.id)
# print(book1.id)





# author_repositories.delete(author2.id)

select_author = author_repositories.select(author1.id)

author1.name = 'Ian M Banks'

# author_repositories.update(author1)

authors_list = author_repositories.select_all()

pdb.set_trace()