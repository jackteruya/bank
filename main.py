import re
from time import sleep

from src.user_case.account import AccountUserCase
from src.user_case.cash_management import CashManagementUserCase
from src.user_case.user import UserUserCase
from src.user_case.statement import StatementUserCase
from repository.account_repository import AccountRepository
from repository.user_repository import UserRepository
from repository.statment_repository import StatementRepository


def main():
    message_bank = """
    Bem Vindo ao Konv Mini Bank \n
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """
    print(message_bank)

    msg_opcao = """
    1 - Novo Cliente
    2 - Serviços para Cliente
    """
    print(msg_opcao)
    resposta = input("Informe o numero da opção desejada: ")

    if str(resposta) in ["1", "2"]:
        pass
    else:
        print("Opção invalida")
        return

    if int(resposta) == 1:
        msg_novo = """
        Informe seus dados:
        """
        print(msg_novo)
        nome = input("Nome: ")
        cpf = str(input("CPF: "))
        nacionalidade = input("nacionalidade: ")
        senha = input("senha: ")

        account = AccountUserCase(AccountRepository)\
            .created_account(
            UserRepository,
            name=nome,
            cpf=cpf,
            nationality=nacionalidade,
            password=senha
        )
        print(f"{nome} foi conta criado com sucesso!!!")
        print("Aguarde um instante que estaremos redirecionado para o menu do Cliente.")
        sleep(3)
    else:
        cpf = input("Por favor, informe seu CPF: ")
        response = AccountUserCase(AccountRepository).get_account(cpf)
        if not response:
            print("Conta não identificada, tente novamente!")
            return
        account = response.value
        # sleep(3)

    while account:
        menu_cliente = """\n\nMenu Cliente
        1 - Saldo
        2 - Depósito
        3 - Saque
        4 - Extrato
        5 - Sair
        """
        print(menu_cliente)
        opcao_menu_cliente = int(input("Informe o numero da opção desejada: "))
        if opcao_menu_cliente == 1:
            cpf = str(input("Informe seu CPF: "))
            saldo = AccountUserCase(AccountRepository).view_balance(cpf)
            saldo = str(round(saldo.value, 2)).replace(".", ",")
            print(f"Saldo Atual: R$ {saldo}")
            input("pressione enter")

        if opcao_menu_cliente == 2:
            msg_deposito = "Para deposito informe o valor e CPF, ex: 50,00 999.999.999-11"
            print(msg_deposito)

            valor_cpf = str(input("valor e CPF: "))
            if len(valor_cpf.split()) <= 1:
                print(1)
                return
            valor = valor_cpf.split()[0]
            if "," in valor:
                if not re.search(r"[0-9]*", valor[-2:]):
                    print("Valor invalido")
                valor = valor.replace(",", ".")

            valor = float(valor)
            if not CashManagementUserCase().value_allowed(valor):
                print("Valor Invalido")
            cpf = valor_cpf.split()[1]

            account_user = AccountUserCase(AccountRepository)
            response = account_user.get_account(cpf)

            account_number = response.value.account
            account_user.deposited(StatementRepository, cpf, valor, account_number)
            if not response:
                print("Valor invalido")
            elif response:
                print("Valor depositado com sucesso!!!")
                input("pressione enter")

        if opcao_menu_cliente == 3:
            msg_deposito = "Para sacar informe o valor e CPF, ex: 50,00 999.999.999-11"
            print(msg_deposito)

            valor_cpf = str(input("valor e CPF: "))
            valor = valor_cpf.split()[0]
            if "," in valor:
                if not re.search(r"[0-9]*", valor[-2:]):
                    print("Valor invalido")
                valor = valor.replace(",", ".")

            valor = float(valor)
            if not CashManagementUserCase().value_allowed(valor):
                print("Valor Invalido")
            cpf = valor_cpf.split()[1]

            account_user = AccountUserCase(AccountRepository)
            response = account_user.get_account(cpf)

            account_number = response.value.account

            response = account_user.withdraw(StatementRepository, cpf, valor, account_number)
            if not response:
                print(response.message)
            elif response:
                print("Saque realizado com sucesso!!!")
                input("pressione enter")

        if opcao_menu_cliente == 4:
            msg_extrato = "visualizar seu extrato, informe seu CPF"
            print(msg_extrato)

            cpf = str(input("CPF: "))

            account_user = AccountUserCase(AccountRepository)
            response = account_user.get_account(cpf).value

            account_number = response.account
            extrato = StatementUserCase(StatementRepository).list(account_number)

            saldo = AccountUserCase(AccountRepository).view_balance(cpf)
            saldo = str(round(saldo.value, 2)).replace(".", ",")
            print(extrato)

            print("   Data            -             valor  -      operação (D-debito(saida) / C-credito(entradas)")
            for movimentacao in extrato:
                print(f"{movimentacao.date}          -  {movimentacao.value}  -       {movimentacao.operation}")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print(f"Saldo: {saldo}")
            input("pressione enter")

        if opcao_menu_cliente == 5:
            account = None


if __name__ == "__main__":
    status = True
    while status:
        main()
