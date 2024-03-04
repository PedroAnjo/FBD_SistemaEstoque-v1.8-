from flask import Flask
from flask import Flask, render_template
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