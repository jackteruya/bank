from src.utils.validated_cpf import validated_cpf


class UserUserCase:
    def __init__(self, repository):
        self.repository = repository

    def created_user(self, name, cpf, nationality, password):
        try:
            if validated_cpf(cpf):
                return self.repository().created_user(name, cpf, nationality, password)
        except Exception as exc:
            return exc

    def get_user(self, cpf):
        try:
            if validated_cpf(cpf):
                return self.repository().get_user(cpf)
        except Exception as exc:
            return exc
