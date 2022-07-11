class StatementUserCase:
    def __init__(self, repository):
        self.repository = repository

    def register_movimentation(self, value, date, account_number, operation):
        try:
            if operation:
                self.repository().save(value, date, account_number, operation)
        except Exception as exc:
            return exc

    def list(self, account_number):
        try:
            return self.repository().list_statments(account_number)
        except Exception as exc:
            return exc
