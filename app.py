from flask import Flask, render_template
from database import Sessao_base
from models.animal import Animal
import random

from controllers.autenticacao_controller import autenticacao_bp
from controllers.animais_controller import animais_bp
from controllers.interesse_controller import interesse_bp
from controllers.adocao_controller import adocao_bp
from controllers.usuario_controller import usuario_bp

app = Flask(__name__)
app.secret_key = "SENHASUPERHIPERMEGASECRETAUAAAAAU"

@app.route('/')
def index():
    with Sessao_base() as sessao:
        animais = sessao.query(Animal).all()
        total_animais = len(animais)
        quantidade = min(5, total_animais)
        animais_sorteados = random.sample(animais, quantidade)

    return render_template('index.html', animais=animais_sorteados)

app.register_blueprint(autenticacao_bp, url_prefix="/auth")
app.register_blueprint(animais_bp, url_prefix="/animais")
app.register_blueprint(interesse_bp, url_prefix="/interesse")
app.register_blueprint(adocao_bp, url_prefix="/adocao")
app.register_blueprint(usuario_bp, url_prefix="/usuario")

print("ROTAS REGISTRADAS:")
print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
