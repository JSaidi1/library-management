from interfaces.consultable import Consultable
from models.document import Document


class Magazine(Document, Consultable):
    def __init__(self, titre: str, year_of_publication: int, number: int):
        super().__init__(titre, year_of_publication)
        self.number = number

    def show_informations(self):
        print(f"Magazine ({self.title, self.year_of_publication, self.number})")

    def consulter(self):
        super().consult()