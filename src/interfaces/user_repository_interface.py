from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):

    @abstractmethod
    def created_user(self, name, cpf, nationality, password):
        raise Exception("Should implement method")

    @abstractmethod
    def get_user(self, cpf):
        raise Exception("Should implement method")
