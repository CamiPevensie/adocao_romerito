from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Boolean, ForeignKey
from database import Base

class Animal(Base):
    __tablename__ = "animais"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(40), nullable=False)
    raca: Mapped[str] = mapped_column(String(40), nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    sexo: Mapped[str] = mapped_column(String(40), nullable=False)
    porte: Mapped[str] = mapped_column(String(40), nullable=False)
    vacinado: Mapped[bool] = mapped_column(Boolean, nullable=False)
    vacinas_tomadas: Mapped[str] = mapped_column(String(320), nullable=False)
    sobre: Mapped[str] = mapped_column(String(320), nullable=False)
    foto: Mapped[str] = mapped_column(String(700), nullable=False)
    localizacao: Mapped[str] = mapped_column(String(100), nullable=False)
    nome_protetor: Mapped[str] = mapped_column(String(320), nullable=False)
    telefone_contato: Mapped[str] = mapped_column(String(15), nullable=False)
    email_contato: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Animal {self.nome}>"
