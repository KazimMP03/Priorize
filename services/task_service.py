# Importa a classe MongoConnection do módulo database.mongo_connection para gerenciar conexões com o MongoDB
from database.mongo_connection import MongoConnection
# Importa a classe Task do módulo models.task que representa uma tarefa
from models.task import Task
# Importa a classe ObjectId do módulo bson para trabalhar com IDs de documentos do MongoDB
from bson import ObjectId
# Importa a função validate_due_date do módulo utils.validators para validar datas de vencimento
from utils.validators import validate_due_date

class TaskService:
    # Inicializa a classe TaskService e estabelece uma conexão com a coleção de tarefas no MongoDB
    def __init__(self):
        mongo_conn = MongoConnection()  # Cria uma instância da conexão com o MongoDB
        self.tasks_collection = mongo_conn.get_collection("tasks")  # Obtém a coleção de tarefas

    # Cria uma nova tarefa após validar a data de vencimento
    def create_task(self, title, description, due_date, priority):
        # Valida se a data de vencimento não é menor que a data atual
        if not validate_due_date(due_date):
            raise ValueError("A data de vencimento não pode ser menor que a data de hoje.")
        
        # Cria uma instância da tarefa
        task = Task(title, description, due_date, priority)
        # Insere a tarefa no banco de dados como um dicionário
        self.tasks_collection.insert_one(task.to_dict())
        return task.id  # Retorna o ID da tarefa criada

    # Lista as tarefas filtradas por status e prioridade
    def list_tasks(self, status=None, priority=None):
        query = {}  # Dicionário para construir a consulta ao banco de dados
        if status:  # Adiciona o filtro de status, se fornecido
            query['status'] = status
        if priority:  # Adiciona o filtro de prioridade, se fornecido
            query['priority'] = priority

        # Busca as tarefas no banco de dados com base na consulta construída
        tasks_data = self.tasks_collection.find(query)

        tasks = []  # Lista para armazenar as tarefas criadas a partir dos dados do banco
        for task_data in tasks_data:
            # Cria uma instância de Task para cada tarefa retornada do banco
            task = Task(
                title=task_data['title'],
                description=task_data['description'],
                due_date=task_data['due_date'],
                priority=task_data['priority']
            )
            task.id = str(task_data['_id'])  # Atribui o ID do MongoDB à tarefa
            task.status = task_data['status']  # Atribui o status da tarefa
            tasks.append(task)  # Adiciona a tarefa à lista de tarefas
        
        return tasks  # Retorna a lista de tarefas

    # Atualiza os detalhes de uma tarefa existente
    def update_task(self, task_id, title=None, description=None, due_date=None, priority=None):
        updates = {}  # Dicionário para armazenar as atualizações a serem feitas
        if title:  # Se um novo título for fornecido, adiciona ao dicionário de atualizações
            updates['title'] = title
        if description:  # Se uma nova descrição for fornecida, adiciona ao dicionário de atualizações
            updates['description'] = description
        # Se uma nova data de vencimento for fornecida e for válida, adiciona ao dicionário de atualizações
        if due_date and validate_due_date(due_date):
            updates['due_date'] = due_date
        if priority:  # Se uma nova prioridade for fornecida, adiciona ao dicionário de atualizações
            updates['priority'] = priority

        # Atualiza a tarefa no banco de dados com as novas informações
        self.tasks_collection.update_one({"_id": task_id}, {"$set": updates})

    # Altera o status de uma tarefa existente
    def change_status(self, task_id, new_status):
        # Verifica se o novo status é válido
        if new_status not in ["pendente", "concluida"]:
            raise ValueError("Status inválido. Use 'pendente' ou 'concluida'.")
        
        # Atualiza o status da tarefa no banco de dados
        self.tasks_collection.update_one({"_id": task_id}, {"$set": {"status": new_status}})
    
    # Exclui uma tarefa existente do banco de dados
    def delete_task(self, task_id):
        # Remove a tarefa do banco de dados com base no ID fornecido
        self.tasks_collection.delete_one({"_id": task_id})
