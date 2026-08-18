from abc import ABC, abstractmethod


class Account(ABC):

    @abstractmethod
    def display(self):
        pass