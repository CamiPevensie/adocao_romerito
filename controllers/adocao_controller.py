from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.usuario import Usuario

adocao_bp = Blueprint("adocao", __name__)

@adocao_bp.route('/adocao')
def adocao():
    return render_template('adocao.html')