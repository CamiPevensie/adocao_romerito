from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Cria a engine (faz a conexão com o banco)
engine = create_engine('sqlite:///dados.db', echo=True)

# Cria a sessão
Sessao_base = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


# Cria a base dos modelos (Usuario, Animal, etc.)
Base = declarative_base()
