from sqlalchemy.exc import NoResultFound

from infra.db_config import DBConnectionHandler
from repository.models import Account
from src.interfaces.account_repository_interface import AccountRepositoryInterface
from src.domain.account import Account as AccountEntity


class AccountRepository(AccountRepositoryInterface):

    def created_account(self, cpf, date):
        with DBConnectionHandler() as db_connection:
            try:
                new_account = Account(
                    cpf=cpf,
                    created_date=date,
                    bank_balance=0.00
                )
                db_connection.session.add(new_account)
                db_connection.session.commit()

                return AccountEntity(
                    account=new_account.account,
                    cpf=new_account.cpf,
                    created_date=new_account.created_date,
                    bank_balance=new_account.bank_balance,
                )

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

        return None

    def get_account(self, cpf):
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session.query(Account)
                    .filter_by(cpf=cpf)
                    .one()
                )

                return AccountEntity(
                    account=data.account,
                    cpf=data.cpf,
                    created_date=data.created_date,
                    bank_balance=data.bank_balance,
                )

            except NoResultFound:
                return []

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

        return None

    def update_balance(self, cpf, value):

        with DBConnectionHandler() as db_connection:
            try:
                account = db_connection.session.query(Account).filter_by(cpf=cpf).one()
                account.bank_balance = value
                db_connection.session.commit()

                return AccountEntity(
                    account=account.account,
                    cpf=account.cpf,
                    created_date=account.created_date,
                    bank_balance=account.bank_balance,
                )

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

        return None
