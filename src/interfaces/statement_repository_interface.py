from abc import ABC, abstractmethod


class StatementRepositoryInterface(ABC):

    @abstractmethod
    def save(self, value, date, account_number, operation):
        raise Exception("Should implement method")

    @abstractmethod
    def list_statments(self, account_number):
        raise Exception("Should implement method")
