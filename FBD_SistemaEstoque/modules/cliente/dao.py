from modules.cliente.modelo import Cliente
from modules.cliente.sql import SQLCliente
from service.connect import ConnectDataBase


class DAO_cliente(object):

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def get_all(self):
        cursor = self.connect.cursor()
        sql = SQLCliente._SELECT
        cursor.execute(sql)
        all_cliente = cursor.fetchall()
        lista_clientes = []
        nome_colunas = [descricao[0] for descricao in cursor.description ]
        #print(cursor.description)
        for cliente_encontrado in all_cliente:
            cliente_json = dict(zip(nome_colunas, cliente_encontrado))
            cliente = Cliente(**cliente_json)
            lista_clientes.append(cliente.get_json())
        cursor.close()
        return lista_clientes

    
    def get_cliente_id(self, id):
        cursor = self.connect.cursor()
        sql = SQLCliente._SELECT_BY_ID.format(SQLCliente._TABLE_NAME, id)
        cursor.execute(sql)
        cliente = cursor.fetchone()
        if not cliente:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, cliente))
        cliente = Cliente(**data)
        cursor.close()
        return cliente
    

    
    def new_cliente(self, cliente):
        cursor = self.connect.cursor()
        sql = SQLCliente._INSERT
        cursor.execute(sql, (cliente.nome, cliente.cpf, cliente.dataniversario))
        self.connect.commit()
        cursor.close()
        return cliente.id


    def update_cliente(self, cliente_old, cliente_new):
        cursor = self.connect.cursor()
        sql = SQLCliente._UPDATE
        cursor.execute(sql, (cliente_new.nome, cliente_new.cpf, cliente_new.dataaniversario, cliente_old.id))
        self.connect.commit()
        cursor.close()
        

    def delete_cliente(self, id):
        cursor = self.connect.cursor()
        sql = SQLCliente._DELETE.format(SQLCliente._TABLE_NAME, id)
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()