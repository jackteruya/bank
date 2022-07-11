from datetime import datetime

from src.responses import ResponseSuccess, ResponseFailure, ResponseTypes
from src.user_case.statement import StatementUserCase
from src.utils.validated_cpf import validated_cpf
from src.utils.get_numeric import get_numeric


class AccountUserCase:
    def __init__(self, repository):
        self.repository = repository
        self._operation_type = {
            "deposit": "C",
            "withdraw": "D"
        }

    def created_account(self, user_repository, name, cpf, nationality, password):
        try:
            if validated_cpf(cpf):
                if len(cpf) > 11:
                    cpf = get_numeric(cpf)
                user = user_repository().created_user(name, cpf, nationality, password)

                date = datetime.today()
                account = self.repository().created_account(user.cpf, date)
                return ResponseSuccess(account)

        except Exception as exc:
            return exc

    def get_account(self, cpf):
        try:
            if len(cpf) > 11:
                cpf = get_numeric(cpf)
            if validated_cpf(cpf):
                account = self.repository().get_account(cpf)
                return ResponseSuccess(account)

        except Exception as exc:
            return exc

    def view_balance(self, cpf):
        try:
            if len(cpf) > 11:
                cpf = get_numeric(cpf)
            if validated_cpf(cpf):
                account = self.repository().get_account(cpf)
                return ResponseSuccess(account.bank_balance)
        except Exception as exc:
            return exc

    def deposited(self, repository_statemant, cpf, value, account_number):
        try:
            if len(cpf) > 11:
                cpf = get_numeric(cpf)
            if validated_cpf(cpf):
                date = datetime.today()
                StatementUserCase(
                    repository_statemant
                ).register_movimentation(value, date, account_number, self._operation_type["deposit"])

                self._updated_balance(cpf, self._operation_type["deposit"], value)

                return ResponseSuccess()

        except Exception as exc:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)

    def withdraw(self, repository_statemant, cpf, value, account_number):
        try:
            if len(cpf) > 11:
                cpf = get_numeric(cpf)
            if validated_cpf(cpf):
                account = self.repository().get_account(cpf)
                date = datetime.today()
                if account.bank_balance < value:
                    return ResponseFailure(ResponseTypes.SYSTEM_ERROR, "Valor maior que saldo !")
                StatementUserCase(
                    repository_statemant
                ).register_movimentation(value, date, account_number, self._operation_type["withdraw"])

                self._updated_balance(cpf, self._operation_type["withdraw"], value)

                return ResponseSuccess()

        except Exception as exc:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)

    def _updated_balance(self, cpf, operation, value):
        try:
            if len(cpf) > 11:
                cpf = get_numeric(cpf)
            if validated_cpf(cpf):
                account = self.view_balance(cpf)

                if operation == self._operation_type["deposit"]:
                    new_balance = account.value + value
                    self.repository().update_balance(cpf, new_balance)
                    return ResponseSuccess()

                if operation == self._operation_type["withdraw"]:
                    new_balance = account.value - value
                    self.repository().update_balance(cpf, new_balance)
                    return ResponseSuccess()

        except Exception as exc:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
