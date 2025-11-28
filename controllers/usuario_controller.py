from flask import Blueprint, render_template, url_for, request, redirect
from database import Sessao_base
from models.usuario import Usuario

usuario_bp = Blueprint('usuario',__name__)

@usuario_bp.route('/perfil', methods=['GET,''POST'])
def perfil():

    
    with Sessao_base() as sessao:
        perfil = sessao.query('Usuario').one()
