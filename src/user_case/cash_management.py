from src.responses import ResponseFailure


class CashManagementUserCase:

    def __init__(self):
        self._money = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0]

    def value_allowed(self, value):
        for m in self._money:
            value = value % m
            if value == 0:
                return True
        return False



