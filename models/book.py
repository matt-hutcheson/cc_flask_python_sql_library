class Book:
    def __init__(self, title, publisher, number_of_pages, author, loan_status=False id=None):
        self.title = title
        self.publisher = publisher
        self.number_of_pages = number_of_pages
        self.author = author
        self.loan_status = loan_status
        self.id = id