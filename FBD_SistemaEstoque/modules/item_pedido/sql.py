class SQLItemPedido:
    _TABLE_NAME = 'itemPedido'
    _COL_ID = 'idItemPedido'
    _COL_ID_PEDIDO ='idpedido'
    _COL_ID_PRODUTO = 'idproduto'
    _QUANTIDADE = 'quantidadeProduto'
    _VALOR_PRODUTO = 'valorproduto'
    _COL_NOME_PRODUTO = 'nomeproduto'

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} ' \
                    f'({_COL_ID} serial primary key, ' \
                    f'{_COL_ID_PEDIDO} int REFERENCES pedido(idpedido) on DELETE CASCADE, ' \
                    f'{_COL_ID_PRODUTO} int REFERENCES produto(idproduto) on DELETE CASCADE,' \
                    f'{ _COL_NOME_PRODUTO } VARCHAR(255) NOT NULL,'\
                    f'{_VALOR_PRODUTO} FLOAT NOT NULL,'\
                    f'{_QUANTIDADE} int NOT NULL);'
    
    _INSERT = F"INSERT INTO {_TABLE_NAME} (idpedido, idproduto, nomeproduto, valorproduto, quantidadeproduto) VALUES (%s, %s, %s, %s, %s)"
    _SELECT = F'SELECT * FROM {_TABLE_NAME}'
    #_SELECT_BY_ID = 'SELECT * FROM {} WHERE idpedido={}'
    _SELECT_BY_ID = 'SELECT idItemPedido, idpedido, idproduto, nomeproduto, quantidadeproduto  FROM {} WHERE idpedido={}'
    _DELETE = 'DELETE FROM {} WHERE ID={}'
    
