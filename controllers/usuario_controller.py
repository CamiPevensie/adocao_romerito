from flask import Blueprint, render_template, url_for, request, redirect, flash, session
from database import Sessao_base
from models.usuario import Usuario

usuario_bp = Blueprint('usuario',__name__)

@usuario_bp.route('/perfil/<int: usuario_id>', methods=['GET,''POST'])
def perfil(animal_id):
    # Se o usuário não estiver logado
    if 'usuario_id' not in session:
        flash("Faça login para continuar.", "warning")
        return redirect(url_for('auth.login'))


    
    with Sessao_base() as sessao:
        perfil = sessao.query(Usuario).filter(Usuario.id == animal_id).first()
