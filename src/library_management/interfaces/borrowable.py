from abc import ABC, abstractmethod


class Borrowable(ABC):
    def __init__(self):
        self.is_borrowed = False

    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def give_back(self):
        pass