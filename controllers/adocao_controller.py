from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database import Sessao_base
from models.usuario import Usuario
from models.animal import Animal

adocao_bp = Blueprint("adocao", __name__)

