from sqlalchemy.exc import NoResultFound

from infra.db_config import DBConnectionHandler
from repository.models import User
from src.interfaces.user_repository_interface import UserRepositoryInterface
from src.domain.user import User as UserEntity


class UserRepository(UserRepositoryInterface):

    def created_user(self, name, cpf, nationality, password):
        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(
                    name=name,
                    cpf=cpf,
                    nationality=nationality,
                    password=password
                )
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return UserEntity(
                    name=new_user.name,
                    cpf=new_user.cpf,
                    nationality=new_user.nationality,
                    password=new_user.password
                )

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

        return None

    def get_user(self, cpf):
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session.query(User)
                    .filter_by(cpf=cpf)
                    .one()
                )

                return UserEntity(
                    name=data.name,
                    cpf=data.cpf,
                    nationality=data.nationality,
                    password=data.password
                )

            except NoResultFound:
                return []

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

        return None
