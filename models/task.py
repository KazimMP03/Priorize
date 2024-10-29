# Importa a classe datetime para manipulação de datas e horas
from datetime import datetime
# Importa o módulo uuid para geração de IDs únicos
import uuid

class Task:
    # Inicializa uma nova instância de Task com ID, título, descrição, status, data de criação, data de vencimento e prioridade
    def __init__(self, title, description, due_date, priority):
        self.id = str(uuid.uuid4())  # Gera um ID único para a tarefa
        self.title = title  # Define o título da tarefa
        self.description = description  # Define a descrição da tarefa
        self.status = 'pendente'  # Define o status inicial como 'pendente'
        self.created_at = datetime.now()  # Armazena a data e hora de criação da tarefa
        self.due_date = due_date  # Define a data de vencimento
        self.priority = priority  # Define a prioridade da tarefa (baixa, moderada, alta)
    
    # Retorna uma representação em string legível da tarefa
    def __str__(self):
        due_date_str = self.due_date.strftime("%d-%m-%Y")  # Converte a data para o formato DD-MM-YYYY
        return (
            f"Tarefa ID: {self.id}\n"
            f"Título: {self.title}\n"
            f"Descrição: {self.description}\n"
            f"Data de Vencimento: {due_date_str}\n"
            f"Prioridade: {self.priority}\n"
            f"Status: {self.status}\n"
            "---------------------------"
        )
    
    # Converte os atributos da tarefa para um dicionário, facilitando a manipulação e o armazenamento em um banco de dados
    def to_dict(self):
        return {
            "_id": self.id,  # ID único da tarefa
            "title": self.title,  # Título da tarefa
            "description": self.description,  # Descrição da tarefa
            "status": self.status,  # Status atual da tarefa
            "created_at": self.created_at,  # Data de criação da tarefa
            "due_date": self.due_date,  # Data de vencimento da tarefa
            "priority": self.priority  # Prioridade da tarefa
        }
