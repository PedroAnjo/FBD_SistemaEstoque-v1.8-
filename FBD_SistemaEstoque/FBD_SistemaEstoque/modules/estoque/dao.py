from flask import Response
from modules.produto.dao import DAO_produto
from modules.estoque.modelo import Estoque
from modules.estoque.sql import SQLEstoque
from service.connect import ConnectDataBase


class DAO_estoque():

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def get_all(self):
        cursor = self.connect.cursor()
        sql = SQLEstoque._SELECT
        cursor.execute(sql)
        all_estoque = cursor.fetchall()
        estoques = []
        nome_colunas = [descricao[0] for descricao in cursor.description ]
        for estoque_encontrado in all_estoque:
            estoque_json = dict(zip(nome_colunas, estoque_encontrado))
            estoque = Estoque(**estoque_json)
            estoques.append(estoque.get_json())
        cursor.close()
        return estoques


    def get_produto_estoque_id(self, idproduto):
        cursor = self.connect.cursor()
        sql = SQLEstoque._SELECT_BY_ID.format(idproduto)
        cursor.execute(sql)
        estoque = cursor.fetchone()
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, estoque))
        return Estoque(**data)
        
    
    def add_produto_no_estoque(self,id, quantidade, dataentrada):
        produto = DAO_produto().get_produto_id(id)
        cursor = self.connect.cursor()
        sql = SQLEstoque._INSERT
        cursor.execute(sql,(id, produto.nome, quantidade, dataentrada))
        #cursor.execute(sql,(id, quantidade, dataEntrada))
        self.connect.commit()
        cursor.close()
        

    def update_produto_estoque(self, idproduto, quantidade, dataentrada):
        cursor = self.connect.cursor()
        sql = SQLEstoque._UPDATE
        cursor.execute(sql,(quantidade, dataentrada, idproduto))
        self.connect.commit()
        cursor.close()

    
    def update_quantidade(self, nova_quantidade, idproduto):
        cursor = self.connect.cursor()
        sql = SQLEstoque._UPDATE_QUANTIDADE
        cursor.execute(sql,(nova_quantidade, idproduto))
        self.connect.commit()
        cursor.close()


    def delete_produto_estoque(self, idproduto):
        cursor = self.connect.cursor()
        sql = SQLEstoque._DELETE.format(SQLEstoque._TABLE_NAME, idproduto)
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()

    def get_quantidade(self, idproduto):
        cursor = self.connect.cursor()
        produto = DAO_produto().get_produto_id(idproduto)
        if not produto:
            return Response({'produto não encontrado'}, status=404)
        sql = SQLEstoque._SELECT_QUANTIDADE_BY_ID.format(idproduto)
        cursor.execute(sql)
        quantidade = cursor.fetchone()
        cursor.close()
        return quantidade
        
    