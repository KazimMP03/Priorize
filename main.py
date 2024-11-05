# Importa o serviço de tarefas, que gerencia as operações relacionadas a tarefas
from services.task_service import TaskService
# Importa a classe datetime para manipulação de datas
from datetime import datetime
# Importa as classes de exceções personalizadas para tratamento de erros
from exceptions.exceptions import InvalidDateFormatError, PastDueDateError, InvalidPriorityError, InvalidStatusError
# Importa a função para validação de datas
from utils.validators import validate_due_date

# Cria uma instância do serviço de tarefas
task_service = TaskService()

def main():
    while True:  # Loop principal do menu
        print("\nEscolha uma opção:")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Alterar status da tarefa")
        print("4. Atualizar tarefa")
        print("5. Excluir tarefa")
        print("0. Sair")
        
        # Captura a escolha do usuário
        choice = input("\nDigite a opção: ")

        if choice == "1":  # Opção para criar uma nova tarefa
            title = ""
            description = ""
            due_date = None
            priority = ""

            while True:  # Loop para criar a tarefa
                try:
                    if not title:  # Verifica se o título não foi informado
                        title = input("Título: ")
                    if not description:  # Verifica se a descrição não foi informada
                        description = input("Descrição: ")

                    if due_date is None:  # Se a data de vencimento não foi informada
                        due_date_str = input("Data de vencimento (DD-MM-YYYY): ")
                        try:
                            # Converte a string de data para o formato datetime
                            due_date = datetime.strptime(due_date_str, "%d-%m-%Y")
                            # Valida se a data de vencimento é válida (não é no passado)
                            if not validate_due_date(due_date):
                                raise PastDueDateError()
                        except ValueError:
                            raise InvalidDateFormatError()  # Erro de formato inválido

                    if not priority:  # Verifica se a prioridade não foi informada
                        priority = input("Prioridade (baixa, moderada, alta): ").lower()
                        # Valida se a prioridade é uma das opções válidas
                        if priority not in ["baixa", "moderada", "alta"]:
                            raise InvalidPriorityError()

                    # Cria a tarefa utilizando o serviço de tarefas
                    task_service.create_task(title, description, due_date, priority)
                    print("Tarefa criada com sucesso!")
                    break  # Sai do loop se a tarefa foi criada com sucesso

                except (InvalidDateFormatError, PastDueDateError, InvalidPriorityError) as e:
                    # Captura erros de data e prioridade e exibe uma mensagem
                    print(f"Erro: {e}. Tente novamente.")
                    # Reseta apenas os campos que falharam
                    if isinstance(e, InvalidDateFormatError) or isinstance(e, PastDueDateError):
                        due_date = None  # Força a reentrada da data
                    if isinstance(e, InvalidPriorityError):
                        priority = ""  # Força a reentrada da prioridade

        elif choice == "2":  # Opção para listar tarefas
            status = ""
            priority = ""

            while True:  # Loop para listar tarefas
                try:
                    if not status:  # Verifica se o status não foi informado
                        status = input("Filtrar por status (pendente, concluida ou deixar vazio): ").lower()
                        if status and status not in ["pendente", "concluida"]:
                            raise InvalidStatusError()
                    
                    if not priority:  # Verifica se a prioridade não foi informada
                        priority = input("Filtrar por prioridade (baixa, moderada, alta ou deixar vazio): ").lower()
                        if priority and priority not in ["baixa", "moderada", "alta"]:
                            raise InvalidPriorityError()

                    # Lista as tarefas com base nos filtros fornecidos
                    tasks = task_service.list_tasks(status, priority)
                    if tasks:
                        for task in tasks:
                            print(f"\n{task}")
                    else:
                        print("Nenhuma tarefa encontrada.")
                    break  # Sai do loop se as tarefas foram listadas

                except (InvalidStatusError, InvalidPriorityError) as e:
                    # Captura erros de status e prioridade e exibe uma mensagem
                    print(f"Erro: {e}. Tente novamente.")
                    # Reseta apenas os campos que falharam
                    if isinstance(e, InvalidStatusError):
                        status = ""  # Força a reentrada do status
                    if isinstance(e, InvalidPriorityError):
                        priority = ""  # Força a reentrada da prioridade

        elif choice == "3":  # Opção para alterar o status de uma tarefa
            task_id = input("ID da tarefa: ")
            new_status = ""

            while True:  # Loop para alterar o status
                try:
                    new_status = input("Novo status (pendente, concluida): ").lower()
                    if new_status not in ["pendente", "concluida"]:
                        raise InvalidStatusError()
                    
                    # Atualiza o status da tarefa
                    task_service.change_status(task_id, new_status)
                    print("Status atualizado com sucesso!")
                    break  # Sai do loop se o status foi alterado com sucesso
                except InvalidStatusError as e:
                    # Captura erro de status inválido e exibe uma mensagem
                    print(f"Erro: {e}. Tente novamente.")

        elif choice == "4":  # Opção para atualizar uma tarefa
            task_id = input("ID da tarefa: ")
            title = input("Novo título (ou deixar vazio): ")
            description = input("Nova descrição (ou deixar vazio): ")
            due_date = None
            priority = ""

            while True:  # Loop para atualizar a tarefa
                try:
                    if not due_date:  # Verifica se a nova data de vencimento não foi informada
                        due_date_str = input("Nova data de vencimento (DD-MM-YYYY) ou deixar vazio: ")
                        if due_date_str:
                            try:
                                # Converte a string de data para o formato datetime
                                due_date = datetime.strptime(due_date_str, "%d-%m-%Y")
                                # Valida se a nova data de vencimento é válida
                                if not validate_due_date(due_date):
                                    raise PastDueDateError()
                            except ValueError:
                                raise InvalidDateFormatError()

                    if not priority:  # Verifica se a nova prioridade não foi informada
                        priority = input("Nova prioridade (baixa, moderada, alta ou deixar vazio): ").lower()
                        if priority and priority not in ["baixa", "moderada", "alta"]:
                            raise InvalidPriorityError()

                    # Atualiza a tarefa com os novos dados fornecidos
                    task_service.update_task(task_id, title, description, due_date, priority)
                    print("Tarefa atualizada com sucesso!")
                    break  # Sai do loop se a tarefa foi atualizada com sucesso
                except (InvalidDateFormatError, PastDueDateError, InvalidPriorityError) as e:
                    # Captura erros de data e prioridade e exibe uma mensagem
                    print(f"Erro: {e}. Tente novamente.")
                    # Reseta apenas os campos que falharam
                    if isinstance(e, InvalidDateFormatError) or isinstance(e, PastDueDateError):
                        due_date = None  # Força a reentrada da data
                    if isinstance(e, InvalidPriorityError):
                        priority = ""  # Força a reentrada da prioridade

        elif choice == "5":  # Opção para excluir uma tarefa
            task_id = input("ID da tarefa: ")
            task_service.delete_task(task_id)  # Chama o método para excluir a tarefa
            print("Tarefa excluída com sucesso!")

        elif choice == "0":  # Opção para sair do programa
            break  # Sai do loop principal e encerra o programa

        else:
            print("Opção inválida. Tente novamente.")  # Mensagem para opção inválida

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
