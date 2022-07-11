#Caixa Eletronico
versão o python é a 3.10

Mais um caso de estudo.
Implementado um mini caixa eletronico com as opções de cadastro de usuario e quando estiver cadastrado é possivel verificar saldo, fazer deposito, saque e extrato.


Para ambiente linux.

Com do docker instaldo, caso não tenha -> https://docs.docker.com/engine/install/ e https://docs.docker.com/compose/install/

Caso queira utilizar o Banco de dados mysql crie um banco ou se preferir tem um arquivo docker-compose.yml para subir um container.

    $ cd infra/docker;
    $ docker-compose up database ou $ docker-compose up -d mysqldb caso queira fechar o terminal ;

Mas Também é possivel utilizar o sqlite na branch -> dev-sqlite.
   
     $ git checkout dev-sqlite

Crie um ambiente virtual para desenvolvimento e ative:
    
    $ python3 -m venv .env
    $ source .env/bin/activate

Instalando os requirements:

    $ pip install -r requirements.txt;

Com o banco de dados rodando, inicie as migrations:

    $ alembic updrade head

Só iniciar o projeto:
    $ python main.py
