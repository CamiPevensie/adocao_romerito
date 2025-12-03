from flask import Flask, render_template
from database import Sessao_base
from models.animal import Animal

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
        print(animais)
    return render_template('index.html', animais=animais)

app.register_blueprint(autenticacao_bp, url_prefix="/auth")
app.register_blueprint(animais_bp, url_prefix="/")
app.register_blueprint(interesse_bp, url_prefix="/")
app.register_blueprint(adocao_bp, url_prefix="/")
app.register_blueprint(usuario_bp, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)
