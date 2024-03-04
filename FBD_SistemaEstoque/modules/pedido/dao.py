from modules.item_pedido.dao import DAO_item_pedido
from modules.pedido.modelo import Pedido
from modules.pedido.sql import SQLPedido
from service.connect import ConnectDataBase


class DAO_pedido():
    def __init__(self) -> None:
        self.connect = ConnectDataBase().get_instance()

    def get_all(self):
        cursor = self.connect.cursor()
        sql = SQLPedido._SELECT
        cursor.execute(sql)
        all_pedido = cursor.fetchall()
        pedidos = []
        nome_colunas = [descricao[0] for descricao in cursor.description ]
        for pedido_encontrado in all_pedido:
            item_pedido = DAO_item_pedido().get_item_pedido_by_id(pedido_encontrado[0])
            pedidos.append({"idPedido":pedido_encontrado[0],"idCliente":pedido_encontrado[1], "dataPedido":pedido_encontrado[2], "itens": item_pedido })
            
        cursor.close()
        return pedidos
    
    def get_pedido_id(self, idPedido):
        cursor = self.connect.cursor()
        sql = SQLPedido._SELECT_BY_ID.format(SQLPedido._TABLE_NAME, idPedido)
        cursor.execute(sql)
        estoque = cursor.fetchone()
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, estoque))
        return Pedido(**data)
    
    def add_pedido(self, pedido):
        cursor = self.connect.cursor()
        sql = SQLPedido._INSERT
        cursor.execute(sql,(pedido.idcliente, pedido.datapedido))
        novo_pedido_tuple = cursor.fetchone()
        novo_pedido = Pedido(idpedido=novo_pedido_tuple[0], idcliente=novo_pedido_tuple[1], datapedido=novo_pedido_tuple[2])
        self.connect.commit()
        cursor.close()
        return novo_pedido
        

    def delete_pedido(self, idPedido):
        cursor = self.connect.cursor()
        sql = SQLPedido._DELETE.format(SQLPedido._TABLE_NAME, idPedido)
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()
