class Cliente():
    def __init__(self, nome, cpf, dataaniversario, id=None):
        self.nome = nome
        self.cpf = cpf
        self.dataniversario = dataaniversario
        self.id = id

    def __str__(self):
        return f'ID: {self.id} - nome: {self.nome} - cpf:{self.cpf} - data:{self.dataniversario}'

    def get_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'dataaniversario': self.dataniversario,
        }