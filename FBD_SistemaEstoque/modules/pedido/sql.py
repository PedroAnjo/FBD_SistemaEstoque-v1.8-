from modules.cliente.sql import SQLCliente
from modules.produto.sql import SQLProduto

class SQLPedido:

    _TABLE_NAME = 'pedido'
    _COL_ID = 'idPedido'
    _COL_CLIENTE_ID = 'idcliente'
    _COL_PRODUTO_ID = 'idproduto'
    _QUANTIDADE = 'quantidadeProduto'
    _DATA_PEDIDO ='dataPedido'
    _REFERENCES_CLIENTE = f'{SQLCliente._TABLE_NAME}({SQLCliente._COL_ID})'
    _REFERENCES_PRODUTO = f'{SQLProduto._TABLE_NAME}({SQLProduto._COL_ID})'

                    
    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} ' \
                    f'({_COL_ID} serial primary key, ' \
                    f'{_COL_CLIENTE_ID} int REFERENCES cliente(idcliente) on DELETE CASCADE,' \
                    f'{_DATA_PEDIDO} date NOT NULL);'
    
    _INSERT = F"INSERT INTO {_TABLE_NAME} (idcliente, dataPedido) VALUES (%s, %s) RETURNING idpedido, idcliente, datapedido"
    _SELECT = F'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _DELETE = 'DELETE FROM {} WHERE ID={}'
    _UPDATE = F'UPDATE {_TABLE_NAME} SET idcliente = {'%s'}, dataPedido = {'%s'} WHERE ID={'%s'}'