from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from sqlalchemy.orm import joinedload
from database import Sessao_base
from models.adocao import Adocao

adocao_bp = Blueprint("adocao", __name__)

@adocao_bp.route('/animais_adocoes_usuario')
def animais_adocoes_usuario():
    usuario_id = session.get('usuario_id')

    if not usuario_id:
        return redirect(url_for('auth.login'))

    with Sessao_base() as sessao:
        adocoes = sessao.query(Adocao)\
            .options(joinedload(Adocao.animal))\
            .filter_by(usuario_id=usuario_id)\
            .all()

    return render_template('adocao.html', adocoes=adocoes)

@adocao_bp.route('/adotar/<int:animal_id>', methods=['POST'])
def adotar(animal_id):
    usuario_id = session.get('usuario_id')

    if not usuario_id:
        return redirect(url_for('auth.login'))

    with Sessao_base() as sessao:
        nova_adocao = Adocao(usuario_id=usuario_id, animal_id=animal_id)
        sessao.add(nova_adocao)
        sessao.commit()

    flash("Adoção solicitada com sucesso!", "success")
    return redirect(url_for('adocao.animais_adocoes_usuario'))
