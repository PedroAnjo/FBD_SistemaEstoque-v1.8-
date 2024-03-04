from flask import Flask
from flask import Flask, render_template
from modules.cliente.dao import DAO_cliente
from modules.estoque.dao import DAO_estoque
from modules.produto.modelo import Produto
from modules.cliente.modelo import Cliente
from service.connect import ConnectDataBase
from modules.produto.dao import DAO_produto
from modules.estoque.controller import app_estoque
from modules.cliente.controller import app_cliente
from modules.produto.controller import app_produto
from modules.pedido.controller import app_pedido

app = Flask(__name__)
ConnectDataBase().init_table()
app.register_blueprint(app_estoque)
app.register_blueprint(app_produto)
app.register_blueprint(app_cliente)
app.register_blueprint(app_pedido)



@app.route('/')
def index():
    produtos = DAO_produto().get_all()
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    #print(DAO_produto().get_all())
    app.run(debug=True)



#DAO_estoque().add_produto_no_estoque(15,3,'22/01/2023')
#DAO_produto().update_produto()
#DAO_cliente().new_cliente(Cliente('Tailson','11923331442','09/06/2001'))
#DAO_produto().new_produto(Produto('Pringles','pote 135g', 15.00, '25/02/2025'))
#TESTES SUCESSO
# endpoint update_produto 
# endpoint delete_produto 
# endpoint new_produto 
# endpoint get_produto_id
# endpoint get_produto (all)
#print(DAO_produto().get_all())
#print(DAO_produto().get_produto_id(1)) 
#DAO_produto().new_produto(Produto('Pringles','pote 135g', 15.00, '25/02/2025'))
#DAO_estoque().add_produto_no_estoque(1, 25, '26/02/23')
#-----------------------



#print(DAO_produto().get_all())

#app.run()
