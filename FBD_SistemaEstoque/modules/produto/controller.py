from flask import Blueprint, Response, jsonify, make_response, request
from modules.produto.dao import DAO_produto
from modules.produto.modelo import Produto

app_produto = Blueprint('app_produto', __name__)

module_name = 'produto'
DAO_produto = DAO_produto()

@app_produto.route(f'/{module_name}/', methods=['GET'])
def get_produto():
    produtos = DAO_produto.get_all()
    return make_response(jsonify(produtos))


@app_produto.route(f'/{module_name}/<id>', methods=['GET'])
def get_produto_id(id: int):
    produto = DAO_produto.get_produto_id(id)
    if not produto:
        return Response({}, status=404)
    return make_response(jsonify(produto.get_json()))



@app_produto.route(f'/{module_name}/add/', methods=['POST'])
def new_produto():
    data_produto = dict(request.form)
    produto = Produto(**data_produto)
    DAO_produto.new_produto(produto)
    return make_response(produto.get_json())


@app_produto.route(f'/{module_name}/<id>/', methods=['PUT'])
def update_produto(id):
    data_produto = dict(request.form)
    produto_old = DAO_produto.get_produto_id(id)
    if not produto_old:
        return make_response({'Erro': f'Id do produto não encontrado:{id}'}, 404)
    
    produto_new = Produto(**data_produto, id= produto_old.id)
    DAO_produto.update_produto(produto_old, produto_new)
    return make_response(produto_new.get_json())

@app_produto.route(f'/{module_name}/<id>/', methods=['DELETE'])
def delete_produto(id):
    if not DAO_produto.get_produto_id(id):
         return make_response({'Erro': f'Id do produto não encontrado:{id}'}, 404)
    DAO_produto.delete_produto(id)
    return make_response('Produto removido com sucesso!', 200)