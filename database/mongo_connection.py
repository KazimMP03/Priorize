from pymongo import MongoClient

class MongoConnection:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="Priorize"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]

# Exemplo de uso
# mongo_conn = MongoConnection()
# tasks_collection = mongo_conn.get_collection("tasks")
