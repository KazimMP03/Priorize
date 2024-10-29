# Importa MongoClient para conectar ao banco de dados MongoDB
from pymongo import MongoClient

class MongoConnection:
    # Inicializa a conexão com o MongoDB usando a URI e o nome do banco de dados
    def __init__(self, uri="mongodb://localhost:27017/", db_name="Priorize"):
        self.client = MongoClient(uri)  # Cria um cliente MongoDB com a URI fornecida
        self.db = self.client[db_name]  # Conecta ao banco de dados especificado

    # Retorna uma coleção específica dentro do banco de dados
    def get_collection(self, collection_name):
        # Retorna a coleção solicitada a partir do banco
        return self.db[collection_name]

# Exemplo de uso
# mongo_conn = MongoConnection()
# tasks_collection = mongo_conn.get_collection("tasks")
