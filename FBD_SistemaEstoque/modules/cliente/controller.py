from flask import Blueprint, Response, jsonify, make_response, request
from modules.cliente.dao import DAO_cliente
from modules.cliente.modelo import Cliente

app_cliente = Blueprint('app_cliente', __name__)

module_name = 'cliente'
DAO_cliente = DAO_cliente()

@app_cliente.route(f'/{module_name}/', methods=['GET'])
def get_cliente():
    clientes = DAO_cliente.get_all()
    return make_response(jsonify(clientes))


@app_cliente.route(f'/{module_name}/<id>', methods=['GET'])
def get_cliente_id(id: int):
    cliente = DAO_cliente.get_cliente_id(id)
    if not cliente:
        return Response({}, status=404)
    return make_response(jsonify(cliente.get_json()))


@app_cliente.route(f'/{module_name}/add/', methods=['POST'])
def new_cliente():
    data_cliente = dict(request.form)
    cliente = Cliente(**data_cliente)
    DAO_cliente.new_cliente(cliente)
    return make_response(cliente.get_json())
    

@app_cliente.route(f'/{module_name}/<id>/', methods=['PUT'])
def update_cliente(id):
    data_cliente = dict(request.form)
    cliente_old = DAO_cliente.get_cliente_id(id)
    if not cliente_old:
        return make_response({'Erro': f'Id do cliente não encontrado:{id}'}, 404)
    
    cliente_new = Cliente(**data_cliente, id= cliente_old.id)
    DAO_cliente.update_cliente(cliente_old, cliente_new)
    return make_response(cliente_new.get_json())

@app_cliente.route(f'/{module_name}/<id>/', methods=['DELETE'])
def delete_cliente(id):
    if not DAO_cliente.get_cliente_id(id):
         return make_response({'Erro': f'Id do cliente não encontrado:{id}'}, 404)
    DAO_cliente.delete_cliente(id)
    return make_response('Cliente removido com sucesso!', 200)