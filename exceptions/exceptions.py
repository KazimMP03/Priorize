class InvalidDateFormatError(Exception):
    # Exceção para formato de data inválido.
    def __init__(self):
        super().__init__("Formato de data inválido. Use DD-MM-YYYY.")

class PastDueDateError(Exception):
    # Exceção para data de vencimento no passado.
    def __init__(self):
        super().__init__("A data de vencimento deve ser maior que a data atual.")

class InvalidPriorityError(Exception):
    # Exceção para prioridade inválida.
    def __init__(self):
        super().__init__("Prioridade inválida. Use 'baixa', 'moderada' ou 'alta'.")

class InvalidStatusError(Exception):
    # Exceção para status inválido.
    def __init__(self):
        super().__init__("Status inválido. Use 'pendente' ou 'concluida'.")
