from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import (
    LoginManager, login_user, logout_user,
    login_required, current_user
)
from models.usuario import Usuario
from database import Sessao_base
from typing import Optional

login_manager = LoginManager()
login_manager.login_view = "auth.login"  # type: ignore

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

@autenticacao_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome_form')
        nome_completo = request.form.get('nome_completo_form')
        telefone = request.form.get('telefone_form')
        email = request.form.get('email_form')
        senha = request.form.get('senha_form')
        rua = request.form.get('rua_form')
        bairro = request.form.get('bairro_form')
        cidade = request.form.get('cidade_form')
        numero = request.form.get('numero_form')
        complemento = request.form.get('complemento_form')
        estado = request.form.get('estado_form')

        with Sessao_base() as sessao:
            usuario_existente = sessao.query(Usuario).filter_by(email=email).first()
            if usuario_existente:
                flash("Este e-mail já está cadastrado.", "erro")
                return render_template('cadastro.html')

            novo_usuario = Usuario(nome=nome, nome_completo=nome_completo,
            telefone=telefone, email=email, senha=senha,
            rua=rua, bairro=bairro, cidade=cidade,
            numero=numero, complemento=complemento, estado=estado)

            sessao.add(novo_usuario)
            sessao.commit()

        flash("Cadastro realizado com sucesso! Faça login.", "success")
        return redirect(url_for('index'))

    return render_template('cadastro.html')

@autenticacao_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash("Logout realizado com sucesso!", "success")
    return redirect(url_for('auth.login'))
