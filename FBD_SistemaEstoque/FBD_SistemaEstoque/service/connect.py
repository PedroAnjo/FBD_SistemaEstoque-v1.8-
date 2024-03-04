import psycopg2
from modules.item_pedido.sql import SQLItemPedido
from modules.pedido.sql import SQLPedido

from modules.cliente.sql import SQLCliente
from modules.produto.sql import SQLProduto
from modules.estoque.sql import SQLEstoque


class ConnectDataBase:
    def __init__(self):
       self.connection = psycopg2.connect(
            host = 'localhost',
            database = 'FBD_sistema_estoque',
            user = 'postgres',
            password = 'admin',
        )
       
    def get_instance(self):
        return self.connection
    
    
    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute(SQLCliente._CREATE_TABLE)
        cursor.execute(SQLProduto._CREATE_TABLE)
        cursor.execute(SQLEstoque._CREATE_TABLE)
        cursor.execute(SQLPedido._CREATE_TABLE)
        cursor.execute(SQLItemPedido._CREATE_TABLE)
        self.connection.commit()
        cursor.close()