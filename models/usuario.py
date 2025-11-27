from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(40), nullable=False)
    nome_completo: Mapped[str] = mapped_column(String(320), nullable=False)
    telefone: Mapped[str] = mapped_column(String(15), nullable=False)
    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(100), nullable=False)

    rua: Mapped[str] = mapped_column(String(40), nullable=False)
    bairro: Mapped[str] = mapped_column(String(40), nullable=False)
    cidade: Mapped[str] = mapped_column(String(40), nullable=False)
    numero: Mapped[str] = mapped_column(String(15), nullable=False)
    complemento: Mapped[str] = mapped_column(String(320), nullable=False)
    estado: Mapped[str] = mapped_column(String(40), nullable=False)


    def __repr__(self):
        return f"<Usuario {self.nome}>"
