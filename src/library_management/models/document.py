from abc import ABC, abstractmethod


class Document(ABC):
    nb_document = 0

    def __init__(self, title: str, year_of_publication: int):
        self.title = title 
        self.year_of_publication = year_of_publication

    @abstractmethod
    def show_informations(self):
        pass

    @classmethod
    def show_nbr_documents(cls):
        print(f"\nWe currently have {cls.nb_document} documents in our library.")