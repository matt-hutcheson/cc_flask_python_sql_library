import pdb 
from models.author import Author
from models.book import Book

import repositories.author_repositories as author_repositories


author_repositories.delete_all()

author1 = Author("Iain M Banks")
author_repositories.save(author1)
book1 = Book("Matter", "Orbit", "Sci-Fi", author1.id)
# print(author1.name)
# print(book1.title)
# print(author1.id)
# print(book1.id)



authors_list = author_repositories.select_all()




pdb.set_trace()