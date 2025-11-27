from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import Sessao_base
from models.animal import Animal

animais_bp = Blueprint("animais", __name__)

@animais_bp.route('/cadastrar_animal', methods=['GET', 'POST'])
def cadastrar_animal():
    if request.method == 'POST':
        nome = request.form['nome_form']
        raca = request.form['raca_form']
        idade = int(request.form['idade_form'])
        sexo = request.form['sexo_form']
        porte = request.form['porte_form']
        # Checkbox retorna 'on' se marcado, None se desmarcado
        vacinado = request.form.get('vacinado_form') == 'on'
        vacinas_tomadas = request.form['vacinas_tomadas_form']
        sobre = request.form['sobre_form']
        localizacao = request.form['localizacao_form']
        nome_protetor = request.form['nome_protetor_form']
        telefone_contato = request.form['telefone_contato_form']
        email_contato = request.form['email_contato_form']

        # Cria o objeto Animal
        animal = Animal(
            nome=nome,
            raca=raca,
            idade=idade,
            sexo=sexo,
            porte=porte,
            vacinado=vacinado,
            vacinas_tomadas=vacinas_tomadas,
            sobre=sobre,
            localizacao=localizacao,
            nome_protetor=nome_protetor,
            telefone_contato=telefone_contato,
            email_contato=email_contato
        )

        # Adiciona ao banco de dados
        with Sessao_base() as sessao:
            sessao.add(animal)
            sessao.commit()

        flash("Animal cadastrado com sucesso!", "success")
        return redirect(url_for('animais.animais'))

    return render_template('cadastrar_animal.html')

@animais_bp.route('/animais')
def animais():
    # Aqui você pode adicionar a consulta para listar os animais no template
    with Sessao_base() as sessao:
        lista_animais = sessao.query(Animal).all()
    return render_template('animais.html', animais=lista_animais)
