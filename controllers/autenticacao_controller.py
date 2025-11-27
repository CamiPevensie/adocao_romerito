from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.usuario import Usuario
from typing import Optional
from database import Sessao_base

autenticacao_bp = Blueprint("auth", __name__)

@autenticacao_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email_form']
        senha = request.form['senha_form']

        with Sessao_base() as sessao:
            usuario = sessao.query(Usuario).filter_by(email=email).first()
            print(usuario)
            if usuario and usuario.senha == senha:
                return f"Login bem-sucedido! Bem-vindo {usuario.nome}!"
            else:
                return "Usuário ou senha inválidos"
    return render_template('login.html')

@autenticacao_bp.route('/cadastro', methods = ['GET','POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome_form']
        nome_completo = request.form['nome_completo_form']
        telefone = request.form['telefone_form']
        email = request.form['email_form']
        senha = request.form['senha_form']
        rua = request.form['rua_form']
        bairro = request.form['bairro_form']
        cidade = request.form['cidade_form']
        numero = request.form['numero_form']
        complemento = request.form['complemento_form']
        estado = request.form['estado_form']

        usuario = Usuario(nome=nome, nome_completo=nome_completo, telefone=telefone, email=email, senha=senha, rua=rua, bairro=bairro, cidade=cidade, numero=numero, complemento=complemento, estado=estado)
        with Sessao_base() as sessao:
            sessao.add(usuario)
            sessao.commit()
        return redirect(url_for('index'))
    return render_template('cadastro.html')

@autenticacao_bp.route('/logout')
def logout():
    session.clear()  
    flash("Logout realizado com sucesso!", "success")
    return redirect(url_for('auth.login')) 




