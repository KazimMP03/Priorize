# Importa a classe TaskService do módulo services.task_service para manipular tarefas
from services.task_service import TaskService
# Importa a classe datetime do módulo datetime para trabalhar com datas
from datetime import datetime

# Cria uma instância do serviço de tarefas
task_service = TaskService()

def main():
    # Loop infinito para manter o menu ativo até que o usuário decida sair
    while True:
        # Exibe as opções do menu
        print("\nEscolha uma opção:")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Alterar status da tarefa")
        print("4. Atualizar tarefa")
        print("5. Excluir tarefa")
        print("0. Sair")
        
        # Solicita ao usuário que escolha uma opção
        choice = input("\nDigite a opção: ")

        # Opção para criar uma nova tarefa
        if choice == "1":
            title = input("Título: ")  # Solicita o título da tarefa
            description = input("Descrição: ")  # Solicita a descrição da tarefa
            due_date_str = input("Data de vencimento (DD-MM-YYYY): ")  # Solicita a data de vencimento
            # Converte a string da data para um objeto datetime, utilizando o formato brasileiro
            due_date = datetime.strptime(due_date_str, "%d-%m-%Y")  
            priority = input("Prioridade (baixa, moderada, alta): ")  # Solicita a prioridade da tarefa
            # Cria a tarefa utilizando o serviço de tarefas
            task_service.create_task(title, description, due_date, priority)
            print("Tarefa criada com sucesso!")  # Confirmação da criação da tarefa
        
        # Opção para listar todas as tarefas
        elif choice == "2":
            status = input("Filtrar por status (pendente, concluida ou deixar vazio): ")  # Filtra por status
            priority = input("Filtrar por prioridade (baixa, moderada, alta ou deixar vazio): ")  # Filtra por prioridade
            # Obtém a lista de tarefas filtradas
            tasks = task_service.list_tasks(status, priority)
            # Verifica se há tarefas a serem exibidas
            if tasks:
                for task in tasks:
                    print(f"\n{task}")  # Imprime cada tarefa, chamando o método __str__ da classe Task
            else:
                print("Nenhuma tarefa encontrada.")  # Mensagem caso não haja tarefas
        
        # Opção para alterar o status de uma tarefa existente
        elif choice == "3":
            task_id = input("ID da tarefa: ")  # Solicita o ID da tarefa a ser alterada
            new_status = input("Novo status (pendente, concluida): ")  # Solicita o novo status
            # Altera o status da tarefa utilizando o serviço
            task_service.change_status(task_id, new_status)
            print("Status atualizado com sucesso!")  # Confirmação da atualização do status

        # Opção para atualizar os detalhes de uma tarefa existente
        elif choice == "4":
            task_id = input("ID da tarefa: ")  # Solicita o ID da tarefa a ser atualizada
            title = input("Novo título (ou deixar vazio): ")  # Solicita um novo título
            description = input("Nova descrição (ou deixar vazio): ")  # Solicita uma nova descrição
            due_date_str = input("Nova data de vencimento (DD-MM-YYYY) ou deixar vazio: ")  # Solicita uma nova data de vencimento
            # Verifica se uma nova data foi fornecida
            if due_date_str:
                due_date = datetime.strptime(due_date_str, "%d-%m-%Y")  # Converte a nova data se fornecida
            else:
                due_date = None  # Mantém a data como None se não fornecida
            priority = input("Nova prioridade (baixa, moderada, alta ou deixar vazio): ")  # Solicita nova prioridade
            # Atualiza a tarefa utilizando o serviço de tarefas
            task_service.update_task(task_id, title, description, due_date, priority)
            print("Tarefa atualizada com sucesso!")  # Confirmação da atualização da tarefa
        
        # Opção para excluir uma tarefa existente
        elif choice == "5":
            task_id = input("ID da tarefa: ")  # Solicita o ID da tarefa a ser excluída
            # Exclui a tarefa utilizando o serviço
            task_service.delete_task(task_id)
            print("Tarefa excluída com sucesso!")  # Confirmação da exclusão da tarefa

        # Opção para sair do programa
        elif choice == "0":
            break  # Sai do loop, encerrando o programa

        # Caso a opção escolhida não seja válida
        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de erro para opção inválida

# Execução da função main se o script for executado diretamente
if __name__ == "__main__":
    main()
