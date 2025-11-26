from sqlalchemy import create_engine, Column, String, Integer, Float
from database import Sessao_base, engine, Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False)
    nome_completo = Column(String(320), nullable=False)
    telefone = Column(String(15), nullable=False)
    email = Column(String(320), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)
    rua = Column(String(40), nullable=False)
    bairro = Column(String(40), nullable=False)
    cidade = Column(String(40), nullable=False)
    numero = Column(String(15), nullable=False)
    complemento = Column(String(320), nullable=False)
    estado = Column(String(40), nullable=False)
    
    def __repr__(self):
        return f'<Usuario {self.nome}>'