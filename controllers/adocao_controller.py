from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.orm import joinedload
from flask_login import login_required, current_user
from database import Sessao_base
from models.adocao import Adocao

adocao_bp = Blueprint("adocao", __name__)

@adocao_bp.route('/animais_adocoes_usuario')
@login_required
def animais_adocoes_usuario():
    usuario_id = current_user.id
    with Sessao_base() as sessao:
        adocoes = (
            sessao.query(Adocao)
            .options(joinedload(Adocao.animal))
            .filter(Adocao.usuario_id == usuario_id)
            .all())
    return render_template('adocao.html', adocoes=adocoes)


@adocao_bp.route('/adotar/<int:animal_id>', methods=['POST'])
@login_required
def adotar(animal_id):
    usuario_id = current_user.id

    with Sessao_base() as sessao:
        adocao_existente = sessao.query(Adocao).filter(
            Adocao.usuario_id == usuario_id,
            Adocao.animal_id == animal_id
        ).first()
        if adocao_existente:
            flash("Você já adotou este animal!", "warning")
            return redirect(url_for('adocao.animais_adocoes_usuario'))
        nova_adocao = Adocao(
            usuario_id=usuario_id,
            animal_id=animal_id
        )
        sessao.add(nova_adocao)
        sessao.commit()
    flash("Adoção cadastrada com sucesso!", "success")
    return redirect(url_for('adocao.animais_adocoes_usuario'))


@adocao_bp.route('/desfazer_adocao/<int:animal_id>', methods=['POST'])
@login_required
def desfazer_adocao(animal_id):
    usuario_id = current_user.id

    with Sessao_base() as sessao:
        adocao = sessao.query(Adocao).filter(Adocao.usuario_id == usuario_id,
        Adocao.animal_id == animal_id).first()
        if adocao:
            sessao.delete(adocao)
            sessao.commit()
            flash("Adoção desfeita com sucesso!", "success")
        else:
            flash("Nenhuma adoção encontrada para desfazer.", "warning")

    return redirect(url_for('adocao.animais_adocoes_usuario'))
