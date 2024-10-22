from datetime import datetime

def validate_due_date(due_date):
    """Valida se a data de vencimento não é menor que a data atual."""
    return due_date >= datetime.now()
