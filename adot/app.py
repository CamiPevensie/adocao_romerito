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

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
