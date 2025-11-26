from sqlalchemy import Column, String, Integer, Float, Boolean
from database import Sessao_base, engine, Base

class Animal(Base):
    __tablename__ = 'animais'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False)
    raca = Column(String(40), nullable=False)
    idade = Column(Integer, nullable=False)
    sexo = Column(String(40), nullable=False)
    porte = Column(String(40), nullable=False)
    vacinado = Column(Boolean, nullable=False)
    vacinas_tomadas = Column(String(320), nullable=False)
    sobre = Column(String(320), nullable=False)
    localizacao = Column(String(100), nullable=False)
    nome_protetor = Column(String(320), nullable=False)
    telefone_contato = Column(String(15), nullable=False)
    email_contato = Column(String(100), unique=True, nullable=False)
    def __repr__(self):
        return f'<Produto {self.nome}>'
    
Base.metadata.create_all(engine)