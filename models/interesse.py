from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Interesse(Base):
    __tablename__ = 'interesses'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    animal_id = Column(Integer, ForeignKey('animais.id'), nullable=False)
    endereco = Column(String(320), nullable=False)
    condicoes_economicas = Column(String(320), nullable=False)
    motivacao = Column(String(500), nullable=False)
    status = Column(String(20), default='pendente')  # pendente, aprovado, negado

    usuario = relationship("Usuario")
    animal = relationship("Animal")

    def __repr__(self):
        return f"<Interesse usuario_id={self.usuario_id} animal_id={self.animal_id} status={self.status}>"
