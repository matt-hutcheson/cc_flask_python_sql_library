class Book:
    def __init__(self, title, publisher, genre, author, loan_status=False, id=None):
        self.title = title
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.loan_status = loan_status
        self.id = id