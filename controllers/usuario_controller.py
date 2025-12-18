from flask import Blueprint, render_template, url_for, request, redirect, flash, session
from database import Sessao_base
from models.usuario import Usuario
from flask_login import logout_user, login_required, current_user

usuario_bp = Blueprint('usuario',__name__)


from flask import Blueprint, render_template
from flask_login import login_required, current_user

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/perfil")
@login_required
def perfil():
    return render_template("perfil.html", usuario=current_user)

