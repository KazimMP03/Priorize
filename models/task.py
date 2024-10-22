from datetime import datetime
import uuid

class Task:
    def __init__(self, title, description, due_date, priority):
        self.id = str(uuid.uuid4())  # Gerar ID único
        self.title = title
        self.description = description
        self.status = 'pendente'
        self.created_at = datetime.now()
        self.due_date = due_date
        self.priority = priority  # baixa, moderada, alta
    
    def __str__(self):
        """Retorna uma string legível para a tarefa"""
        due_date_str = self.due_date.strftime("%d-%m-%Y")  # Formato DD-MM-YYYY
        return (
            f"Tarefa ID: {self.id}\n"
            f"Título: {self.title}\n"
            f"Descrição: {self.description}\n"
            f"Data de Vencimento: {due_date_str}\n"
            f"Prioridade: {self.priority}\n"
            f"Status: {self.status}\n"
            "---------------------------"
        )
    
    def to_dict(self):
        return {
            "_id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "due_date": self.due_date,
            "priority": self.priority
        }
