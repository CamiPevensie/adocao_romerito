from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import Sessao_base
from models.animal import Animal
from models.interesse import Interesse
from models.adocao import Adocao
import os 
from werkzeug.utils import secure_filename
animais_bp = Blueprint("animais", __name__)
# animais_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import Sessao_base
from models.animal import Animal
from models.interesse import Interesse
from models.adocao import Adocao

animais_bp = Blueprint("animais", __name__)

@animais_bp.route('/', methods=['GET'])
def animais():
    with Sessao_base() as sessao:
        animais = sessao.query(Animal).all()
    return render_template('animais.html', animais=animais)


@animais_bp.route('/detalhes_animal/<int:animal_id>', methods=['GET'])
def detalhes_animal(animal_id):
    with Sessao_base() as sessao:
        animal = sessao.query(Animal).get(animal_id)
    return render_template('detalhes_animal.html', animal=animal)


@animais_bp.route('/cadastrar_animal', methods=['GET', 'POST'])
def cadastrar_animal():
    if request.method == 'POST':
        nome = request.form['nome_form']
        raca = request.form['raca_form']
        idade = int(request.form['idade_form'])
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

        animal = Animal(
            nome=nome, raca=raca, idade=idade, sexo=sexo, porte=porte,
            vacinado=vacinado, vacinas_tomadas=vacinas_tomadas, sobre=sobre,
            localizacao=localizacao, nome_protetor=nome_protetor,
            telefone_contato=telefone_contato, email_contato=email_contato,
            foto=foto_animal
        )

        with Sessao_base() as sessao:
            sessao.add(animal)
            sessao.commit()

        flash("Animal cadastrado com sucesso!", "success")
        return redirect(url_for('animais.animais_para_adocao'))

    return render_template('cadastrar_animal.html')


@animais_bp.route('/animais_para_adocao', methods=['GET'])
def animais_para_adocao():
    with Sessao_base() as sessao:
        animais = sessao.query(Animal).all()
    return render_template('adocao.html', animais=animais)


@animais_bp.route('/ver_animal/<int:animal_id>', methods=['GET', 'POST'])
def ver_animal(animal_id):

    # Verificar login
    if 'usuario_id' not in session:
        flash("Faça login para continuar.", "warning")
        return redirect(url_for('auth.login'))

    with Sessao_base() as sessao:
        animal = sessao.query(Animal).filter_by(id=animal_id).first()

        if not animal:
            flash("Animal não encontrado.", "danger")
            return redirect(url_for('animais.animais'))

        # Quando o usuário apertar um botão
        if request.method == 'POST':
            acao = request.form.get("acao")

            # --- LISTA DE INTERESSE ---
            if acao == "interesse":
                existe = sessao.query(Interesse).filter_by(
                    usuario_id=session['usuario_id'],
                    animal_id=animal.id
                ).first()

                if existe:
                    flash("Este animal já está nos seus interesses.", "info")
                else:
                    novo = Interesse(
                        usuario_id=session['usuario_id'],
                        animal_id=animal.id
                    )
                    sessao.add(novo)
                    sessao.commit()
                    flash("Animal adicionado aos seus interesses!", "success")

                return redirect(url_for('interesse.interesse'))

            # --- ADOÇÃO ---
            if acao == "adotar":
                existe = sessao.query(Adocao).filter_by(
                    usuario_id=session['usuario_id'],
                    animal_id=animal.id
                ).first()

                if existe:
                    flash("Você já solicitou adoção deste animal.", "info")
                else:
                    nova = Adocao(
                        usuario_id=session['usuario_id'],
                        animal_id=animal.id,
                        status="pendente"
                    )
                    sessao.add(nova)
                    sessao.commit()
                    flash("Adoção solicitada!", "success")

                return redirect(url_for('adocao.animais_adocoes_usuario'))

    # GET → página do animal
    return render_template('detalhes_animal.html', animal=animal)
