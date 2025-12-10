from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Base dos modelos
Base = declarative_base()

# Criação da engine (APÓS os models serem importados no app principal)
engine = create_engine('sqlite:///dados.db', echo=True)

# Sessão
Sessao_base = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)

Base.metadata.create_all(engine)
