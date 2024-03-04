from datetime import datetime
from flask import Blueprint, Response, jsonify, make_response, request
from modules.item_pedido.dao import DAO_item_pedido
from modules.pedido.modelo import Pedido
from modules.estoque.dao import DAO_estoque
from modules.pedido.dao import DAO_pedido

app_pedido = Blueprint('app_pedido', __name__)

module_name = 'pedido'
DAO_pedido = DAO_pedido()
DAO_estoque = DAO_estoque()
DAO_item_pedido = DAO_item_pedido()


@app_pedido.route(f'/{module_name}/', methods=['GET'])
def get_pedido():
    pedidos = DAO_pedido.get_all()
    if not pedidos:
         return make_response({'erro': 'Não existem pedidos realizados'})  
    return make_response(jsonify({"pedidos": pedidos}))


@app_pedido.route(f'/{module_name}/<idPedido>/', methods=['GET'])
def get_pedido_by_id(idPedido: int):
    pedido = DAO_pedido.get_pedido_id(idPedido)
    if not pedido:
        return Response({'Produto não encontrado'}, status=404)
    return make_response(jsonify(pedido.get_json()))


@app_pedido.route(f'/{module_name}/add/', methods=['POST'])
def add_pedido():
    dados_pedido = request.get_json()
    idcliente = dados_pedido.get('idcliente')
    produtos = dados_pedido.get('produtos')
    datapedido_str = dados_pedido.get('datapedido')
    datapedido = datetime.strptime(datapedido_str, "%Y-%m-%d").date()

    pedido = Pedido(idcliente, datapedido)
    pedido_gerado = DAO_pedido.add_pedido(pedido)

    for produto in produtos:
        idproduto = produto.get('idproduto')
        quantidade = produto.get('quantidade')

        quantidade_disponivel = DAO_estoque.get_quantidade(idproduto)

        if not quantidade_disponivel or quantidade_disponivel[0] < quantidade:
            return make_response(jsonify({'erro': 'quantidade indisponivel'}),404)
        else:
            DAO_item_pedido.add_item_pedido(idpedido=pedido_gerado.idpedido, idproduto=idproduto, quantidadeproduto=quantidade)
            nova_quantidade = (quantidade_disponivel[0] - quantidade)
            DAO_estoque.update_quantidade(nova_quantidade,idproduto)

    return jsonify({"mensagem": "Pedido adicionado com sucesso"})

    
#falta testar
@app_pedido.route(f'/{module_name}/<idPedido>/', methods=['DELETE'])
def delete_pedido(idPedido):
    if not DAO_pedido.delete_pedido(idPedido):
        return make_response({'Erro': f'Id do pedido não encontrado:{idPedido}'}, 404)
    DAO_pedido.delete_pedido(idPedido)
    return make_response('Pedido removido com sucesso!', 200)




        
#@app_pedido.route(f'/{module_name}/add/', methods=['POST'])
#def add_pedido():
#    dado_pedido = request.get_json()
#    produto_ids = dado_pedido['idproduto']
#    quantidade_pedidos = int(dado_pedido['quantidadeproduto',0])
#    idCliente = dado_pedido['idcliente']
#    dataPedido = dado_pedido['datapedido']
    
#    pedido = Pedido(idCliente, dataPedido)
#    DAO_pedido.add_pedido(pedido)

#    for i in range(len(idCliente)):
#        idproduto = produto_ids[i]
#        quantidadeproduto = quantidade_pedidos[i]
#        quantidade_disponivel = DAO_estoque.get_quantidade(idproduto)
#        if quantidade_disponivel and quantidade_disponivel[0] >= quantidadeproduto:

#           DAO_item_pedido.add_item_pedido(pedido.idpedido, idproduto, quantidadeproduto)
#            nova_quantidade = (quantidade_disponivel[0] - quantidadeproduto)
#            DAO_estoque.update_quantidade(nova_quantidade,idproduto)
#    return jsonify({'mensagem': 'pedido adicionado com sucesso!'})
    
        #return make_response(jsonify({'erro': f'pedido não adicionado. Quantidade insuficiente no estoque'}),404)
    #dado_pedido = dict(request.form)
    #idproduto = dado_pedido.get('idproduto')
    #quantidade_pedido = int(dado_pedido.get('quantidadeproduto',0))
    #idCliente = dado_pedido.get('idcliente')
    #dataPedido = dado_pedido.get('datapedido')
