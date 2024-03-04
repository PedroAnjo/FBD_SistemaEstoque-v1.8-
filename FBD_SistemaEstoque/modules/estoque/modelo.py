class Estoque:
    
    def __init__(self, idproduto,nomeproduto,quantidadeestoque, dataentrada, id=None):
        self.id = id
        self.idproduto = idproduto
        self.nomeproduto = nomeproduto
        self.quantidadeestoque =quantidadeestoque
        self.dataentrada = dataentrada
    
    
    def __str__(self):
        return f'id: {self.id}'\
            f'\nid produto: {self.idproduto} ' \
            f'\nnome produto: {self.nomeproduto}'\
            f'\nquantidade estoque: {self.quantidadeestoque}'\
            f'\ndata entrada: {self.dataentrada}'
    
    def get_json(self):
        return {
            'id': self.id,
            'idproduto': self.idproduto,
            'nomeproduto': self.nomeproduto,
            'quantidadeestoque': self.quantidadeestoque,
            'dataentrada': self.dataentrada
        }