from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import (
    LoginManager, login_user, logout_user,
    login_required, current_user
)
from models.usuario import Usuario
from database import Sessao_base

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    with Sessao_base() as sessao:
        return sessao.get(Usuario, int(user_id))

autenticacao_bp = Blueprint("auth", __name__)

@autenticacao_bp.route("/login", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == 'POST':
        email = request.form['email_form']
        senha = request.form['senha_form']
        with Sessao_base() as sessao:
            usuario = sessao.query(Usuario).filter_by(email=email).first()
            if usuario and usuario.senha == senha:
                login_user(usuario)
                return redirect(url_for("usuario.perfil"))
            else:
                erro = "Usuário ou senha inválidos"
    return render_template('login.html', erro=erro)

@autenticacao_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash("Logout realizado com sucesso!", "success")
    return redirect(url_for('auth.login'))
