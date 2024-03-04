class SQLProduto:
    _TABLE_NAME = 'produto'
    _COL_ID = 'idproduto'
    _COL_NOME ='nome'
    _COL_DESCRICAO= 'descricao'
    _COL_PRECO='preco'
    _COL_DATA_VALIDADE = 'dataValidade'

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME}'\
                    f'({_COL_ID} SERIAL PRIMARY KEY,'\
                    f'{ _COL_NOME } VARCHAR(255) UNIQUE,'\
                    f'{ _COL_DESCRICAO } VARCHAR(255) NOT NULL,'\
                    f'{ _COL_PRECO } FLOAT NOT NULL,'\
                    f'{_COL_DATA_VALIDADE} VARCHAR(15) NOT NULL);'
    
    _INSERT = F"INSERT INTO {_TABLE_NAME} (nome, descricao, preco, dataValidade) VALUES (%s, %s, %s, %s)"
    _SELECT = F'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE idproduto={}'
    _SELECT_BY_NOME = 'SELECT * FROM {} WHERE nome = {}'
    _DELETE = 'DELETE FROM {} WHERE ID={}'
    _UPDATE = F'UPDATE {_TABLE_NAME} SET nome = {'%s'},descricao = {'%s'},preco = {'%s'}, dataValidade = {'%s'} WHERE ID={'%s'}'
