class ItemPedido:
    def __init__(self, idpedido, idproduto, nomeproduto, quantidadeproduto, idItemPedido = None ):
        self.idItemPedido = idItemPedido
        self.idpedido = idpedido
        self.idproduto = idproduto
        self.nomeproduto = nomeproduto
        self.quantidadeproduto = quantidadeproduto
       
    
    def __str__(self):
        return  f'idItemPedido: {self.idItemPedido}'\
            f'idPedido: {self.idpedido}'\
            f'\nidproduto: {self.idproduto} ' \
             f'\nnomeproduto: {self.nomeproduto} ' \
            f'\nquantidadeProduto: {self.quantidadeproduto}'
    
    def get_json(self):
        return {
            'idItemPedido': self.idItemPedido,
            'idPedido': self.idpedido,
            'idproduto': self.idproduto,
            'nomeproduto': self.nomeproduto,
            'quantidadeProduto': self.quantidadeproduto,
        }
    
    def __dict__(self):
        return {
            'idItemPedido': self.idItemPedido,
            'idproduto': self.idproduto,
            'nomeproduto': self.nomeproduto,
            'quantidadeproduto': self.quantidadeproduto
        }
    