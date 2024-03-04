from flask import make_response
from modules.produto.modelo import Produto
from modules.produto.sql import SQLProduto
from service.connect import ConnectDataBase


class DAO_produto(object):

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def get_all(self):
        cursor = self.connect.cursor()
        sql = SQLProduto._SELECT
        cursor.execute(sql)
        all_produto = cursor.fetchall()
        lista_produtos = []
        nome_colunas = [descricao[0] for descricao in cursor.description ]
        #print(cursor.description)
        for produto_encontrado in all_produto:
            produto_json = dict(zip(nome_colunas, produto_encontrado))
            produto = Produto(**produto_json)
            lista_produtos.append(produto.get_json())
        cursor.close()
        return lista_produtos

    
    def get_produto_id(self, idproduto):
        cursor = self.connect.cursor()
        sql = SQLProduto._SELECT_BY_ID.format(SQLProduto._TABLE_NAME, idproduto)
        cursor.execute(sql)
        produto = cursor.fetchone()
        if not produto:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, produto))
        produto = Produto(**data)
        cursor.close()
        return produto
    
    def get_produto_by_nome(self, produto):
        cursor = self.connect.cursor()
        sql = SQLProduto._SELECT_BY_NOME.format(SQLProduto._TABLE_NAME, produto.nome)
        cursor.execute(sql)
        produto = cursor.fetchone()
        if not produto:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, produto))
        produto = Produto(**data)
        cursor.close()
        return produto
    
    
    def new_produto(self, produto):
        cursor = self.connect.cursor()
        sql = SQLProduto._INSERT
        cursor.execute(sql, (produto.nome, produto.descricao, produto.preco, produto.datavalidade))
        self.connect.commit()
        cursor.close()
        return produto.idproduto


    def update_produto(self, produto_old, produto_new):
        cursor = self.connect.cursor()
        sql = SQLProduto._UPDATE
        cursor.execute(sql, (produto_new.nome, produto_new.descricao, produto_new.preco, produto_new.datavalidade, produto_old.idproduto))
        self.connect.commit()
        cursor.close()
        

    def delete_produto(self, idproduto):
        cursor = self.connect.cursor()
        sql = SQLProduto._DELETE.format(SQLProduto._TABLE_NAME, idproduto)
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()
        


