import pdb

from models.book import Book
from models.library import Library
import repositories.book_repository as book_repository
import repositories.library_repository as library_repository

book_repository.delete_all()
library_repository.delete_all()

library_1 = Library("CodeClan Library")
library_repository.save(library_1)

book_1 = Book("The Lord of the Rings", "J. R. R. Tolkein", library_1)
book_repository.save(book_1)

book_2 = Book("Head First Python", "Paul Barry", library_1)
book_repository.save(book_2)

pdb.set_trace()
