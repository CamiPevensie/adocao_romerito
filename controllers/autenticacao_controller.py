from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models.usuario import Usuario
from database import Sessao_base
login_manager = LoginManager()
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    db = Sessao_base()
    try:
        return db.get(Usuario, int(user_id))
    finally:
        db.close

autenticacao_bp = Blueprint("auth", __name__)

@autenticacao_bp.route("/debug")
def debug():
    return{
        "is authenticated": current_user.is_authenticated,
        "id": current_user.get_id() if current_user.is_authenticated else None
    }

@autenticacao_bp.route("forceL")
def forceL():
    usuario = Usuario.query.first()
    login_user(usuario)
    return "logado"

@autenticacao_bp.route("/login", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == 'POST':
        email = request.form['email_form']
        senha = request.form['senha_form']
        
        with Sessao_base() as sessao:
            usuario = sessao.query(Usuario).filter_by(email=email).first()
            print(usuario)
        if usuario and usuario.senha == senha:
            session['usuario_id'] = usuario.id
            return render_template('perfil.html', usuario=usuario)
        else:
            erro = "Usuário ou senha inválidos"
    return render_template('login.html', erro=erro)

from flask import request, flash, redirect, url_for

@autenticacao_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome_form'].strip()
        nome_completo = request.form['nome_completo_form'].strip()
        telefone = request.form['telefone_form'].strip()
        email = request.form['email_form'].strip()
        senha = request.form['senha_form'].strip()
        rua = request.form['rua_form'].strip()
        bairro = request.form['bairro_form'].strip()
        cidade = request.form['cidade_form'].strip()
        numero = request.form['numero_form'].strip()
        complemento = request.form['complemento_form'].strip()
        estado = request.form['estado_form'].strip()

        campos_obrigatorios = [nome, nome_completo, telefone, email, senha,rua, bairro, cidade, numero, estado]

        for campo in campos_obrigatorios:
            if not campo:
                flash('Preencha todos os campos obrigatórios!', 'error')
                return redirect(url_for('auth.cadastro'))

        usuario = Usuario(nome=nome,nome_completo=nome_completo,telefone=telefone,email=email,senha=senha,rua=rua,bairro=bairro,cidade=cidade,numero=numero,complemento=complemento,estado=estado)

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




