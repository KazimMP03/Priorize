from database.mongo_connection import MongoConnection
from models.task import Task
from bson import ObjectId
from utils.validators import validate_due_date

class TaskService:
    def __init__(self):
        mongo_conn = MongoConnection()
        self.tasks_collection = mongo_conn.get_collection("tasks")

    def create_task(self, title, description, due_date, priority):
        if not validate_due_date(due_date):
            raise ValueError("A data de vencimento não pode ser menor que a data de hoje.")
        
        task = Task(title, description, due_date, priority)
        self.tasks_collection.insert_one(task.to_dict())
        return task.id

    def list_tasks(self, status=None, priority=None):
        query = {}
        if status:
            query['status'] = status
        if priority:
            query['priority'] = priority

        tasks_data = self.tasks_collection.find(query)

        tasks = []
        for task_data in tasks_data:
            task = Task(
                title=task_data['title'],
                description=task_data['description'],
                due_date=task_data['due_date'],
                priority=task_data['priority']
            )
            task.id = str(task_data['_id'])  # Atribui o ID do MongoDB à tarefa
            task.status = task_data['status']
            tasks.append(task)
        
        return tasks

    def update_task(self, task_id, title=None, description=None, due_date=None, priority=None):
        updates = {}
        if title:
            updates['title'] = title
        if description:
            updates['description'] = description
        if due_date and validate_due_date(due_date):
            updates['due_date'] = due_date
        if priority:
            updates['priority'] = priority

        self.tasks_collection.update_one({"_id": task_id}, {"$set": updates})

    def change_status(self, task_id, new_status):
        if new_status not in ["pendente", "concluida"]:
            raise ValueError("Status inválido. Use 'pendente' ou 'concluida'.")
        
        self.tasks_collection.update_one({"_id": task_id}, {"$set": {"status": new_status}})

    def delete_task(self, task_id):
        self.tasks_collection.delete_one({"_id": task_id})
