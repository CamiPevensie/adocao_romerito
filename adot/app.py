from flask import Flask, render_template, request, redirect, url_for, flash;
from werkzeug.security import check_password_hash;
from modelo import engine, Usuario, Produto
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.secret_key = "SENHASUPERHIPERMEGASECRETAUAAAAAU"
Sessao_base = sessionmaker(engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adocao')
def adocao():
    return render_template('adocao.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/mascotes')
def mascotes():
    return render_template('mascotes.html')

@app.route('/cadastro', methods = ['GET','POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome_completo_form']
        nome_completo = request.form['nome_form']
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
        with Sessao_base as sessao:
            sessao.add(usuario)
            sessao.commit()
        return redirect(url_for('index'))
    return render_template('cadastro.html')

@app.route('/cadastrar_animal')
def cadastrar_animal():
    return render_template()