class Produto:

    def __init__(self,nome, descricao, preco, datavalidade, idproduto=None):
        self.idproduto = idproduto
        self.nome= nome
        self.descricao= descricao
        self.preco = preco
        self.datavalidade = datavalidade

    def __str__(self):
        return f'idproduto: {self.idproduto}'\
            f'\nnome: {self.nome} ' \
            f'\ndescricao: {self.descricao}'\
            f'\npreco:{self.preco}'\
            f'\ndataValidade:{self.datavalidade}'
    
    def get_json(self):
        return {
            'idproduto': self.idproduto,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco,
            'dataValidade': self.datavalidade
        }