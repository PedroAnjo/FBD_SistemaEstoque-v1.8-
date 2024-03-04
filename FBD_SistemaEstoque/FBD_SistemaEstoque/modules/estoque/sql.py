class SQLEstoque:
    _TABLE_NAME = 'estoque'
    _COL_ID_PRODUTO = 'idProduto'
    _COL_NOME_PRODUTO = 'nomeProduto'
    _COL_DATA = 'dataEntrada'
    _COL_QUANTI_PRODUTO='quantidadeEstoque'

    
    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME}'\
                    f'(id SERIAL PRIMARY KEY,'\
                    f'{ _COL_ID_PRODUTO } INT REFERENCES produto(idproduto) ON DELETE CASCADE,'\
                    f'{ _COL_NOME_PRODUTO } VARCHAR(255) NOT NULL,'\
                    f'{ _COL_QUANTI_PRODUTO } INT NOT NULL,'\
                    f'{ _COL_DATA } VARCHAR(15) NOT NULL);'
    
    
    _INSERT = F"INSERT INTO {_TABLE_NAME} (idProduto, nomeProduto, quantidadeEstoque, dataEntrada) VALUES (%s, %s, %s, %s)"
    _SELECT = F'select * from {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM estoque WHERE idproduto ={}'
    _SELECT_QUANTIDADE_BY_ID = 'SELECT quantidadeestoque FROM estoque WHERE idproduto={}'
    _SCRIPT_SELECT_BUSCA = F"SELECT * FROM {_TABLE_NAME} WHERE nome ILIKE %"
    _DELETE = 'DELETE FROM {} WHERE IDPRODUTO={}'
    _UPDATE = F'UPDATE {_TABLE_NAME} SET  quantidadeestoque = {'%s'}, dataentrada = {'%s'} WHERE IDPRODUTO={'%s'}'
    _UPDATE_QUANTIDADE = F'UPDATE {_TABLE_NAME} SET quantidadeestoque = {'%s'} WHERE IDPRODUTO={'%s'}'