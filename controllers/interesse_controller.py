from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database import Sessao_base
from models.interesse import Interesse
from models.usuario import Usuario
from models.animal import Animal

interesse_bp = Blueprint("interesse", __name__)

# Página para solicitar adoção de um animal
@interesse_bp.route('/interesse/<int:animal_id>', methods=['GET', 'POST'])
def solicitar_interesse(animal_id):
    if 'usuario_id' not in session:
        flash("Você precisa estar logado para adotar.", "warning")
        return redirect(url_for('auth.login'))

    with Sessao_base() as sessao:
        animal = sessao.query(Animal).filter(Animal.id == animal_id).first()
        if not animal:
            flash("Animal não encontrado.", "danger")
            return redirect(url_for('animais.animais'))

        if request.method == 'POST':
            endereco = request.form['endereco_form']
            condicoes = request.form['condicoes_form']
            motivacao = request.form['motivacao_form']

            interesse = Interesse(
                usuario_id=session['usuario_id'],
                animal_id=animal.id,
                endereco=endereco,
                condicoes_economicas=condicoes,
                motivacao=motivacao
            )
            sessao.add(interesse)
            sessao.commit()

            flash("Solicitação enviada! aguarde avaliação do administrador.", "success")
            return redirect(url_for('animais.animais'))

    return render_template('solicitar_interesse.html', animal=animal)
