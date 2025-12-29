from typing import List, Union
from enums.genre import Genre
from models.book import Book
from models.magazine import Magazine


class DocumentStore:

    @staticmethod
    def get_list_documents() -> List[Union[Book, Magazine]]:
        return [
            Book("The witcher", 2000, "Andrej", 600, Genre.FANTASY),
            Book("les 12 travaux", 1990, "Socrate", 500, Genre.NOVEL),
            Magazine("Canard PC", 2000, 3),
        ]

    
list_documents = DocumentStore.get_list_documents()
# for doc in list_document:
#     doc.show_informations()