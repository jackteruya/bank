from abc import ABC, abstractmethod


class AccountRepositoryInterface(ABC):

    @abstractmethod
    def created_account(self, cpf, date):
        raise Exception("Should implement method")

    @abstractmethod
    def get_account(self, cpf):
        raise Exception("Should implement method")

    @abstractmethod
    def update_balance(self, cpf, value):
        raise Exception("Should implement method")
