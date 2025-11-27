from flask import Flask, render_template
from database import Sessao_base

# IMPORTA OS BLUEPRINTS
from controllers.autenticacao_controller import autenticacao_bp
from controllers.animais_controller import animais_bp
from controllers.interesse_controller import interesse_bp


app = Flask(__name__)
app.secret_key = "SENHASUPERHIPERMEGASECRETAUAAAAAU"

@app.route('/')
def index():
    return render_template('index.html')

# REGISTRA OS BLUEPRINTS
app.register_blueprint(autenticacao_bp, url_prefix="/auth")
app.register_blueprint(animais_bp, url_prefix="/")
app.register_blueprint(interesse_bp, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)
