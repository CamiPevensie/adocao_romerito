from database import Base, engine
from models.usuario import Usuario
from models.animal import Animal

# Cria todas as tabelas no banco de dados
Base.metadata.create_all(engine)