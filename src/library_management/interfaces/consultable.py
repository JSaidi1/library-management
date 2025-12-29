from abc import ABC, abstractmethod


class Consultable(ABC):
    @abstractmethod
    def consult(self):
        print("You are viewing this document.")