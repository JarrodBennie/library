class Book:
    def __init__(self, title, author, library, id=None):
        self.title = title
        self.author = author
        self.library = library
        self.id = id

    def pretty_print(self):
        return f"{self.title} by {self.author}"
