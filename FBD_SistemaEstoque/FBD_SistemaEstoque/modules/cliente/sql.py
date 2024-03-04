class SQLCliente:
    _TABLE_NAME = 'cliente'
    _COL_ID = 'idCliente'
    _COL_NOME ='nome'
    _COL_CPF= 'CPF'
    _COL_DATA_ANIVERSARIO = 'dataAniversario'

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME}'\
                    f'({_COL_ID} SERIAL PRIMARY KEY,'\
                    f'{ _COL_NOME } VARCHAR(255) UNIQUE,'\
                    f'{ _COL_CPF } VARCHAR(255) NOT NULL,'\
                    f'{_COL_DATA_ANIVERSARIO} VARCHAR(15) NOT NULL);'
    
    _INSERT = F"INSERT INTO {_TABLE_NAME} (nome, cpf, dataaniversario) VALUES ( %s, %s, %s)"
    _SELECT = F'SELECT * FROM {_TABLE_NAME}'
    _SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _DELETE = 'DELETE FROM {} WHERE ID={}'
    _UPDATE = F'UPDATE {_TABLE_NAME} SET nome = {'%s'},cpf = {'%s'}, dataaniversario = {'%s'} WHERE ID={'%s'}'