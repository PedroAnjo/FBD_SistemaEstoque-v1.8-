from flask import Blueprint, Response, jsonify, make_response, request
from modules.estoque.modelo import Estoque

from modules.estoque.dao import DAO_estoque


app_estoque = Blueprint('app_estoque', __name__)

module_name = 'estoque'
DAO_estoque = DAO_estoque()

@app_estoque.route(f'/{module_name}/', methods=['GET'])
def get_estoque():
    estoques = DAO_estoque.get_all()
    if not estoques:
        return make_response({'erro': 'Não existem produtos no estoque'})  
    return make_response(jsonify(estoques))
     


@app_estoque.route(f'/{module_name}/<id>/', methods=['GET'])
def get_produto_estoque_id(id: int):
    estoque = DAO_estoque.get_produto_estoque_id(id)
    if not estoque:
        return Response({'pedido não encontrado'}, status=404)
    return make_response(jsonify(estoque.get_json()))


@app_estoque.route(f'/{module_name}/add/', methods=['POST'])
def add_produto_no_estoque():
    data = dict(request.form)
    DAO_estoque.add_produto_no_estoque(**data)
    return make_response('Produto adicionado com sucesso!',200)


@app_estoque.route(f'/{module_name}/<idproduto>/', methods=['PUT'])
def update_estoque(idproduto):
    data = dict(request.form)
    produto_estoque = DAO_estoque.get_produto_estoque_id(idproduto)
    if not produto_estoque:
        return make_response({'Erro': f'Id do produto não encontrado:{idproduto}'}, 404)
    DAO_estoque.update_produto_estoque(idproduto,**data)
    return make_response('produto atualizado',200)
    



@app_estoque.route(f'/{module_name}/<idproduto>/', methods=['DELETE'])
def delete_produto_estoque(idproduto):
    if not DAO_estoque.get_produto_estoque_id(idproduto):
        return make_response({'Erro': f'Id do produto não encontrado:{idproduto}'}, 404)
    DAO_estoque.delete_produto_estoque(idproduto)
    return make_response('produto removido com sucesso!', 200)






