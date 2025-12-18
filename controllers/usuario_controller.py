from flask import Blueprint, render_template, url_for, request, redirect, flash, session
from database import Sessao_base
from models.usuario import Usuario
from flask_login import logout_user, login_required, current_user

usuario_bp = Blueprint('usuario',__name__)


@usuario_bp.route('/perfil', methods=['GET','POST'])
@login_required
def perfil():
    # Se o usuário não estiver logado
    return render_template('perfil.html', usuario=current_user)

@usuario_bp.route('/logout', methods=["POST", "GET"])
def logout():
    logout_user()  # encerra a sessão do usuário logado
    return redirect(url_for('index'))

