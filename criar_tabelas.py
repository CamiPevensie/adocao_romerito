from database import Base, engine
from models.usuario import Usuario
from models.animal import Animal
from models.adocao import Adocao
from models.interesse import Interesse


# Cria todas as tabelas no banco de dados
Base.metadata.create_all(engine)