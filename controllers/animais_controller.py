from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import Sessao_base
from models.animal import Animal
from flask_login import login_required, current_user

animais_bp = Blueprint("animais", __name__)


@animais_bp.route('/', methods=['GET'])
def animais():
    with Sessao_base() as sessao:
        animais = sessao.query(Animal).all()
    return render_template('animais.html', animais=animais)

@animais_bp.route('/detalhes_animal/<int:animal_id>', methods=['GET'])
def detalhes_animal(animal_id):
    with Sessao_base() as sessao:
        animal = sessao.get(Animal, animal_id)
        if animal is None:
            return "Animal não encontrado", 404
        dono = (
            current_user.is_authenticated and current_user.id == animal.usuario_cad_id
        )
    return render_template('detalhes_animal.html', animal=animal, dono=dono)

@animais_bp.route('/remover_animal', methods=["GET", "POST"])
def remover_animal():
    animal_id = request.form.get('id')

    if not animal_id:
        flash("ID não recebido.", category="error")
        return redirect(url_for('animais.animais')) 

##########        --- editandoo aquii --- 
@animais_bp.route('/editar_animais/<int:animal_id>', methods=["GET", "POST"])
@login_required
def editar_animais(animal_id):
    with Sessao_base() as sessao:
        animal = sessao.query(Animal).filter_by(id=animal_id).first()
    if not animal:
        flash("Animal não encontrado.", "error")
        return redirect(url_for('animais.animais'))
    if request.method == 'POST':
        animal.nome = request.form['nome_form']
        animal.raca = request.form['raca_form']
        animal.idade = request.form['idade_form']
        animal.sexo = request.form['sexo_form']
        animal.porte = request.form['porte_form']
        animal.vacinado = request.form.get('vacinado_form') == 'on'
        animal.vacinas_tomadas = request.form['vacinas_tomadas_form']
        animal.sobre = request.form['sobre_form']
        animal.localizacao = request.form['localizacao_form']
        animal.nome_protetor = request.form['nome_protetor_form']
        animal.telefone_contato = request.form['telefone_contato_form']
        animal.email_contato = request.form['email_contato_form']
        animal.foto_animal = request.form['foto_form']
        animal.usuario_id = current_user.id
    
        sessao.commit()
        flash("Animal atualizado com sucesso!", "success")
        return redirect(url_for('animais.animais')) 
    return render_template('editar_animais.html', animal=animal)


@animais_bp.route('/cadastrar_animal', methods=['GET', 'POST'])
@login_required
def cadastrar_animal():

    if request.method == 'POST':
        nome = request.form['nome_form']
        raca = request.form['raca_form']
        idade = request.form['idade_form']
        sexo = request.form['sexo_form']
        porte = request.form['porte_form']
        vacinado = request.form.get('vacinado_form') == 'on'
        vacinas_tomadas = request.form['vacinas_tomadas_form']
        sobre = request.form['sobre_form']
        localizacao = request.form['localizacao_form']
        nome_protetor = request.form['nome_protetor_form']
        telefone_contato = request.form['telefone_contato_form']
        email_contato = request.form['email_contato_form']
        foto_animal = request.form['foto_form']
        usuario_id = current_user.id

        if not all([nome, idade, sexo, porte, localizacao,nome_protetor, telefone_contato, email_contato, foto_animal]):
            flash("Preencha todos os campos obrigatórios.", "error")
            return redirect(url_for('animais.cadastrar_animal'))

        animal = Animal(nome=nome, raca=raca, idade=idade, sexo=sexo, porte=porte, vacinado=vacinado, vacinas_tomadas=vacinas_tomadas, sobre=sobre,
        localizacao=localizacao, nome_protetor=nome_protetor, telefone_contato=telefone_contato, email_contato=email_contato,
        foto=foto_animal, usuario_cad_id=usuario_id)

        with Sessao_base() as sessao_db:
            sessao_db.add(animal)
            sessao_db.commit()

        flash("Animal cadastrado com sucesso!", "success")
        return redirect(url_for('animais.animais_para_adocao'))

    return render_template('cadastrar_animal.html')

@animais_bp.route('/animais_adocoes_usuario', methods=['GET'])
def animais_para_adocao():
    with Sessao_base() as sessao:
        animais = sessao.query(Animal).all()
    return render_template('adocao.html', animais=animais)
