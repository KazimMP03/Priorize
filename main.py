from services.task_service import TaskService
from datetime import datetime

task_service = TaskService()

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Alterar status da tarefa")
        print("4. Atualizar tarefa")
        print("5. Excluir tarefa")
        print("0. Sair")
        
        choice = input("\nDigite a opção: ")

        if choice == "1":
            title = input("Título: ")
            description = input("Descrição: ")
            due_date_str = input("Data de vencimento (DD-MM-YYYY): ")
            due_date = datetime.strptime(due_date_str, "%d-%m-%Y") # Formato de data brasileiro
            priority = input("Prioridade (baixa, moderada, alta): ")
            task_service.create_task(title, description, due_date, priority)
            print("Tarefa criada com sucesso!")
        
        elif choice == "2":
            status = input("Filtrar por status (pendente, concluida ou deixar vazio): ")
            priority = input("Filtrar por prioridade (baixa, moderada, alta ou deixar vazio): ")
            tasks = task_service.list_tasks(status, priority)
            if tasks:
                for task in tasks:
                    print(f"\n{task}")  # O __str__ da classe Task será chamado aqui
            else:
                print("Nenhuma tarefa encontrada.")

        elif choice == "3":
            task_id = input("ID da tarefa: ")
            new_status = input("Novo status (pendente, concluida): ")
            task_service.change_status(task_id, new_status)
            print("Status atualizado com sucesso!")

        elif choice == "4":
            task_id = input("ID da tarefa: ")
            title = input("Novo título (ou deixar vazio): ")
            description = input("Nova descrição (ou deixar vazio): ")
            due_date_str = input("Nova data de vencimento (YYYY-MM-DD) ou deixar vazio: ")
            if due_date_str:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            else:
                due_date = None
            priority = input("Nova prioridade (baixa, moderada, alta ou deixar vazio): ")
            task_service.update_task(task_id, title, description, due_date, priority)
            print("Tarefa atualizada com sucesso!")
        
        elif choice == "5":
            task_id = input("ID da tarefa: ")
            task_service.delete_task(task_id)
            print("Tarefa excluída com sucesso!")

        elif choice == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
