from modules.item_pedido.modelo import ItemPedido
from modules.item_pedido.sql import SQLItemPedido
from modules.produto.dao import DAO_produto
from service.connect import ConnectDataBase


class DAO_item_pedido():
    def __init__(self) -> None:
        self.connect = ConnectDataBase().get_instance()

    def get_all(self):
        return
    
    def get_item_pedido_by_id(self, idPedido):
        cursor = self.connect.cursor()
        sql = SQLItemPedido._SELECT_BY_ID.format(SQLItemPedido._TABLE_NAME, idPedido)
        cursor.execute(sql)
        itens_pedido = cursor.fetchall() 
        
        itens = []
        for item in itens_pedido:
            idItemPedido,idpedido, idproduto,nomeproduto, quantidadeproduto = item
            item_encontrado = ItemPedido(idpedido, idproduto,nomeproduto, quantidadeproduto, idItemPedido)
            itens.append(item_encontrado.get_json())
        return itens
    
    def add_item_pedido(self, idpedido, idproduto, quantidadeproduto):
        cursor = self.connect.cursor()
        produto = DAO_produto().get_produto_id(idproduto)
        valorproduto = produto.preco
        nomeproduto = produto.nome
        sql = SQLItemPedido._INSERT
        cursor.execute(sql,(idpedido,idproduto, nomeproduto, valorproduto, quantidadeproduto))
        self.connect.commit()
        cursor.close()

    def delete_pedido(self, idPedido):
        return
    
