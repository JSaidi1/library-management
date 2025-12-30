import sys
from typing import List, Union
from enums.genre import Genre
from models.book import Book
from models.magazine import Magazine
from models.document import Document


class DocumentStore:

    list_documents = [Book("The witcher", 2000, "Andrej", 600, Genre.FANTASY),
                      Book("les 12 travaux", 1990, "Socrate", 500, Genre.NOVEL),
                      Magazine("Canard PC", 2000, 3)
                     ]
    
    @classmethod
    def add_document(self, new_document: Document):
        if new_document != None:
            self.list_documents.append(new_document)
            print(f"The document below has been successfully added to the docs list:")
            new_document.show_informations()
    
    @classmethod
    def remove_document(self, document_to_remove: Document):
        doc_to_remove_from_list = None
        if document_to_remove != None:
            for doc in self.list_documents:
                if doc == document_to_remove:
                    doc_to_remove_from_list = doc
                    break
            if doc_to_remove_from_list == None:
                print("The document is not on the list: It cannot be deleted!")
            else:
                self.list_documents.remove(doc_to_remove_from_list)
                print(f"The document below has been successfully removed from the docs list:")
                doc_to_remove_from_list.show_informations()            
        else:
            print(f"Failed to remove the document below because it's not present on the docs list: None")
            document_to_remove.show_informations()

list_documents = DocumentStore.list_documents