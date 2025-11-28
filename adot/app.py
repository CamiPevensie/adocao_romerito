from flask import Flask, render_template, request, redirect, url_for, flash;
from werkzeug.security import check_password_hash;
from models import engine, Usuario, Animal
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.secret_key = "SENHASUPERHIPERMEGASECRETAUAAAAAU"
Sessao_base = sessionmaker(engine)

@app.route('/')
def index():
    return render_template('index.html')
