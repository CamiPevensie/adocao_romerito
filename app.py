from flask import Flask, render_template, request, redirect, url_for, flash;
from werkzeug.security import check_password_hash;
from models.usuario import Usuario
from models.animal import Animal
from sqlalchemy import create_engine, Column, String, Integer, Float
from database import Sessao_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.secret_key = "SENHASUPERHIPERMEGASECRETAUAAAAAU"

@app.route('/')
def index():
    return render_template('index.html')

