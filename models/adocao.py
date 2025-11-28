from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # use o mesmo Base dos outros models

class Adocao(Base):
    __tablename__ = "adocoes"

    id = Column(Integer, primary_key=True, autoincrement=True)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    animal_id = Column(Integer, ForeignKey("animais.id"), nullable=False)

    status = Column(String, default="pendente")  
    # opções possíveis: pendente, aprovado, recusado, concluido

    # RELACIONAMENTOS
    usuario = relationship("Usuario")
    animal = relationship("Animal")

    def __repr__(self):
        return f"<Adocao usuario={self.usuario_id} animal={self.animal_id}>"