from src.library_management.enums.genre import Genre
from src.library_management.exceptions.document_already_borrowed_exception import DocumentAlreadyBorrowedException
from src.library_management.exceptions.document_not_borrowed_exception import DocumentNotBorrowedException
from src.library_management.interfaces.borrowable import Borrowable
from src.library_management.interfaces.consultable import Consultable
from src.library_management.models.document import Document


class Book(Document, Borrowable, Consultable):

    def __init__(self, title: str,  year_of_publication: int,  author: str, nb_pages: int, genre: Genre):
        super().__init__(title,  year_of_publication)
        Borrowable.__init__(self)
        self. author =  author
        self.nb_pages = nb_pages
        self.genre = genre

    @staticmethod
    def secondary_constructeur(self, title: str,  author: str, genre: Genre):
        return Book(title, 0,  author, 100, genre)
    
    @staticmethod
    def compt_nbr_pages(liste_book: list): 
        total = 0
        for book in liste_book:
            total += book.nb_pages
        
        return total
    
    def show_informations(self):
        print(f"Book ({self.title, self.author, self.year_of_publication, self.nb_pages, self.genre.name})")

    def  borrow(self):
        if self.is_borrowed == True: 
            raise DocumentAlreadyBorrowedException("You cannot borrow a book that has already been borrowed ...")
        else:
            print("Emprunt réussi !")
            self.is_borrowed = True

    def give_back(self):
        if self.is_borrowed == False: 
            raise DocumentNotBorrowedException("You cannot return a book that has not been borrowed ...")
        else:
            print("The book is available now.")
            self.is_borrowed = False
        
    def consult(self):
        super().consulter()