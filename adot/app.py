from flask import Flask, render_template, request, redirect, url_for, flash;
from werkzeug.security import check_password_hash;
from modelo import engine, Usuario, Animal
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

@app.route('/animais')
def mascotes():
    return render_template('animais.html')


@app.route('/cadastrar_animal', methods = ['GET','POST'])
def cadastrar_animal():
    if request.method =='POST':
        nome = request.form['nome_form']
        raca = request.form['raca_form']
        idade = request.form['idade_form']
        sexo = request.form['sexo_form']
        porte = request.form['porte_form']
        vacinado = request.form['vacinado_form']
        vacinas_tomadas = request.form['vacinas_tomadas_form']
        sobre = request.form['sobre_form']
        localizacao = request.form['localizacao_form']
        nome_protetor = request.form['nome_protetor_form']
        telefone_contato = request.form['telefone_contato_form']
        email_contato = request.form['email_contato_form']
    return render_template()
