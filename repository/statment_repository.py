from sqlalchemy.exc import NoResultFound

from infra.db_config import DBConnectionHandler
from src.interfaces.statement_repository_interface import StatementRepositoryInterface
from repository.models.statement_orm import Statement
from src.domain.statement import Statement as StatementEtity


class StatementRepository(StatementRepositoryInterface):

    def save(self, value, date, account_number, operation):

        with DBConnectionHandler() as db_connection:
            try:
                new_statmente = Statement(
                    account_number=account_number,
                    date=date,
                    value=value,
                    operation=operation
                )
                db_connection.session.add(new_statmente)
                db_connection.session.commit()

                return StatementEtity(
                    account_number=new_statmente.account_number,
                    date=new_statmente.date,
                    value=new_statmente.value,
                    operation=new_statmente.operation,
                )

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

        return None

    def list_statments(self, account_number):
        with DBConnectionHandler() as db_connection:
            try:
                statments = (
                    db_connection.session.query(Statement)
                    .filter_by(account_number=account_number)
                    .all()
                )

                return [StatementEtity(account_number=statment.account_number,
                                       date=statment.date,
                                       value=statment.value,
                                       operation=statment.operation) for statment in statments]

            except NoResultFound:
                return []

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

        return None
