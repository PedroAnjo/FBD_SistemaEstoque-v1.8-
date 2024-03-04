class Pedido:
    def __init__(self, idcliente, datapedido, idpedido = None ):
        self.idpedido = idpedido
        self.idcliente = idcliente
        self.datapedido = datapedido
    
    
    def __str__(self):
        return f'idPedido: {self.idpedido}'\
            f'\nidCliente: {self.idcliente} ' \
            f'\ndataPedido:{self.datapedido}'
    
    
    def get_json(self):
        return {
            'idPedido': self.idpedido,
            'idCliente': self.idcliente,
            'dataPedido': self.datapedido
        }
    